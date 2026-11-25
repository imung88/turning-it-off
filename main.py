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

    # The grader provides a writable output dir and runs us as an
    # unprivileged user on a read-only fs, so just write the one file.
    # umask 022 makes it 0644, readable by the collector.
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip() + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
