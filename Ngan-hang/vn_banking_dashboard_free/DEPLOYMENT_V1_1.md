# Deploy Vietnam Banking Dashboard V1.1

## Recommended architecture
- Frontend: Vercel static site (root directory `/`, output `.`).
- API: Render Web Service from this repository, root directory `backend`, Docker runtime.
- Database: Supabase PostgreSQL. Backend uses the server-side connection string; do not expose it to browser JavaScript.

## 1. Supabase
1. Create a Supabase project.
2. Open SQL Editor and run `supabase/schema.sql`.
3. In Project Settings > Database, copy the Session Pooler connection string (or a supported connection URI). Replace it with SQLAlchemy form: `postgresql+psycopg://...`.
4. Keep the database password private. Do not use the `service_role` key in the browser.

## 2. Deploy API to Render
1. Push this folder to a private GitHub repository.
2. In Render, choose New > Blueprint and select the repository (or create a Docker Web Service with root directory `backend`).
3. Set `DATABASE_URL` to the Supabase PostgreSQL URI.
4. Set `BANKING_WRITE_KEY` to a random secret of at least 32 characters.
5. Set `CORS_ORIGINS` to the exact Vercel production URL, e.g. `https://minhtri-banking.vercel.app` (comma-separated if needed).
6. Optional: set `SSI_API_KEY` and `SSI_API_SECRET` only after obtaining SSI credentials and confirming entitlement.
7. Deploy; verify `https://YOUR-API.onrender.com/health` returns `status: ok`.

## 3. Deploy frontend to Vercel
1. Import the same GitHub repository into Vercel.
2. Framework Preset: Other; Root Directory: `.`; Build Command: leave empty; Output Directory: `.`.
3. Deploy. The site serves `index.html`.
4. Open the website and click `Kết nối API`; enter the Render API URL. The browser calls the read-only `/health` and `/dashboard/records` endpoints.
5. If connection fails, check exact CORS origin and API health endpoint.

## 4. Import financial data
1. Prepare a CSV using `DATA_IMPORT_TEMPLATE.csv`.
2. Obtain the API write key from the Render environment settings. Keep it private.
3. Import using `POST /import/csv` with multipart field `file` and header `X-API-Key`. Example:

```bash
curl -X POST 'https://YOUR-API.onrender.com/import/csv' \
  -H 'X-API-Key: YOUR_WRITE_KEY' \
  -F 'file=@DATA_IMPORT_TEMPLATE.csv'
```

5. Add the bank master record with `POST /banks` before inserting observations; the Supabase schema enforces the bank foreign key.
6. Check `/observations`, `/dashboard/records`, `/sources/status` and `/docs`.

## 5. SSI market-data connector
- Register/activate FastConnect Data and obtain the V3 API Key + API Secret.
- Put credentials in Render environment variables, never in Vercel or HTML.
- Call `GET /market/ssi/securities?market=HOSE` (also HNX/UPCOM). This adapter uses the current V3 auth/token and data/securitiesByBoard endpoints, and retrieves the securities master only. Add separate market endpoints only after reviewing current SSI API specs and usage rights.

## Security / operations
- Keep API write key and database URI only in Render secrets.
- Restrict CORS to the production and preview domains actually used.
- Add authentication/user roles before multi-user private research data is exposed.
- Enable Supabase RLS; backend connects as trusted server. Do not grant anonymous write access.
- Back up database regularly. Supabase daily managed backups are plan-dependent; export free-tier data routinely.
- Free Render web services may sleep after inactivity; choose an always-on paid instance for routine production use.

## Current limitations
- No vendor financial-statement feed is active until provider credentials and data rights are supplied.
- SSI connector is optional and covers the securities master, not bank fundamentals.
- Full bank legal-entity registry must be verified against current State Bank of Vietnam licensing records; do not infer completeness from exchange ticker lists.
- Ranking outputs are screening aids, not investment recommendations.

## 6. Import the bank registry
Prepare a CSV from `BANK_REGISTRY_TEMPLATE.csv` and POST it to `/import/banks-csv` with `X-API-Key`. Use `listing_status` values `listed` or `unlisted`; keep ownership in `ownership_type` (e.g. `state_owned`, `private`, `foreign_owned`). This is an editable import template, not a complete official bank list.
