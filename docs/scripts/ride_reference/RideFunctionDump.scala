package docgen

// Dumps every built-in Ride function, as the node itself sees it, to JSON,
// plus the names of the types and global variables of each stdlib version.
//
// Not part of node-scala: generate_ride_reference.py copies this file into a
// node-scala checkout's lang/jvm module, runs it with sbt, and deletes it
// again. Reading the compiled contexts instead of parsing Scala source is what
// makes costs set through helper functions (the BigInt operators, for
// example) or picked by version inside a context builder (the hash functions)
// come out right: the cost of a function in version v is costByLibVersion(v)
// on the context built for v, which is exactly what utils.estimate charges.

import com.decentralchain.DocSource
import com.decentralchain.common.utils.EitherExt2.*
import com.decentralchain.lang.directives.values.*
import com.decentralchain.lang.directives.{DirectiveDictionary, DirectiveSet}
import com.decentralchain.lang.utils.lazyContexts
import com.decentralchain.lang.v1.FunctionHeader
import com.decentralchain.lang.v1.compiler.UtilityFunctionPrefix
import com.decentralchain.lang.v1.evaluator.ctx.BaseFunction
import com.decentralchain.lang.v1.traits.Environment

import java.nio.charset.StandardCharsets.UTF_8
import java.nio.file.{Files, Paths}

object RideFunctionDump {
  // The script kinds whose function sets differ. Library scripts compile
  // against the Expression context, so they don't need a row of their own.
  private val kinds: Seq[(String, ScriptType, ContentType)] = Seq(
    ("account", Account, Expression),
    ("asset", Asset, Expression),
    ("dapp", Account, DApp)
  )

  // Per-version doc tables keep the hjson category (file name), which the
  // merged DocSource.funcData drops. Key: (name, param types, version).
  private def docsFor(v: Int): Map[(String, List[String], Int), (String, List[String], String, Int)] = v match {
    case 3 => DocSource.funcsV3
    case 4 => DocSource.funcsV4
    case 5 => DocSource.funcsV5
    case 6 => DocSource.funcsV6
    case 7 => DocSource.funcsV7
    case 8 => DocSource.funcsV8
    case 9 => DocSource.funcsV9
    case _ => Map.empty
  }

  private def q(s: String): String = {
    val sb = new StringBuilder("\"")
    s.foreach {
      case '"'          => sb ++= "\\\""
      case '\\'         => sb ++= "\\\\"
      case '\n'         => sb ++= "\\n"
      case '\r'         => sb ++= "\\r"
      case '\t'         => sb ++= "\\t"
      case c if c < ' ' => sb ++= f"\\u${c.toInt}%04x"
      case c            => sb += c
    }
    sb += '"'
    sb.result()
  }

  private def arr(items: Iterable[String]): String = items.mkString("[", ",", "]")

  private def headerId(h: FunctionHeader): String = h match {
    case FunctionHeader.Native(id)        => s"native:$id"
    case FunctionHeader.User(internal, _) => s"user:$internal"
  }

  private def functionJson(f: BaseFunction[Environment], version: StdLibVersion, kindsAvailable: Seq[String]): String = {
    val argTypes = f.signature.args.map(_._2.toString).toList
    val doc      = docsFor(version.id).get((f.name, argTypes, version.id))
    Seq(
      s"\"name\":${q(f.name)}",
      s"\"header\":${q(headerId(f.header))}",
      s"\"args\":${arr(f.args.zip(argTypes).map { case (n, t) => s"{\"name\":${q(n)},\"type\":${q(t)}}" })}",
      s"\"result\":${q(f.signature.result.toString)}",
      s"\"cost\":${f.costByLibVersion(version)}",
      s"\"deprecated\":${f.deprecated}",
      s"\"kinds\":${arr(kindsAvailable.map(q))}",
      s"\"category\":${doc.fold("null")(d => q(d._3))}",
      s"\"doc\":${doc.fold("null")(d => q(d._1))}"
    ).mkString("{", ",", "}")
  }

  def main(args: Array[String]): Unit = {
    require(args.length == 1, "usage: RideFunctionDump <out.json>")

    val versions = DirectiveDictionary[StdLibVersion].all.toSeq.sortBy(_.id)
    val perVersion = versions.map { version =>
      // Same flags as utils.ctx(): every fix that is active on the network today.
      val ctxs = kinds.collect {
        case (kind, scriptType, contentType) if contentType != DApp || version >= V3 =>
          val ds = DirectiveSet(version, scriptType, contentType).explicitGet()
          kind -> lazyContexts((ds, true, true, true)).value()
      }
      val byKind    = ctxs.map { case (kind, ctx) => kind -> ctx.functions.filterNot(_.name.startsWith(UtilityFunctionPrefix)).toSeq }
      val typeNames = ctxs.flatMap(_._2.types.map(_.name)).distinct.sorted
      val varNames  = ctxs.flatMap(_._2.vars.keys).distinct.sorted
      val functions = byKind
        .flatMap { case (kind, fs) => fs.map(f => (headerId(f.header), f, kind)) }
        .groupBy(_._1)
        .toSeq
        .map { case (_, entries) =>
          val f = entries.head._2
          entries.foreach { case (_, other, _) =>
            require(other.costByLibVersionMap == f.costByLibVersionMap, s"${f.name}: cost differs between script kinds")
          }
          (f, kinds.map(_._1).filter(k => entries.exists(_._3 == k)))
        }
        .sortBy { case (f, _) => (f.name, f.signature.args.map(_._2.toString).mkString(","), headerId(f.header)) }
        .map { case (f, ks) => functionJson(f, version, ks) }
      s"${q(version.id.toString)}:{\"types\":${arr(typeNames.map(q))},\"vars\":${arr(varNames.map(q))},\"functions\":${functions.mkString("[\n", ",\n", "\n]")}}"
    }

    Files.write(Paths.get(args(0)), perVersion.mkString("{\n", ",\n", "\n}\n").getBytes(UTF_8))
  }
}
