# Submission content (Microsoft MCP server certification)

Copy-ready answers for the intake form and the Partner Center offer. Credentials are never written here: this repository is public. Tracking: RAC-14374.

## 1. Intake form

Form: "MCP server certification intake form", linked from https://learn.microsoft.com/microsoft-copilot-studio/mcp-certification. Microsoft emails the next steps; during the preview it processes a limited number of submissions.

| Question | Answer |
|---|---|
| Contact | Yann Ravel-Sibillot, Flowie (a Sovos company) |
| Company / publisher | Sovos, for Flowie SAS (Flowie is part of Sovos) |
| Partner Center ID (Seller ID) | Sovos's ID, from its Partner Center admin |
| Legal vetting completed | Yes |
| Package ready | Yes, `dist/flowie-m365.zip` built by `build.py` |
| MCP server URL | https://back.p2p-flowie.com/agent-hub/mcp |
| Authentication | OAuth 2.0 authorization code with a confidential client (no PKCE), refresh token supported, configuration in Azure Key Vault |
| Do you own the endpoint? | Yes, Flowie operates it |
| Why now | Flowie customers on Microsoft Dynamics 365 ask to work in Flowie from Copilot: create and send compliant invoices, follow them to payment, and approve supplier invoices and purchase orders without leaving Microsoft 365. |
| Microsoft contact | Any Sovos business-development contact at Microsoft |

## 2. Partner Center offer

Offer type: **Apps and Agents for M365 and Copilot**. Package: `dist/flowie-m365.zip`.

### Listing

- **Name**: Flowie
- **Short description** (from `manifest.json`): Send compliant invoices in 150 countries, plus order-to-cash and procure-to-pay.
- **Long description**: `manifest.json` `description.full`, or `intro.md` up to "Rate limits".
- **Categories**: Finance; Productivity
- **Industries**: Professional services; Retail and consumer goods; Manufacturing
- **Website**: https://get-flowie.com
- **Support**: https://get-flowie.com/contact
- **Privacy policy**: https://get-flowie.com/legal/privacy
- **Terms of use**: https://get-flowie.com/legal/terms
- **Documentation**: https://docs.get-flowie.com/build-with-ai/
- **Screenshots** (PNG, 1366x768): take them during the Microsoft 365 test (Copilot answering "Show my 5 latest invoices", the Flowie sign-in page, a spend overview report).

### Notes for certification (test notes)

Paste, then add the reviewer account's email and password from the tokens file in the Partner Center field itself:

```
Flowie is an order-to-cash and procure-to-pay platform. This connector is Flowie's
app MCP server (https://back.p2p-flowie.com/agent-hub/mcp). Copilot acts as the
signed-in Flowie user, with that user's permissions.

Test account (demo company DUNDER MIFFLIN, no MFA):
  email:    <reviewer email>
  password: <reviewer password>

Steps:
1. Add the Flowie connector and run any prompt below. Copilot opens the Flowie
   sign-in page: sign in with the test account, then click Approve.
2. Prompts:
   - "Which Flowie companies can I access?"
   - "Show my 5 latest invoices."
   - "Who are our suppliers?"
   - "Build a spend overview report."
   - "What is waiting for my approval?"
3. Tools that create or change data act only on an explicit request and are
   annotated (readOnlyHint / destructiveHint). The demo company holds test data
   only; creating an invoice there is safe.

Sign-in: OAuth 2.0 authorization code, confidential client, refresh token
supported (access token 24 h). Configuration in Azure Key Vault flowie-mcp-kv.

Video walkthrough: https://drive.google.com/file/d/1pimPmtEj_-WLNO0OtL8CbMDlgjodpkvB/view
Support: https://get-flowie.com/contact
```

## 3. Review

Microsoft runs automated validation (structure, schema, metadata, baseline policy), then a functional and safety review (endpoint behaviour, sign-in, security, compliance, responsible AI). Answer what they flag on the RAC-14374 thread.

Known risk: the server exposes 254 tools. If Microsoft asks for fewer, serve the 54 lead tools (`LEAD_TOOLS` in agents-hub) to Microsoft clients by User-Agent, as for ChatGPT, then rebuild with `--refresh-tools`.
