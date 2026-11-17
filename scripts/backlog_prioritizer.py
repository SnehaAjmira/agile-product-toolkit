"""
backlog_prioritizer.py

WSJF (Weighted Shortest Job First) backlog prioritization calculator,
following the SAFe definition:

    Cost of Delay = Business Value + Time Criticality + Risk Reduction
    WSJF          = Cost of Delay / Job Size

Usage:
    python scripts/backlog_prioritizer.py                       # demo backlog
    python scripts/backlog_prioritizer.py --input examples/sample_backlog.csv \
                                          --output examples/prioritized_backlog.csv
"""

import argparse
import csv
from dataclasses import dataclass, field
from typing import List

FIBONACCI = (1, 2, 3, 5, 8, 13, 21)
SCORED_FIELDS = ("business_value", "time_criticality", "risk_reduction", "job_size")


@dataclass
class BacklogItem:
    """A single backlog item scored on the modified Fibonacci scale."""

    id: str
    title: str
    business_value: int
    time_criticality: int
    risk_reduction: int
    job_size: int
    notes: str = ""
    wsjf_score: float = field(init=False)

    def __post_init__(self):
        for name in SCORED_FIELDS:
            value = getattr(self, name)
            if value not in FIBONACCI:
                raise ValueError(f"{self.id}: {name}={value} is not one of {FIBONACCI}")
        self.wsjf_score = round(self.cost_of_delay / self.job_size, 2)

    @property
    def cost_of_delay(self) -> int:
        return self.business_value + self.time_criticality + self.risk_reduction


def load_from_csv(path: str) -> List[BacklogItem]:
    """Load backlog items from a CSV with columns: id, title, the four scores, notes."""
    with open(path, newline="", encoding="utf-8") as f:
        return [
            BacklogItem(
                id=row["id"],
                title=row["title"],
                business_value=int(row["business_value"]),
                time_criticality=int(row["time_criticality"]),
                risk_reduction=int(row["risk_reduction"]),
                job_size=int(row["job_size"]),
                notes=row.get("notes", ""),
            )
            for row in csv.DictReader(f)
        ]


def prioritize(items: List[BacklogItem]) -> List[BacklogItem]:
    """Sort by WSJF (highest first). Ties go to the smaller job, then higher cost of delay."""
    return sorted(items, key=lambda i: (-i.wsjf_score, i.job_size, -i.cost_of_delay))


def save_to_csv(items: List[BacklogItem], path: str) -> None:
    fields = ["rank", "id", "title", "wsjf_score", "cost_of_delay", *SCORED_FIELDS, "notes"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for rank, item in enumerate(items, start=1):
            writer.writerow({
                "rank": rank, "id": item.id, "title": item.title,
                "wsjf_score": item.wsjf_score, "cost_of_delay": item.cost_of_delay,
                **{name: getattr(item, name) for name in SCORED_FIELDS},
                "notes": item.notes,
            })


def print_table(items: List[BacklogItem]) -> None:
    print(f"{'Rank':<5}{'ID':<9}{'WSJF':>6}  {'Title':<44}{'BV':>4}{'TC':>4}{'RR':>4}{'Size':>6}")
    print("-" * 82)
    for rank, i in enumerate(items, start=1):
        print(f"{rank:<5}{i.id:<9}{i.wsjf_score:>6.2f}  {i.title[:43]:<44}"
              f"{i.business_value:>4}{i.time_criticality:>4}{i.risk_reduction:>4}{i.job_size:>6}")


DEMO = [
    BacklogItem("US-001", "Instrument data webhook integration", 13, 8, 8, 5),
    BacklogItem("US-002", "QC metrics dashboard", 8, 5, 3, 3),
    BacklogItem("US-003", "Role-based access control", 5, 13, 13, 8),
    BacklogItem("US-004", "Automated certificate of analysis", 8, 3, 2, 2),
    BacklogItem("US-005", "Data validation checkpoints", 5, 8, 13, 3),
]


def main():
    parser = argparse.ArgumentParser(description="WSJF backlog prioritizer")
    parser.add_argument("--input", help="CSV file of backlog items")
    parser.add_argument("--output", help="CSV file for the prioritized backlog")
    args = parser.parse_args()

    ranked = prioritize(load_from_csv(args.input) if args.input else DEMO)
    print_table(ranked)
    if args.output:
        save_to_csv(ranked, args.output)
        print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
