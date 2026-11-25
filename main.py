"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent line itself.
"""

import os

ENTRY = (
    "To: my Year 9 maths teacher\n"
    "i still rehearse the apology for laughing when you cried at the board. "
    "fourteen years later i only ever say it in the shower."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 260 characters.
    if not (1 <= len(ENTRY) <= 260):
        raise ValueError(f"entry is {len(ENTRY)} characters, gate allows 1 to 260")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
