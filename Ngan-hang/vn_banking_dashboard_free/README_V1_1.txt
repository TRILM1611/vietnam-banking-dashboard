MINHTRIINVEST – VIETNAM BANKING DASHBOARD V1.1

New in V1.1:
- FastAPI backend supports SQLite locally and PostgreSQL/Supabase in hosting.
- Normalized bank, observation, source registry and ingestion-run tables.
- CSV import APIs for bank registry and financial observations.
- Dashboard records endpoint and browser-side API connection control.
- Browser control to push CSV to server; write key is prompted and not stored.
- Optional SSI FastConnect Data securities-master adapter (requires credentials).
- Render Blueprint, Vercel static config, Supabase schema and deployment guide.

Important: no vendor financial-statement feed is active until provider credentials and data rights are supplied. SSI connector provides securities master only, not bank fundamentals. Demo data in the frontend remains illustrative until replaced by verified data.

See DEPLOYMENT_V1_1.md.
