# Flowie App MCP server

`com.get-flowie/app` · `https://back.p2p-flowie.com/agent-hub/mcp`

The Flowie app as an MCP server: what Flowie's in-app AI agent can do, from any AI assistant. It **acts as you**, the signed-in user, with exactly your Flowie permissions.

## What you can do

- **Send invoices**: create customer invoices, credit notes and orders (`create_transaction_document` computes every amount), compliant in 150 countries through Sovos, then follow them to payment.
- **Procure-to-pay**: purchase requests, approvals and refusals, purchase orders, invoice-to-PO matching, payments, budgets.
- **Suppliers (SRM)**: partners and contacts, onboarding forms, IBAN validation, spend concentration and off-contract spend.
- **Operations**: tasks, flows (workflows), inbox, documents, custom fields, tags, reports (AI dashboards), organization settings.

Start with `list_my_organizations`; every tool takes an optional `organization_id`.

## Connect

```bash
claude mcp add --transport http flowie-app https://back.p2p-flowie.com/agent-hub/mcp
```

VS Code `.vscode/mcp.json`:

```json
{ "servers": { "flowie-app": { "type": "http", "url": "https://back.p2p-flowie.com/agent-hub/mcp" } } }
```

Claude.ai / Claude Desktop: Settings → Connectors → Add custom connector → paste the URL → Connect.

## Sign-in

OAuth only (no API key). The client discovers everything from the `401` challenge: RFC 9728 protected-resource metadata, RFC 8414 authorization-server metadata, RFC 7591 dynamic client registration, authorization code + PKCE S256. You sign in with your normal Flowie login (SSO and Google work). Access tokens last 24 hours and are refreshed automatically.

## Limits

60 JSON-RPC requests per minute per user; over it the server answers `429` with `Retry-After`. For high volume, use the [Exchange API server](../exchange/).

Staging: `https://back.flowie.ink/agent-hub/mcp`. Full docs: <https://docs.get-flowie.com/mcp.md>
