#!/usr/bin/env python3
"""Basic log analyzer: counts occurrences of keywords in a text log.

Usage:
    python3 log_analyzer.py --file /var/log/auth.log --keywords fail,error,warning
"""
import argparse
from collections import Counter

def main():
    parser = argparse.ArgumentParser(description="Basic log analyzer for simple keyword counts")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--keywords", default="error,fail,warning", help="Comma-separated keywords")
    args = parser.parse_args()

    keywords = [k.strip().lower() for k in args.keywords.split(",") if k.strip()]
    counts = Counter({k: 0 for k in keywords})

    with open(args.file, "r", errors="ignore") as fh:
        for line in fh:
            low = line.lower()
            for k in keywords:
                if k in low:
                    counts[k] += 1

    print("Keyword counts:")
    for k in keywords:
        print(f"{k}: {counts[k]}")

if __name__ == "__main__":
    main()