// Illustrates: docs/04_building-apps/07_smart-contracts-overview.md, "Compile a Script"
// The other dApp, smart account and smart asset samples import compileRide from here.

// Compiles Ride source with a node's compiler and returns the base64 script that
// setScript(), setAssetScript() and issue() take.
export async function compileRide(source: string, nodeUrl: string): Promise<string> {
  const response = await fetch(`${nodeUrl}/utils/script/compileCode`, {
    method: 'POST',
    headers: { 'Content-Type': 'text/plain' },
    body: source,
  });
  const text = await response.text();
  let result;
  try {
    result = JSON.parse(text);
  } catch {
    throw new Error(`Ride compilation failed: HTTP ${response.status} from ${nodeUrl}: ${text.slice(0, 200)}`);
  }
  if (!response.ok || typeof result.script !== 'string') {
    throw new Error(`Ride compilation failed: ${result.message ?? text}`);
  }
  console.log(`Compiled: complexity ${result.complexity}, extra fee ${result.extraFee}`);
  return result.script; // "base64:..."
}
