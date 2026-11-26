# Flowie for Salesforce Agentforce (AgentExchange listing)

Listing type: **ISV MCP Tool Action** on AgentExchange. Agentforce calls Flowie's Exchange API MCP server with OAuth 2.0 client credentials.

## Listing content

**Name:** Flowie: e-invoicing in 150 countries

**Tagline (short description):** Send compliant e-invoices in 150 countries from Agentforce, through Sovos, and follow them to payment.

**Description:**

Flowie gives Agentforce agents the tools to send, receive and track electronic invoices worldwide. Flowie is part of the Sovos group: invoices go out in the format and on the network each country requires (Peppol, clearance and real-time reporting regimes), across 150 countries.

What an agent can do with Flowie:
- Build an invoice or credit note from a Salesforce opportunity or order, validate it against the country's rules, and send it.
- Check that a customer can receive e-invoices and find its identifiers (Peppol ID, SIREN, VAT number).
- Track delivery and the invoice lifecycle (received, approved, refused, paid).
- List incoming supplier invoices and their status.
- Record payments and see what is overdue.

Flowie acts for one organization, with the role its admin chose when creating the connection, read-only by default.

**Categories:** Finance, Compliance, Accounting

**Industries:** All. Strongest for companies invoicing in countries with e-invoicing mandates (France 2026, Belgium, Poland, Germany, Spain, Italy, Latin America).

**Pricing:** The listing is free. A Flowie subscription is required.

**Support:** https://get-flowie.com/contact
**Privacy policy:** https://get-flowie.com/legal/privacy
**Terms:** https://get-flowie.com/legal/terms
**Security:** https://get-flowie.com/trust (ISO/IEC 27001 certified, Sovos group; hosted on Google Cloud, Paris region)

## Technical details for the listing

| Field | Value |
|---|---|
| MCP server URL | `https://back.p2p-flowie.com/exchange/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth 2.0 client credentials |
| Token URL | `https://back.p2p-flowie.com/exchange/v1/oauth/token` |
| Client id / secret | Created by the customer's Flowie admin with `POST /v1/oauth/clients` |
| Scope | none |
| Tools | 125 (send, validate, directory, documents, lifecycle, payments, companies) |

Customer setup guide: https://docs.get-flowie.com/build-with-ai/#agentforce-oracle

## Verified

- 26/11/2026, staging: machine client created, token issued by the token URL above, `tools/list` returned 125 tools, `tools/call list_documents` returned data, and the token was refused after the client was revoked.
- Production release: exchange-api 0.1.0-vf24ff66c.

## Steps to publish (partner account holder: Rémi)

1. Log in to the Salesforce Partner Community (Flowie's ISV account, opened July 2023).
2. In the Partner Console, create a listing of type **ISV MCP Tool Action** and paste the content above.
3. Link the MCP server (Agentforce MCP Server Registration) using the technical details above.
4. Submit for the business, technology and security reviews. For the security review, point to https://get-flowie.com/trust and the ISO/IEC 27001 certificate (Sovos group).
5. Recommended before the security review: test in a free Agentforce Developer Edition org (Setup, Agentforce Registry, add a third-party MCP server).
