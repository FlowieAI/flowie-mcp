# Flowie

Flowie is an order-to-cash and procure-to-pay platform. Its key job is sending invoices: it creates customer invoices and credit notes and, for companies set up for e-invoicing, sends them through Sovos in the format each country requires (150 countries, Peppol, clearance and real-time reporting regimes included). It also receives supplier invoices and runs purchase requests, approvals, purchase orders, invoice matching, payments, budgets and supplier relationships.

This MCP server lets Microsoft Copilot work in Flowie as the signed-in user, with exactly that user's Flowie permissions, in the companies they belong to.

## Prerequisites

- A Flowie account (https://app.flowie.me). Sign-in supports SSO and Google.
- Your Microsoft 365 admin may need to allow the Flowie connector for your organization.

## How to get credentials

There is no API key to create. When you first use a Flowie tool, Copilot opens the Flowie sign-in page. Sign in, pick the company Copilot should act in, and approve.

## Supported operations

- **Invoicing (order-to-cash)**: create customer invoices, credit notes and orders with amounts and tax computed; send them through e-invoicing where it is set up; follow them to payment (overdue invoices, payment status, lifecycle history).
- **Approvals**: list what waits for your approval; approve or refuse supplier invoices, purchase requests and purchase orders when you ask.
- **Purchasing (procure-to-pay)**: create purchase requests and purchase orders, match invoices to orders, read catalogs and budgets.
- **Suppliers and customers**: partnerships, contacts, onboarding forms, IBAN checks.
- **Analytics and reports**: spend analytics, supplier concentration, spend without a purchase order, AI reports with a link to the report in Flowie.
- **Organization**: list your companies, members, tags, custom fields, tasks and documents.

Every tool declares whether it only reads, or creates or changes data. Tools that change data act only on an explicit request.

## Example prompts

- "Which Flowie companies can I access?"
- "Show my 5 latest invoices."
- "Invoice Acme for 12 hours of consulting at 150 euros."
- "What is waiting for my approval?"
- "Who are our suppliers?"
- "What did we spend without a purchase order this quarter, in EUR?"
- "Build a spend overview report from invoices, orders and suppliers."

## Rate limits

60 requests a minute per user. High-volume integrations use the Flowie Exchange API (https://back.p2p-flowie.com/exchange/mcp), 120 to 2,400 requests a minute by plan.

## Known issues and limitations

- When you belong to several Flowie companies, name the company in your request or ask Copilot to list your companies first.
- Sending an e-invoice requires the company to be set up for e-invoicing in Flowie.
- Tools follow your Flowie permissions: an operation your role cannot do in the Flowie app fails here too.

## Support

- Documentation: https://docs.get-flowie.com/build-with-ai/
- Support: https://get-flowie.com/contact
- Privacy: https://get-flowie.com/legal/privacy
- Terms: https://get-flowie.com/legal/terms
