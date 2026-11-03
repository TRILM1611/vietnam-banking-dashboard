# Vietnam Banking Dashboard – V1.0 Foundation

## Included
- Browser dashboard (`index.html`) with localStorage persistence for manual/imported records.
- FastAPI + SQLite starter API (`backend/`) for a bank registry and normalized metric observations.
- Data dictionary and bank-registry CSV template.

## Run frontend
Open `index.html` in a modern browser. Export CSV regularly. Browser storage is local to that browser/device and is not a shared database.

## Run API locally
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate ; macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
# Set BANKING_WRITE_KEY to a long random secret before exposing the API
uvicorn main:app --reload
```
Open `http://127.0.0.1:8000/docs` for API documentation and `/health` for health check.

## Production checklist
1. Use managed PostgreSQL rather than SQLite for multi-user production.
2. Put API behind HTTPS; set `BANKING_WRITE_KEY`, strict `CORS_ORIGINS`, backups and rate limits.
3. Never put provider API secrets in frontend JavaScript. Build server-side adapters only after obtaining lawful API credentials and checking redistribution rights.
4. Add authentication/roles, audit log, validation, monitoring and scheduled jobs before production.
5. Backend starter is not yet wired into the static frontend. No hosted deployment or provider data feed is active.

## Data controls
Each observation should retain ticker, reporting period, metric, unit, consolidated/standalone basis, source name/URL, publication date and verification status. Do not silently mix consolidated and standalone statements, quarter-only and TTM values, or regulatory and analyst-defined ratios. Missing values remain null.

## Automatic ingestion
No live provider is connected in this package. Integration requires a chosen provider, credentials, entitlement and field mapping. Official bank reports and regulator/exchange disclosures should be retained as evidence.
