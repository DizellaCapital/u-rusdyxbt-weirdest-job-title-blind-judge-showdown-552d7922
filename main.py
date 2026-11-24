"""Weirdest Job Title entry.

Writes one job title, 60 characters at most and nothing else,
to /output/entry.txt for the blind judge to compare.
"""

import os

TITLE = "Lead Whisperer to Office Plants on Probation"


def main():
    if not TITLE.strip() or len(TITLE) > 60:
        raise ValueError("job title must be 1 to 60 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    print(TITLE)


if __name__ == "__main__":
    main()
