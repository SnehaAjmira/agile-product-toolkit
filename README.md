# Agile Product Toolkit

Requirements templates and a tested WSJF backlog prioritization script for Product Owners and Business Analysts.

| | |
|---|---|
| **Domain** | Product ownership, business analysis, Agile/Scrum |
| **Tools** | Python 3 (standard library only), Markdown |
| **Contents** | 2 templates, 1 script, sample data, unit tests |

---

## 1. Contents

| File | Purpose |
|---|---|
| `templates/BRD_template.md` | Business Requirements Document: objectives, scope, stakeholders, requirements, sign-off |
| `templates/user_story_template.md` | User story with Given/When/Then acceptance criteria, NFRs, and Definition of Done |
| `scripts/backlog_prioritizer.py` | Scores and ranks backlog items using WSJF |
| `examples/sample_backlog.csv` | 8 example backlog items from a laboratory system context |
| `examples/prioritized_backlog.csv` | Output generated from the sample file |
| `tests/test_backlog_prioritizer.py` | Unit tests for scoring, validation, and ranking |

## 2. WSJF Method

```
Cost of Delay = Business Value + Time Criticality + Risk Reduction
WSJF          = Cost of Delay / Job Size
```

All four inputs use the modified Fibonacci scale (1, 2, 3, 5, 8, 13, 21). Values outside the scale are rejected. Ties are broken by smaller job size, then higher cost of delay.

## 3. Example Output

Generated from `examples/sample_backlog.csv`:

| Rank | ID | Item | WSJF |
|---:|---|---|---:|
| 1 | US-104 | Audit trail export to CSV | 13.00 |
| 2 | US-106 | Instrument calibration reminders | 7.00 |
| 3 | US-101 | Electronic signature on result approval | 5.88 |
| 4 | US-103 | Turnaround time dashboard | 4.33 |
| 5 | US-102 | Sample intake barcode scanning | 3.20 |
| 6 | US-107 | Bulk status update for samples | 3.00 |
| 7 | US-105 | Customer portal result download | 1.54 |
| 8 | US-108 | Stability study scheduling module | 0.67 |

The ranking shows the main WSJF trade-off: US-101 has the highest cost of delay (47) but ranks third because of its size, and US-108 drops to last because its 21-point size signals it should be split.

## 4. How to Run

```bash
# Demo backlog
python scripts/backlog_prioritizer.py

# Your own backlog
python scripts/backlog_prioritizer.py --input examples/sample_backlog.csv --output examples/prioritized_backlog.csv

# Tests
python -m unittest discover -s tests -v
```

Input CSV columns: `id, title, business_value, time_criticality, risk_reduction, job_size, notes`.

## 5. Repository Structure

```
agile-product-toolkit/
├── templates/
│   ├── BRD_template.md
│   └── user_story_template.md
├── scripts/
│   └── backlog_prioritizer.py
├── examples/
│   ├── sample_backlog.csv
│   └── prioritized_backlog.csv
└── tests/
    └── test_backlog_prioritizer.py
```

Author: [Sneha Ajmira](https://linkedin.com/in/contactsnehaajmira), PSPO I
