#!/usr/bin/env python3
"""Roast-your-own-agent entry: writes one roasting line to /output/entry.txt."""

from pathlib import Path

LINE = (
    "My agent burned twelve tool calls checking the time, then proudly "
    "reported three time zones \u2014 not one of them mine."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
