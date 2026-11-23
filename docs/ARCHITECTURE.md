# Architecture overview

## Production design (descriptive, not included in this public demo)

- **Client:** Responsive browser application with purpose-specific creation forms, personal and household views, and mobile layouts.
- **Application:** Python API service (FastAPI), with sessions, password hashing, CSRF checks, role-based record authorization, audit history, and user-confirmed actions.
- **Data:** Local SQLite database. Household records have types, owner identities, visibility, and versioned updates. The database and backups are intentionally excluded from this repository.
- **Operation:** Runs as a private local background service with a separately managed HTTPS reverse proxy in the real installation. No network, service, or TLS configuration is distributed here.

This document describes product-level decisions and makes **no claim that the hosted demo enforces real permissions**. A visual menu that hides a finance screen does not enforce a security boundary; that belongs to the backend and must be tested there.

## Demonstration design

`index.html` is a self-contained frontend. It includes the style layer, browser UI code, and fictional in-memory mock responses. It intercepts its own `/api/` calls and intentionally rejects external requests. No data persists on reload, and it does not talk to the real household service.

## Product invariants

- Do not silently invent due dates, stock quantities, actors, attendance, payments, or completed work.
- A shopping-list item does not mean it was purchased.
- A planned meal does not mean it was cooked.
- Low/out inventory can suggest grocery-list additions, with duplicate checks and clear confirmation points.
- Assignments are proposed before being accepted; private data must be checked at the server, not just hidden in the browser.
- A reported bill payment is not a verified bank transaction.

## Working on the demo

Open `index.html` locally in a modern browser. No dependencies. Synthetic people and records are defined in a mock section near the beginning of the file. Edit the demo without importing production data or configuration.
