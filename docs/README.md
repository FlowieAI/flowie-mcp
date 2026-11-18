# Flowie Developer Docs MCP server

`com.get-flowie/docs` · `https://docs.get-flowie.com/mcp`

Search and read the Flowie Exchange API documentation and its OpenAPI contract from your AI assistant or coding agent. **No sign-in needed.**

Use it while building an integration: find the right endpoint, read a request schema, check an error code or an e-invoicing guide.

```bash
claude mcp add --transport http flowie-docs https://docs.get-flowie.com/mcp
```

VS Code `.vscode/mcp.json`:

```json
{ "servers": { "flowie-docs": { "type": "http", "url": "https://docs.get-flowie.com/mcp" } } }
```

Docs: <https://docs.get-flowie.com/developers/> · LLM index: <https://docs.get-flowie.com/llms.txt>
