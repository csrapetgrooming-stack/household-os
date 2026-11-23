# Household OS

**A local-first family dashboard that turns household coordination into something more manageable.**

This repository is a **sanitized, interactive showcase** of the Household OS interface. The underlying personal installation is a separate, authenticated FastAPI/SQLite household application. **Only the fictional-data frontend demonstration is published here.**

## Try the demo

[**Open the interactive demo**](index.html) by downloading this repository and opening `index.html` in a browser. No installation, login, API key, internet connection, or backend server required.

The demo starts as **Alex**, a fictional household administrator. Use the **View as** selector along the top to switch to Morgan or Riley. Changes are simulated in browser memory and disappear on reload. **Never enter real household information.**

### What it demonstrates

- A mobile-minded household dashboard with **My Tasks** and **Household** views.
- Quick Capture, tasks and voluntary task assignments.
- Projects, recurring chores, shared groceries, pantry/refrigerator/freezer inventory.
- Meal ideas, family calendar, birthdays, and house maintenance notes.
- Purpose-specific forms, optional details, clear save messages, and uncertainty-aware language.
- Demonstration finance views and per-member visibility differences. These are **UI illustrations, not security tests**.

### What it does *not* do

This public showcase is **not** the live Household OS service. There is no server, database, real authentication, persistent storage, network access, or financial-data integration. Its local mock endpoints illustrate interactions only. It must **not** be used to store private or financial information, exposed as a production web service, or treated as a deployable secure backend.

### Why local-first?

The real system was designed around a simple principle: shared household data should remain under household control. Financial visibility is separated by account, task assignments require acceptance, unknown dates stay unknown, and planning something does not claim that it happened.

### Current development

The family installation is in active iteration. This showcase reflects the **Household OS 2.1 UX Pass A** interface, rather than claiming every planned feature is finished. A family recipe/meal-voting flow and ingredient-aware meal planning are planned but **not included** in this demo.

See [Architecture](docs/ARCHITECTURE.md) and [Privacy & publishing](docs/PRIVACY.md).

---

**Project:** Household OS · **Source:** interactive demonstration with deliberately fictional data · **License:** not yet selected. Public viewing does not grant a license to reuse or redistribute this code.
