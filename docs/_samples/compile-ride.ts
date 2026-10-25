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
  const result = await response.json();
  if (!response.ok) {
    throw new Error(`Ride compilation failed: ${result.message}`);
  }
  console.log(`Compiled: complexity ${result.complexity}, extra fee ${result.extraFee}`);
  return result.script; // "base64:..."
}
