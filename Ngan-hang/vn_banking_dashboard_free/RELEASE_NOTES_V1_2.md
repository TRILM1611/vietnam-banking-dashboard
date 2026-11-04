# Vietnam Banking Dashboard V1.2 — implementation notes

## Included in this branch

- Demo rows are hidden by default. Viewers must explicitly enable **Hiển thị dữ liệu minh họa** to see sample rows.
- Reporting-period options are generated from available records instead of a fixed four-quarter list. Supported sort formats include Q1–Q4/YYYY, H1–H2/YYYY and FY/YYYY.
- When an API sync completes, existing local/manual rows are preserved; API records update only matching non-demo ticker + period rows.
- Data status is distinguished as demo, verified, or not verified in the overview and data log.
- Null values are no longer silently excluded from averages; legitimate zero values remain valid.
- P/B and P/E summary KPIs display valuation multiples with an x suffix, not a percent sign. P/E is shown only for positive EPS.
- Ranking skips records missing required inputs rather than treating missing values as zero.
- API observation writes validate ticker format, reporting-period format, value range and verification status, and require the bank to exist in the registry.
- CSV imports return row-level skip reasons for unknown metrics, invalid values and registry/validation errors.

## Important data policy

This branch does not add a live bank-fundamentals data provider. A row marked verified should only be set after the source document, period, unit, consolidation basis and calculation method have been checked. Demo rows are illustrative and must not be used for investment decisions.

## Deployment

This is a feature branch only. Review and merge the pull request before deploying. The existing public website and production branch are unchanged by this branch until it is merged and the hosting provider redeploys.
