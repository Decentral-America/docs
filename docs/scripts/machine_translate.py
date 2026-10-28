#!/usr/bin/env python3
"""Machine-translate the messages `translate_catalogs.py export` writes, with an Argos
Translate model (an OPUS-MT model run by CTranslate2), keeping the markup intact.

  machine_translate.py <model_dir> <locale> <in.jsonl> <out.jsonl>

<model_dir> is an unpacked Argos package for English to <locale>: the folder that holds
`model/` and `sentencepiece.model`. The packages are listed in
https://github.com/argosopentech/argospm-index (index.json, `from_code` "en"); an
.argosmodel file is a zip. Needs `pip install ctranslate2 sentencepiece`, which has
wheels for Python 3.12 on Intel Macs. <out.jsonl> goes to `translate_catalogs.py
import`, which still checks every translation.

Before a message goes to the engine, everything the engine must not touch becomes a
placeholder: code literals, roles, URLs, substitutions, HTML tags, CamelCase and dotted
identifiers, and the names the glossary never translates. The visible text of links,
link roles and bold or italic text is translated on its own and put back inside its
markup. A sentence whose placeholders don't all come back is retried with another
placeholder style (models differ in which ones they keep); a message with a sentence
that never comes back intact is left out, so it stays in English. Messages that are
code (Ride signatures, type names, hashes, numbers) are copied unchanged. Last, inline
markup gets a space wherever reST would not see it as markup, for example between a
role and a CJK character (space_markup).

The result is raw machine translation. A locale still needs a native or fluent
speaker's review before it goes into docs/locales/PUBLISHED (see AGENTS.md).
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys
import time
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from translate_catalogs import KEEP_ENGLISH  # noqa: E402
from translations import LINK_ROLES, kept_names  # noqa: E402

MARK = re.compile("\ue000(\\d+)\ue001")   # a placeholder while a message is being worked on

# Placeholder styles, in the order they are tried. ZQ0 survives best in most models;
# Arabic keeps [0] and {0} better, and Bengali keeps none of them reliably.
STYLES = {
    "default": ["ZQ{i}", "X{i}X", "[{i}]", "{{{i}}}"],
    "ar": ["[{i}]", "{{{i}}}", "X{i}X", "ZQ{i}"],
}
STYLE_FIND = {
    "ZQ{i}": r"ZQ(\d+)", "X{i}X": r"X(\d+)X", "[{i}]": r"\[(\d+)\]", "{{{i}}}": r"\{(\d+)\}",
}
NON_LATIN = {"ar", "bn", "hi", "ja", "ru", "zh"}
NO_SPACES = {"ja", "zh"}                     # sentences are joined without a space

# Code and inline markup, scanned left to right like translations.SPAN: ``literal``,
# :role:`body` / {role}`body`, `text <url>`_ and `name`_ references, `literal`.
INLINE = re.compile(
    r"``.+?``"
    r"|(?P<role>:[A-Za-z][\w.+-]*:|(?<![\w}])\{[a-z][\w.+-]*\})`(?P<body>[^`]*)`"
    r"|`(?P<ref>[^`]*)`(?P<under>__?)(?!\w)"
    r"|`[^`]*`"
)
TITLED = re.compile(r"^(?P<text>.*?\S)\s*(?P<target><[^<>]+>)$")     # `text <target>`
IMAGE = re.compile(r"!\[[^\]]*\]\([^)\s]+\)")
LINK = re.compile(r"\[(?P<text>[^\]]+)\]\((?P<url>[^)\s]+)\)")
OPAQUE = re.compile(
    r"https?://[^\s<>()\[\]`]+[^\s<>()\[\]`.,;:!?'\"]"         # bare URL
    r"|</?[a-zA-Z][^<>]*>"                                      # HTML tag
    r"|(?<![\w|])\|\w[^|]*?\|(?![\w|])"                          # |substitution|
    r"|\[[#*\w-]*\]_"                                           # footnote reference
    r"|\{[^{}\s]*\}"                                            # {placeholder}
)
STRONG = re.compile(r"\*\*(?=\S)(?P<text>.+?)(?<=\S)\*\*")
EMPHASIS = re.compile(r"(?<![*\w])\*(?=[^\s*])(?P<text>[^*]+?)(?<=[^\s*])\*(?![*\w])")
IDENTIFIER = re.compile(
    r"(?<![\w.])(?:"
    r"[A-Z][a-z0-9]+(?:[A-Z][a-z0-9]*)+"                        # CamelCase
    r"|[a-z]+(?:[A-Z][a-z0-9]*)+"                               # camelCase
    r"|(?!e\.g\b|i\.e\b)[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+(?:\(\))?"  # dotted.name, domain.tld
    r"|\w+_\w+"                                                 # snake_case
    r"|\w+\(\)"                                                 # call()
    r")(?![\w])"
)
SIGNATURE = re.compile(r"^@?[A-Za-z_][\w.]*\(.*\)(?:\s*:\s*\S.*)?$")
RIDE_TYPES = {"Any", "BigInt", "Boolean", "ByteVector", "Int", "List", "Nothing", "String", "Unit"}
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z\ue000\"'(\[])")
LETTER = re.compile(r"[^\W\d_]")


def is_code(msgid: str) -> bool:
    """A message that is code or a value, copied as it is."""
    text = msgid.strip()
    if SIGNATURE.match(text) and ". " not in text:
        return True
    if text in RIDE_TYPES or re.fullmatch(r"[A-Z0-9]{2,}s?", text):
        return True
    word = text.rstrip(".,:;!?")
    return " " not in word and (bool(re.search(r"[\d_.|\[\]()<>=!&+*/%@#:]", word)) or len(word) >= 20)


class Masked:
    """A message with its markup swapped for placeholders. `items[n]` is either the text
    placeholder n stands for, or a (prefix, masked text, suffix) whose text is translated."""

    def __init__(self, names: list[str]):
        self.items: list[str | tuple[str, str, str]] = []
        self.names = re.compile(
            r"(?<![\w.])(?:" + "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True)) + r"|dApps)(?![\w])"
        )

    def hold(self, item: str | tuple[str, str, str]) -> str:
        self.items.append(item)
        return f"\ue000{len(self.items) - 1}\ue001"

    def titled(self, prefix: str, text: str, suffix: str, whole: str) -> str:
        """Hold markup with visible text: translate the text unless it is code."""
        if is_code(text) or "(" in text or not LETTER.search(MARK.sub("", text)):
            return self.hold(whole)
        return self.hold((prefix, self.mask(text, nested=True), suffix))

    def mask(self, text: str, nested: bool = False) -> str:
        def inline(m: re.Match) -> str:
            whole = m.group(0)
            if m.group("role") and m.group("role").strip(":{}") in LINK_ROLES:
                titled = TITLED.match(m.group("body"))
                if titled and not nested:
                    return self.titled(m.group("role") + "`", titled.group("text"), f" {titled.group('target')}`", whole)
            if m.group("ref") is not None and not nested:
                titled = TITLED.match(m.group("ref"))
                if titled and titled.group("target").startswith("<http"):
                    return self.titled("`", titled.group("text"), f" {titled.group('target')}`{m.group('under')}", whole)
            return self.hold(whole)

        text = INLINE.sub(inline, text)
        text = IMAGE.sub(lambda m: self.hold(m.group(0)), text)
        if nested:
            text = LINK.sub(lambda m: self.hold(m.group(0)), text)
        else:
            text = LINK.sub(lambda m: self.titled("[", m.group("text"), f"]({m.group('url')})", m.group(0)), text)
        text = OPAQUE.sub(lambda m: self.hold(m.group(0)), text)
        for pattern, mark in ((STRONG, "**"), (EMPHASIS, "*")):
            if nested:
                text = pattern.sub(lambda m: self.hold(m.group(0)), text)
            else:
                text = pattern.sub(lambda m, mark=mark: self.titled(mark, m.group("text"), mark, m.group(0)), text)
        text = self.names.sub(lambda m: self.hold(m.group(0)), text)
        return IDENTIFIER.sub(lambda m: self.hold(m.group(0)), text)

    def segments(self, outer: str) -> list[str]:
        """The texts to translate: the message, then the visible text of each held markup."""
        return [outer] + [item[1] for item in self.items if isinstance(item, tuple)]

    def restore(self, outer: str, translated: list[str]) -> str:
        inner = iter(translated[1:])
        texts = {n: next(inner) for n, item in enumerate(self.items) if isinstance(item, tuple)}

        def put(text: str) -> str:
            def one(m: re.Match) -> str:
                n = int(m.group(1))
                item = self.items[n]    # held markup can itself hold earlier placeholders
                return put(item) if isinstance(item, str) else put(item[0]) + put(texts[n]) + put(item[2])
            return MARK.sub(one, text)

        return space_markup(put(translated[0]))


# Inline markup in a finished translation: ``literal``, roles, `references`_, `literal`,
# **strong** and *emphasis*. A CJK character counts as a neighbour here, unlike in INLINE.
MARKUP = re.compile(
    r"``.+?``"
    r"|(?::[A-Za-z][\w.+-]*:|(?<!\})\{[a-z][\w.+-]*\})`[^`]*`"
    r"|`[^`]*`(?:__?)?"
    r"|\*\*(?=\S).+?(?<=\S)\*\*"
    r"|(?<![*A-Za-z0-9])\*(?=[^\s*])[^*]+?(?<=[^\s*])\*(?![*A-Za-z0-9])"
)
# docutils only sees inline markup that has whitespace, one of these ASCII characters or a
# non-ASCII punctuation mark of these categories on each side (reStructuredText spec,
# "Inline markup recognition rules"): `.:ref:` is not a role, `。:ref:` is.
BEFORE_MARKUP = (set("-:/'\"<([{"), {"Pd", "Po", "Pi", "Pf", "Ps"})
AFTER_MARKUP = (set("-.,:;!?\\/'\")]}>"), {"Pd", "Po", "Pi", "Pf", "Pe"})


def space_markup(text: str) -> str:
    """Put a space between inline markup and a neighbour reST would not accept, such as a
    CJK character, a full stop before a role or an opening bracket right after one."""
    def fits(char: str, rule: tuple[set[str], set[str]]) -> bool:
        if char.isspace():
            return True
        return char in rule[0] if char.isascii() else unicodedata.category(char) in rule[1]

    out, last = [], 0
    for m in MARKUP.finditer(text):
        start, end = m.span()
        out.append(text[last:start])
        if start and not fits(text[start - 1], BEFORE_MARKUP):
            out.append(" ")
        out.append(m.group(0))
        if end < len(text) and not fits(text[end], AFTER_MARKUP):
            out.append(" ")
        last = end
    out.append(text[last:])
    return "".join(out)


class Engine:
    def __init__(self, model_dir: pathlib.Path, locale: str):
        import ctranslate2
        import sentencepiece

        threads = int(os.environ.get("MT_THREADS", "6"))
        self.translator = ctranslate2.Translator(
            str(model_dir / "model"), device="cpu", compute_type="int8", intra_threads=threads
        )
        self.sp = sentencepiece.SentencePieceProcessor(model_file=str(model_dir / "sentencepiece.model"))
        self.locale = locale
        self.styles = STYLES.get(locale, STYLES["default"])

    def _usable(self, source: str, output: str) -> bool:
        if not output or len(output) > 4 * len(source) + 40:
            return False
        if output == source and not re.search(r"\b[a-z]{3,}\b", source):
            return True             # only acronyms and placeholders: nothing to translate
        if self.locale in NON_LATIN:
            # An untranslated echo of the English is a failure, not a translation.
            letters = LETTER.findall(re.sub(r"ZQ\d+|X\d+X", "", output))
            latin = sum(1 for c in letters if c.isascii())
            if letters and latin / len(letters) > 0.6:
                return False
        return True

    def sentences(self, todo: list[str]) -> list[str | None]:
        """Translate masked sentences; None where no placeholder style comes back intact."""
        done: list[str | None] = [None] * len(todo)
        pending = list(range(len(todo)))
        for style in self.styles:
            if not pending:
                break
            batch, local, retry, tried = [], [], [], []
            for i in pending:
                order = list(dict.fromkeys(MARK.findall(todo[i])))
                styled = MARK.sub(lambda m, order=order: style.format(i=order.index(m.group(1))), todo[i])
                expected = sorted(order.index(n) for n in MARK.findall(todo[i]))
                if sorted(int(k) for k in re.findall(STYLE_FIND[style], styled)) != expected:
                    # The text has something like this style's placeholder, or a digit right
                    # after one (ZQ0 + 5 reads as ZQ05): try the next style.
                    retry.append(i)
                    continue
                tried.append(i)
                local.append(order)
                batch.append(styled)
            tokens = [self.sp.encode(s, out_type=str) for s in batch]
            results = self.translator.translate_batch(
                tokens, beam_size=2, max_batch_size=32, batch_type="examples",
                max_decoding_length=256, repetition_penalty=1.1,
            )
            for i, source, order, result in zip(tried, batch, local, results):
                out = "".join(result.hypotheses[0]).replace("\u2581", " ")
                out = re.sub(r"\s+", " ", out).strip()
                want = sorted(int(k) for k in re.findall(STYLE_FIND[style], source))
                found = sorted(int(k) for k in re.findall(STYLE_FIND[style], out))
                if self._usable(source, out) and found == want:
                    done[i] = re.sub(STYLE_FIND[style], lambda m, order=order: f"\ue000{order[int(m.group(1))]}\ue001", out)
                else:
                    retry.append(i)
            pending = retry
        return done

    def texts(self, texts: list[str]) -> list[str | None]:
        """Translate masked texts, sentence by sentence."""
        pieces: list[list[str]] = [SENTENCE_END.split(t.strip()) for t in texts]
        todo = sorted({s for p in pieces for s in p if LETTER.search(MARK.sub("", s))}, key=len)
        translated = dict(zip(todo, self.sentences(todo)))
        joiner = "" if self.locale in NO_SPACES else " "
        out: list[str | None] = []
        for p in pieces:
            parts = [translated.get(s, s) for s in p]
            out.append(None if any(x is None for x in parts) else joiner.join(parts))
        return out


def main(argv: list[str]) -> int:
    if len(argv) != 5:
        print(__doc__, file=sys.stderr)
        return 2
    model_dir, locale, source, target = pathlib.Path(argv[1]), argv[2], pathlib.Path(argv[3]), pathlib.Path(argv[4])
    names = kept_names(pathlib.Path(__file__).resolve().parent.parent / "locales")
    rows = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]
    engine = Engine(model_dir, locale)
    started = time.time()

    copied, work = [], []
    for row in rows:
        if row["id"] in KEEP_ENGLISH:
            continue
        if is_code(row["id"]):
            copied.append({**row, "str": row["id"]})
            continue
        masked = Masked(names)
        outer = masked.mask(row["id"])
        if not LETTER.search(MARK.sub("", outer)) and not any(isinstance(i, tuple) for i in masked.items):
            copied.append({**row, "str": row["id"]})
            continue
        work.append((row, masked, outer))

    segments = [s for _, masked, outer in work for s in masked.segments(outer)]
    translated = iter(engine.texts(segments))
    finished, failed = [], 0
    for row, masked, outer in work:
        parts = [next(translated) for _ in masked.segments(outer)]
        if any(p is None for p in parts):
            failed += 1
            continue
        finished.append({**row, "str": masked.restore(outer, parts).strip()})

    with target.open("w", encoding="utf-8") as f:
        for row in copied + finished:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(
        f"{locale}: {len(finished)} translated, {len(copied)} copied as code, {failed} left out "
        f"(placeholders not kept), {time.time() - started:.0f}s"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
