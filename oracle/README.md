# Flowie for Oracle Fusion AI Agent Studio

Oracle Fusion customers connect Flowie as an MCP tool in AI Agent Studio (Fusion 26A and later). Agent Studio calls Flowie's Exchange API MCP server with OAuth 2.0 client credentials.

## Customer setup

1. An admin of the Flowie organization creates a machine client with `POST /v1/oauth/clients` and picks the role it gets (read-only by default). Keep the client id and the secret: the secret is shown once.
2. In Oracle Fusion, open **AI Agent Studio**, then **Tools**, then add a tool of type **MCP**:

   | Field | Value |
   |---|---|
   | Server URL | `https://back.p2p-flowie.com/exchange/mcp` |
   | Transport | Streamable HTTP |
   | Credential type | Client Credentials |
   | Token URL | `https://back.p2p-flowie.com/exchange/v1/oauth/token` |
   | Client id / secret | From step 1 |
   | Scope | Leave empty |

3. Add the Flowie tools to an agent (for example, a payables or billing agent) and test with "List the last invoices received".

Create one client per Flowie organization. The token endpoint adds the Flowie API audience, so Oracle needs no `audience` field.

Full guide: https://docs.get-flowie.com/build-with-ai/#agentforce-oracle

## Oracle AI Agent Marketplace

Listing a Flowie agent template on Oracle's AI Agent Marketplace requires Oracle PartnerNetwork membership and Oracle's 21-point readiness review. Flowie is not a member yet. Do this only once a Fusion customer needs it.

## Verified

26/11/2026 on staging, with the same flow Agent Studio uses: token, `tools/list` (125 tools), a read call, and refusal after the client was revoked. Production release: exchange-api 0.1.0-vf24ff66c.
