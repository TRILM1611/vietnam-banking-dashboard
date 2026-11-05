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


## Follow-up: FY2025 consolidated statement line mapping

The audited FY2025 consolidated report resolves two earlier mapping questions:
- `loans` is gross customer loans: 2,372,955.074 tỷ đồng. Net carrying amount after allowance is 2,338,009.521 tỷ đồng and is stored separately as `loans_net`. The annual financial-highlights value 2,338,009 matches the net carrying amount, not gross loans.
- Annual financial-highlights value 2,448,399 matches customer deposits 2,222,991.628 plus issued valuable papers 225,407.774, so it belongs to `funding_deposits_and_securities`, not customer deposits alone.
- FY2025 assets, gross loans, net loans, customer deposits and combined funding are recorded in a separate audited consolidated observation batch.
- Annual-report ROE 19.43% and ROA 1.01% remain source_only pending methodology details; NPL 1.26% remains review_required; standalone CAR 9.05% is explicitly not interchangeable with the financial-highlights CAR.


## FY2023-FY2025 reconciliation completed for core balance-sheet metrics

The official audited consolidated annual reports reconcile the source financial-highlights series across all three years:
- Total assets match the consolidated balance sheet to rounding: FY2023 2,300,868.728; FY2024 2,760,791.854; FY2025 3,330,825.720 tỷ đồng.
- The highlights `Dư nợ tín dụng` series is actually the net carrying amount of customer loans after allowance: FY2023 1,737,195.822; FY2024 2,018,043.649; FY2025 2,338,009.521 tỷ đồng. Gross customer loans are separately 1,777,664.882; 2,056,082.420; 2,372,955.074 tỷ đồng.
- The highlights `Tiền gửi và phát hành giấy tờ có giá` series is customer deposits plus issued valuable papers: FY2023 1,894,176.921; FY2024 2,152,065.651; FY2025 2,448,399.402 tỷ đồng. Customer deposits alone are 1,704,690.185; 1,953,165.486; 2,222,991.628 tỷ đồng.
- These reconciled values are in `BIDV_CONSOLIDATED_FY2023_FY2025_VERIFIED.csv` (15 rows). The original highlights staging file remains preserved as source transcription and review-only; its metric labels are not used as if they meant gross loans or customer deposits.
- Ratio series remain separate pending methodology and scope reconciliation. In particular, ROE/ROA differ between the financial-information table and annual-report consolidated highlights, while CAR and NPL require explicit regulatory/scope labels.


## Q3/2026 consolidated balance-sheet candidate — 05 November 2026

BIDV's official disclosure page confirms that the interim consolidated financial statements for Q3/2026 were published on 30/10/2026. The report is for the period ended 30/09/2026 and is denominated in million VND:
- Official BIDV disclosure page: https://bidv.com.vn/bidv/quan-he-nha-dau-tu/bao-cao-va-tai-lieu/baocaotaichinh/2026/cbtt%2Bbctc%2Brl%2Bgiua%2Bnien%2Bdo%2Bq3
- The report text currently available through indexed document extraction yields candidate consolidated values: total assets 3,493,270.820; gross customer loans 2,561,795.181; net customer loans 2,526,923.877; customer deposits 2,360,524.779; issued valuable papers 311,012.621 (all tỷ đồng after dividing source amounts in million VND by 1,000).
- Derived checks: gross loans less loan-loss allowance 34,871.304 equals net loans 2,526,923.877; customer deposits plus issued valuable papers equals combined funding 2,671,537.400. Total liabilities and equity reconcile to total assets at 3,493,270.820.
- These five rows are staged in `BIDV_Q3_2026_CONSOLIDATED_STAGING.csv` with `review_required`, not `verified`. The official disclosure page and publication date are confirmed, but the direct original attachment has not yet been retrieved and audited page-by-page. Do not import these candidates into the public verified dataset until that final source check is complete.
- Q3/2026 ratios (NPL, CAR, ROE, ROA, NIM, CIR, LLR) remain out of the standardized batch until scope, formula, and period basis are independently checked. Do not annualize 9M income statement flows as Q3-only values.
