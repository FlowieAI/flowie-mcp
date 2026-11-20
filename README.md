# Flowie MCP servers

Flowie is the AI-native order-to-cash and procure-to-pay platform. Its key job is **sending invoices**: build and send customer invoices and credit notes that are compliant in **150 countries through Sovos** (Peppol, clearance and real-time reporting regimes included), then follow them to payment. It also receives supplier invoices and runs everything from intake to pay: purchase requests, approvals, purchase orders, matching, payments, budgets, supplier onboarding (SRM), workflows and spend analytics.

Flowie runs four remote MCP servers (Streamable HTTP). There is nothing to install: add the URL to your client and sign in.

| Server | Registry name | URL | For |
|---|---|---|---|
| [Flowie App](app/) | `com.get-flowie/app` | `https://back.p2p-flowie.com/agent-hub/mcp` | A person using Flowie from an AI assistant. Acts as you. |
| [Flowie Exchange API](exchange/) | `com.get-flowie/exchange` | `https://back.p2p-flowie.com/exchange/mcp` | Sending and receiving e-invoices, integrations, high volume. |
| [Flowie Developer Docs](docs/) | `com.get-flowie/docs` | `https://docs.get-flowie.com/mcp` | Searching the API docs and OpenAPI contract. No sign-in. |
| [Flowie](website/) | `com.get-flowie/website` | `https://get-flowie.com/mcp` | Questions about Flowie, its product and coverage. No sign-in. |

This repository holds the descriptions of these servers for MCP registries and galleries. The servers themselves are hosted by Flowie; their source code is not here.

## Quick start

**Claude Code**

```bash
claude mcp add --transport http flowie-app https://back.p2p-flowie.com/agent-hub/mcp
claude mcp add --transport http flowie-api https://back.p2p-flowie.com/exchange/mcp
```

**VS Code (GitHub Copilot agent mode)**: `.vscode/mcp.json`

```json
{
  "servers": {
    "flowie-app": { "type": "http", "url": "https://back.p2p-flowie.com/agent-hub/mcp" },
    "flowie-api": { "type": "http", "url": "https://back.p2p-flowie.com/exchange/mcp" }
  }
}
```

**Cursor, Claude Desktop, ChatGPT and others**: add a remote / custom connector with the URL. Sign-in is standard MCP OAuth (protected-resource metadata, dynamic client registration, PKCE S256): no client ID, no secret, no API key needed.

Full, copy-ready configuration for every client: <https://docs.get-flowie.com/mcp.md>

## Microsoft 365 Copilot

The Microsoft 365 app package for MCP server certification (Copilot Studio, Microsoft Foundry, Microsoft 365 Copilot) is in [m365-copilot/](m365-copilot/).

## Environments

| | Production | Staging / sandbox |
|---|---|---|
| App | `https://back.p2p-flowie.com/agent-hub/mcp` | `https://back.flowie.ink/agent-hub/mcp` |
| Exchange API | `https://back.p2p-flowie.com/exchange/mcp` | `https://back.flowie.ink/exchange/mcp` |

## Links

- Website: <https://get-flowie.com>
- Developer docs: <https://docs.get-flowie.com>
- Security and trust: <https://get-flowie.com/trust>

Flowie SAS, Paris.
