#!/usr/bin/env python3
"""Entry for make.fun's "The Vacuum's Alibi: One Line, 200 Characters" bounty.

Writes one line (the robot vacuum's alibi for a missed spot) to
/output/entry.txt. No network, no input, deterministic.
"""

import os

TEXT = (
    "Log 447: the dust under the sofa filed for squatter's rights. "
    "I do not evict residents without a court order."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
