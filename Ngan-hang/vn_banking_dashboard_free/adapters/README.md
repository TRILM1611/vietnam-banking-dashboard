# Data adapter policy

## Official / primary sources
- Bank annual reports and quarterly financial statements: capture the original PDF/HTML URL, publication date, consolidated/standalone basis and reporting period.
- State Bank of Vietnam and exchange disclosures: ingest only fields actually published. Record the source and retrieval timestamp.
- Use manual CSV import as the initial controlled ingestion path. The API expects `DATA_IMPORT_TEMPLATE.csv` columns.

## SSI FastConnect Data
The optional `/market/ssi/securities` endpoint retrieves the exchange security master when SSI API Key and API Secret are configured as backend environment variables. It is a market-data connector, not a source for bank fundamentals. See SSI Developer Portal: https://developers.ssi.com.vn/docs/api-reference

## Commercial fundamentals providers
Implement a provider-specific adapter only after obtaining credentials, a field dictionary, update frequency, historical coverage and redistribution rights. Do not scrape authenticated or paywalled endpoints. Normalize vendor fields to `METRIC_CATALOG` in `backend/main.py` and preserve the original vendor field in an audit note.

## Validation rules
- Never mix consolidated and standalone financial statements.
- Distinguish quarter-only, YTD and TTM values.
- Keep missing values null; zero is a real numeric value, not a missing-value marker.
- Store ratios in percentage points (e.g. 18.4 means 18.4%), not decimals.
- Validate units and period before marking a record `verified`.
