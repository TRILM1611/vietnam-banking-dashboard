# Banking registry and data policy — V1.2

## 1. Registry scope

`BANK_REGISTRY_STARTER.csv` is a working starter list of 28 bank tickers to seed the dashboard's bank dimension. It is **not** a legally authoritative or guaranteed complete list of all Vietnamese credit institutions or securities currently trading.

- All rows are deliberately marked `needs_verification`.
- Exchange and trading-status fields are initial classifications for dashboard setup and must be checked against the latest HOSE/HNX/UPCoM issuer master before a production refresh.
- `official_url` is blank until an investor-relations or official issuer page is confirmed.
- Non-bank finance companies (for example EVF and TIN) are excluded from this commercial-bank universe.

## 2. Reference sources used for the starter list

1. KBSV Research, *Industry Report — Banking Sector*, appendix table of bank tickers, exchanges and institution names: https://www.kbsec.com.vn/pic/Service/KBSV_Banking_Sector_Eng.pdf
2. HNX/UPCoM official securities list: https://www.hnx.vn/vi-vn/cophieu-etfs/chung-khoan-uc.html
3. HNX official listed securities information: https://www.hnx.vn/co-phieu-etfs/chung-khoan-ny-thong-tin.html
4. VietnamFinance, 29 Dec 2025, summary of bank tickers listed on HOSE/HNX and KienlongBank's planned transfer to HOSE: https://vnfinance.vn/hose-sap-don-them-co-phieu-vua-va-them-loat-ngan-hang-ke-hoach-len-san-hose-nam-2026-70964.html
5. HNX/UPCoM new trading registrations (use to verify newly registered tickers such as PCB): https://hnx.vn/vi-vn/co-phieu-etfs/chung-khoan-uc-moi.html

These references help establish a seed universe, not the verification of every current status. Refresh against the official exchange issuer lists before treating the exchange fields as current.

## 3. Observation data rules

Every metric observation should have:
- ticker and reporting period;
- metric key and numeric value;
- unit;
- consolidation basis (`consolidated` or `separate`);
- source name and a direct source URL where available;
- publication date;
- verification status;
- a note describing calculation basis, annualization, accounting classification or any source-specific caveat.

### Verification statuses

- `source_only`: a source document or source record is attached, but the value has not been independently checked.
- `unverified`: imported or entered but source/definition has not been validated.
- `review_required`: inconsistent, incomplete or ambiguous; do not use in comparisons.
- `verified`: source, period, unit, consolidation basis and metric definition have all been checked.

A bank-period row is only returned as `verified` when every metric in that row is verified. The API also returns source, unit and verification status at the individual-metric level.

## 4. Reporting-period convention

- Quarter: `Q1/2026` ... `Q4/2026`
- Half-year: `H1/2026`, `H2/2026`
- Full year: `FY2025`

Do not treat a full-year flow metric as interchangeable with a quarter-only flow metric. For ratios such as NIM, ROE, ROA, CIR and cost of funds, note whether the value is quarterly annualized, TTM or full-year.

## 5. Critical banking metric definitions

| Metric | Standard working definition | Key control |
|---|---|---|
| Assets | Total assets at period end | Prefer consolidated financial statements |
| Loans | Customer loans at period end | Do not substitute system-wide credit |
| Deposits | Customer deposits at period end | Exclude interbank funding |
| CASA | Non-term customer deposits / customer deposits | Confirm source's CASA classification |
| Credit growth | Period-end loans / prior year-end loans - 1 | Distinguish YTD from YoY |
| NIM | Net interest income / average interest-earning assets | Record annualization and denominator |
| ROE | Net income / average equity | Record TTM, FY or annualized quarter |
| ROA | Net income / average assets | Record profit basis and annualization |
| CIR | Operating expenses / operating income | Align income/expense classification |
| NPL | Group 3–5 loans / customer loans | Record consolidation basis |
| Group 2 | Group 2 loans / customer loans | Not the same as NPL |
| LLR | Loan-loss reserves / NPL | Follow the bank's published definition |
| CAR | Capital adequacy ratio as disclosed | Record regulatory standard and solo/consolidated basis |
| LDR | Customer loans / customer deposits | Internal comparison only; not legal regulatory LDR |

## 6. Data import workflow

1. Import the bank registry.
2. Check every bank's legal name, ticker, exchange and official investor-relations page.
3. Import quarterly/annual observations with direct report URLs.
4. Keep source-only/unverified records out of verified investment comparisons.
5. Reconcile year-end and quarterly cumulative values before calculating TTM or annualized ratios.
6. Record every correction in the source note or ingestion log.

No real bank financial values are included in the starter registry. The starter file seeds the bank dimension only.


## 7. Five-bank pilot source register

The official investor-relations and financial-report entry points for the first ingestion pilot are tracked in `PILOT_SOURCE_REGISTER.csv` for VCB, BID, CTG, TCB and MBB.

The register records the official page URLs, the source types visible on those pages, the latest period observed during source review, and remaining extraction work. A page being confirmed does **not** mean that its financial observations have been extracted or verified. Exact PDF attachment URLs, publication dates, consolidation basis, units and metric definitions must be captured per observation before it can be marked `verified`.

Initial official source entry points reviewed:
- Vietcombank investor relations: https://www.vietcombank.com.vn/Nha-dau-tu
- BIDV financial information: https://bidv.com.vn/vn/quan-he-nha-dau-tu/thong-tin-tai-chinh
- BIDV reports and documents: https://bidv.com.vn/vn/quan-he-nha-dau-tu/bao-cao-va-tai-lieu/
- VietinBank investor relations: https://investor.vietinbank.vn/vi
- Techcombank VAS financial statements archive: https://techcombank.com/en/investors/financial-information/financial-statements-vas
- Techcombank investor relations: https://techcombank.com/en/investors
- MB investor relations: https://www.mbbank.com.vn/nha-dau-tu

**Pilot ingestion order:** start with the audited FY2025 consolidated statements and the latest available quarterly consolidated statements, then backfill quarter-end periods from 2023. Do not populate ratios from presentation slides when the underlying definition or calculation basis is not disclosed; preserve the presentation value as source-only until reconciled.


## 8. First staged observation batch

`BIDV_FINANCIAL_HIGHLIGHTS_STAGING.csv` contains 21 annual headline observations (7 metrics × FY2023–FY2025) transcribed from BIDV's official financial-information page. All rows are deliberately marked `review_required` and use `not_disclosed` for consolidation scope. They are **staging values only**, not approved comparison data. Reconcile each item with the corresponding consolidated financial statements, confirm exact statement line, publication date and ratio methodology, then update the status only after review. Do not import these staging rows into a public/verified dataset as-is.


## 9. BIDV annual highlights reconciliation — November 2026

A first reconciliation review of the BIDV annual financial-information page identified metric-definition and reporting-basis conflicts. The 21 values in `BIDV_FINANCIAL_HIGHLIGHTS_STAGING.csv` remain `review_required`; none is approved for standardized bank comparisons.

Official source entry points:
- BIDV annual financial-information table (unit: tỷ VND): https://bidv.com.vn/vn/quan-he-nha-dau-tu/thong-tin-tai-chinh
- BIDV reports and documents, including audited FY2025 consolidated statements: https://bidv.com.vn/vn/quan-he-nha-dau-tu/bao-cao-va-tai-lieu/
- BIDV Annual Report 2025: https://bidv.com.vn/wps/wcm/connect/a8d511f6-3b0b-4ac9-b7f1-8e17ac08bf7e/BIDV_BCTN_2025_%282.1%29_VIE_interactive_15mb.pdf?CACHEID=ROOTWORKSPACE-a8d511f6-3b0b-4ac9-b7f1-8e17ac08bf7e-pS-Z7xM&MOD=AJPERES

Findings requiring explicit mapping before import:
- The annual highlights label for loans is `Dư nợ tín dụng`, which must not automatically be mapped to the balance-sheet line `Cho vay khách hàng`.
- The annual highlights label for deposits is `Tiền gửi và phát hành giấy tờ có giá`, which is not the same as customer deposits alone.
- FY2025 annual-report consolidated highlights show customer loans of 2,372,955 tỷ đồng and customer deposits of 2,222,992 tỷ đồng; these differ from the staged annual highlights values of 2,338,009 and 2,448,399 respectively.
- FY2025 annual-report materials separately disclose standalone CAR of 9.05% and NPL under Circular 31/2024 of 1.26%; these cannot be assumed equivalent to the annual highlights CAR 9.18% and NPL 1.3%.
- Annual-report consolidated ROA is shown as 1.01%, differing from the annual highlights 0.98%. ROE is reported around 19%, while the annual highlights show 19.1%; methodology and scope still need confirmation.
- Total assets for FY2025 are broadly consistent after rounding (3,330,825.72 vs 3,330,826 tỷ đồng), but that alone does not establish the reporting basis for every metric or earlier years.

Decision: retain all staged observations as review-only. Create separate standardized observations from exact consolidated statement line items, and source-specific ratio observations with explicit solo/consolidated and regulatory methodology fields. Never overwrite the original source transcription during reconciliation.


## 10. Standardized BIDV FY2025 consolidated observations

The audited FY2025 consolidated financial statements in the official BIDV Annual Report 2025 have been reconciled for core balance-sheet items. Source report: https://bidv.com.vn/wps/wcm/connect/a8d511f6-3b0b-4ac9-b7f1-8e17ac08bf7e/BIDV_BCTN_2025_%282.1%29_VIE_interactive_15mb.pdf?CACHEID=ROOTWORKSPACE-a8d511f6-3b0b-4ac9-b7f1-8e17ac08bf7e-pS-Z7xM&MOD=AJPERES

The audited consolidated statements are signed by Deloitte on 27/03/2026 and presented in million VND. Convert to tỷ đồng by dividing by 1,000. Reconciled FY2025 values: total assets 3,330,825.720; gross customer loans 2,372,955.074; net carrying amount of customer loans after allowance 2,338,009.521; customer deposits 2,222,991.628; issued valuable papers 225,407.774; customer deposits plus issued valuable papers 2,448,399.402 (all tỷ đồng).

The dashboard metric `loans` is explicitly defined as gross customer loans. Separate `loans_net` records the balance-sheet carrying amount after allowance. Separate `funding_deposits_and_securities` records customer deposits plus issued valuable papers. This prevents the BIDV financial-highlights series from being mislabeled as customer deposits or gross loans.

FY2025 ROE 19.43% and ROA 1.01% are reported in consolidated operating highlights but remain `source_only` pending methodology documentation. NPL 1.26% under Circular 31/2024 remains `review_required` until scope and calculation basis are fully mapped. Standalone CAR 9.05% remains separate from the highlights CAR 9.18%.

See `BIDV_CONSOLIDATED_FY2023_FY2025_VERIFIED.csv` for the standardized observation batch. Only values directly reconciled to audited consolidated statement lines are marked `verified`.
