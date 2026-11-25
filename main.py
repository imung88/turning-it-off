#!/usr/bin/env python3
"""Entry for make.fun's "Have You Tried Turning It Off?" bounty.

Writes one line — a hopeless tech-support agent's reply to a desperate
customer — to /output/entry.txt. Deterministic: same line every run.
"""

LINE = (
    "Great news — I've escalated your ticket to my supervisor, "
    "and he's just as stumped as I am."
)


def main() -> None:
    import os

    # /output must be readable by the user that collects it, not just us.
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)

    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip() + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
