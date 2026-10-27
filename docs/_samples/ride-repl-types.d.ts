// Types for the part of @decentralchain/ride-repl that ride-repl.ts uses: the
// package ships its Scala.js build without TypeScript declarations.
declare module '@decentralchain/ride-repl' {
  export class NodeConnectionSettings {
    constructor(url: string, chainId: number, address: string);
  }
  export interface ReplSession {
    evaluate(expression: string): Promise<{ result?: string; error?: string }>;
    info(name: string): string;
    totalInfo(): string;
    clear(): void;
    reconfigure(settings: NodeConnectionSettings): ReplSession;
  }
  export function repl(settings?: NodeConnectionSettings): ReplSession;
}

// Host functions the REPL calls as globals: hashing, and HTTP GET for chain state.
declare var blake2b256: (message: ArrayBuffer) => ArrayBuffer;
declare var keccak256: (message: ArrayBuffer) => ArrayBuffer;
declare var sha256: (message: ArrayBuffer) => ArrayBuffer;
declare var httpGet: (request: { url: string }) => Promise<{ status: number; body: string }>;
