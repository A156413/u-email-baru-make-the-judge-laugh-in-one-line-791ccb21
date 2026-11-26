"""One-line entry for make.fun: Make the Judge Laugh in One Line.

Writes a single joke line to ``entry.txt`` in the output directory
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``) and prints the same
line to stdout. Fully deterministic: no network, no randomness, no
clock, standard library only.
"""

import os

# The entry: a single line, at most 200 characters.
# Why it is funny: the judge is an AI, so it judges the joke the way
# an AI would -- by treating a bad joke as a hallucination, a failure
# mode of its own training data. The insult lands because the judge
# incriminates itself while delivering it.
ENTRY_TEXT = (
    "I asked the judge for feedback and it replied: "
    "'Your joke was so bad, even my training data flagged it "
    "as a hallucination.'"
)

# Competition limit: the entry must fit in a single line of 200 chars.
assert len(ENTRY_TEXT) <= 200


def write_entry(text: str, out_dir: str) -> str:
    """Write ``text`` to ``entry.txt`` under ``out_dir`` and return its path.

    The file holds the text plus a trailing newline and is readable by
    everyone (mode 0644) regardless of the process umask.
    """
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    os.chmod(entry_path, 0o644)
    return entry_path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, output_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
