---
name: get-started
description: Start using Flowie in ChatGPT. Use right after the Flowie plugin is installed, or when the user asks what Flowie can do, which company Flowie acts in, or how to send their first compliant invoice.
---

# Get started with Flowie

Flowie is the AI-native order-to-cash and procure-to-pay platform. Its key job is sending invoices: it builds customer invoices and credit notes that are compliant in 150 countries through Sovos, sends them, and follows them to payment. It also runs intake-to-pay: purchase requests, approvals, purchase orders, invoice matching, payments, budgets and supplier relationships.

Flowie acts as the signed-in user, with exactly their Flowie permissions.

## First steps

1. Call `list_my_organizations` to see the companies the user belongs to. If there are several, ask which one to work in and pass its id as `organization_id` on every later call. If there are none, tell the user to create or join a company in the Flowie app first.
2. Offer three things the user can do right away:
   - Send an invoice: "Invoice Acme for 12 hours of consulting at 150 euros." Use `create_transaction_document`; it computes every amount and tax. Confirm the customer, lines and totals with the user before creating it.
   - Follow up: "Which customer invoices are overdue?" Use `search_transaction_documents`.
   - Approve: "What is waiting for my approval?" Use `list_objects_pending_approval`, then `approve_object` or `refuse_object` only when the user says so.

## Rules

- Before any write (creating, approving, refusing, deleting), restate what will happen and wait for the user's confirmation.
- Work one object per call. The server allows 60 calls a minute per user; on a `429`, wait the `Retry-After` seconds. For bulk sending or an integration, point the user to the Flowie Exchange API (https://docs.get-flowie.com/mcp.md).
- When a tool returns an error, read the backend's message: it names the field to fix.
