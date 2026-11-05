# NB Public Money Watch

Independent civic transparency MVP for New Brunswick, Canada. Displays curated public-source budget figures, 21 departmental expenditure lines and four officially documented Auditor General case topics.

## Run

Requires Python 3, no frontend build tools:

```bash
python -m http.server 8000
```

Open http://localhost:8000. Do not open `index.html` with `file://` because browsers typically restrict loading local JSON using fetch.

## Data

`data/official.json` includes source URLs and basis labels. As of 2026-11-05. All amounts are CAD. Forecasts are not actuals. Departmental amounts come from the ordinary-account Main Estimates (originally in thousands), **not** the consolidated $15.63B total. Budget variances, audited contract totals and deferred costs are not automatically waste, fraud or recoverable losses.

**Recipient page intentionally contains zero verified payment-level records.** It means no such records have been imported, not that government paid no vendors. Case status in this release is not automatically refreshed.

## Development and validation

```bash
python scripts/validate_data.py
python -m unittest discover -s tests -v
```

GitHub Actions CI validates data integrity on pull requests. An optional source-availability monitor can check for broken source URLs, but cannot verify whether content has changed or substantiate an allegation.

## Roadmap

1. Import official NB supplementary recipient and payment disclosures, preserving each source row.
2. Introduce a normalized payment/vendor/contract/case database with duplicate and reconciliation checks.
3. Schedule source ingestion, snapshots and change detection.
4. Automate audit recommendation follow-up and draft source-linked reports for human approval.
5. Deploy read-only public site once provenance and editorial checks are ready.

This is not an official government application and must not be presented as a live investigations database.
