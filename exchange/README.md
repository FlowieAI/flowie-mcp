# Flowie Exchange API MCP server

`com.get-flowie/exchange` · `https://back.p2p-flowie.com/exchange/mcp`

One API to **send and receive compliant e-invoices in 150 countries through Sovos**, from any ERP or system. Every Flowie Exchange API operation is a tool.

## What you can do

- **Send** invoices and credit notes (`send_document`) as Flowie JSON, UBL or CII; Flowie delivers them in the format and network each country requires.
- **Receive** and download incoming e-invoices.
- **Validate** documents before sending, and **track** their lifecycle statuses.
- Look up companies and partners, and the Peppol / French PPF directory.

## Connect

Sign in (OAuth):

```bash
claude mcp add --transport http flowie-api https://back.p2p-flowie.com/exchange/mcp
```

Or with an API key, for an integration with no person in the loop:

```bash
claude mcp add --transport http flowie-api https://back.p2p-flowie.com/exchange/mcp \
  --header "Authorization: Bearer flw_live_..."
```

VS Code `.vscode/mcp.json`:

```json
{ "servers": { "flowie-api": { "type": "http", "url": "https://back.p2p-flowie.com/exchange/mcp" } } }
```

`flw_live_…` keys work on production, `flw_test_…` keys on staging (`https://back.flowie.ink/exchange/mcp`). A sandbox key needs no signup: `POST https://back.flowie.ink/exchange/v1/sandbox/bootstrap`.

## Limits

Each `tools/call` counts as one Exchange API request against your plan's quota (120 to 2,400 requests per minute); over it, `429` with `Retry-After`.

Full docs: <https://docs.get-flowie.com/mcp.md> · Authentication: <https://docs.get-flowie.com/auth.md>
