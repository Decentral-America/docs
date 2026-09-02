# Node Extensions

Extensions are optional modules a node operator can enable alongside the core {ref}`REST API <05_node-guide/01_node-rest-api:Node REST API>` for consumers that need direct access to binary data instead of JSON.

## gRPC Server

The node ships a `grpc-server` module (built alongside the core node in [node-scala](https://github.com/Decentral-America/node-scala/tree/master/grpc-server)) that exposes {ref}`blocks <02_decentralchain/10_binary-format:Block Binary Format>` and {ref}`transactions <02_decentralchain/10_binary-format:Transaction Binary Format>` directly in their protobuf-serialized binary format, rather than the JSON representation the REST API returns. This is the recommended way to consume chain data for a service that needs to process a large volume of blocks or transactions efficiently.

If you use your own node with the gRPC server enabled, you can send it a `SignedTransaction` object directly instead of composing a JSON transaction for the REST API's `POST /transactions/broadcast` method. See the [`protobuf-serialization`](https://github.com/Decentral-America/protobuf-serialization) package for building and parsing these binary structures from JavaScript/TypeScript.

Enabling and configuring the gRPC server is done through the node's own configuration file — see the `grpc-server` module in the node-scala repository for its current configuration options.
