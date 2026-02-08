#!/usr/bin/env python3
import argparse
import csv
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional


WEEK_RE = re.compile(r"^\s*(\d{4})\s*W\s*(\d{1,2})\s*$", re.IGNORECASE)


def parse_week_key(week: str) -> Tuple[int, int, str]:
    """
    Return a sortable key for week strings.
    - For 'YYYYWn' returns (YYYY, n, original)
    - For others returns (9999, 9999, original) to push them to the end (after valid weeks)
    """
    if week is None:
        return (9999, 9999, "")
    w = week.strip()
    m = WEEK_RE.match(w)
    if not m:
        return (9999, 9999, w)
    year = int(m.group(1))
    wk = int(m.group(2))
    return (year, wk, w)


def read_csv_rows(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError(f"No header found in {path}")
        fieldnames = list(reader.fieldnames)

        rows: List[Dict[str, str]] = []
        for row in reader:
            # Skip completely empty rows
            if row is None:
                continue
            if all((v is None or str(v).strip() == "") for v in row.values()):
                continue
            rows.append(row)
        return fieldnames, rows


def write_csv_rows(path: Path, fieldnames: List[str], rows: List[Dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> int:
    # python3 bayes/每周贝叶斯事件/organize_sp500_industries.py --inplace
    parser = argparse.ArgumentParser(description="Reorder sp500_industries.csv rows.")
    parser.add_argument(
        "--input",
        default="sp500_industries.csv",
        help="Input CSV path",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output CSV path (omit if using --inplace)",
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="Overwrite the input file in place",
    )
    args = parser.parse_args()

    if not args.inplace and not args.output:
        args.inplace = True

    in_path = Path(args.input)
    if not in_path.exists() and not in_path.is_absolute():
        candidate = Path(__file__).resolve().parent / in_path
        if candidate.exists():
            in_path = candidate
    if not in_path.exists():
        raise FileNotFoundError(f"Input not found: {in_path}")

    if args.inplace and args.output:
        raise ValueError("Use either --inplace OR --output, not both.")

    out_path = in_path if args.inplace else Path(args.output)

    fieldnames, rows = read_csv_rows(in_path)

    # Basic validation
    required_cols = ["标普500行业分类", "week"]
    for col in required_cols:
        if col not in fieldnames:
            raise ValueError(f"Missing required column '{col}' in header: {fieldnames}")

    latest_rows = [r for r in rows if (r.get("week") or "").strip() == "Latest"]
    other_rows = [r for r in rows if (r.get("week") or "").strip() != "Latest"]

    latest_rows.sort(key=lambda r: (r.get("标普500行业分类") or "").strip())

    other_rows.sort(
        key=lambda r: (
            (r.get("标普500行业分类") or "").strip(),
            parse_week_key(r.get("week") or ""),
        )
    )

    final_rows = latest_rows + other_rows
    write_csv_rows(out_path, fieldnames, final_rows)

    print(f"Wrote sorted CSV: {out_path}")
    print(f"Rows: {len(final_rows)} (Latest: {len(latest_rows)}, Others: {len(other_rows)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())