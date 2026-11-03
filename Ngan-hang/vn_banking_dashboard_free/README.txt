VIETNAM BANKING DASHBOARD – MINHTRIINVEST (V1.0 FOUNDATION)

FRONTEND
- Open index.html in Chrome/Edge.
- Manually entered/imported data is persisted in browser localStorage.
- Export CSV regularly; browser data does not sync across devices.
- Built-in sample rows are illustrative only, not actual financial data.

BACKEND STARTER
- FastAPI + SQLite API is in backend/.
- See DEPLOYMENT.md for local setup and production checklist.
- Endpoints: GET /health, GET/POST /banks, GET/POST /observations.
- Write endpoints can be protected by BANKING_WRITE_KEY.
- Backend is not yet connected to frontend; no hosted deployment or provider feed is active.

DATA MODEL
- DATA_DICTIONARY.csv defines key fields, units and methodological cautions.
- BANK_REGISTRY_TEMPLATE.csv is for building a verified legal-entity universe.
- Store source, URL, period, consolidation basis and verification status for every metric.

IMPORTANT
- This package does not contain a verified complete list of all banks in Vietnam. Build the full registry from current State Bank of Vietnam records.
- No automatic data feed is active. Provider API integration requires credentials, permission and field mapping.
- Do not use demo data or unverified data for investment decisions.
