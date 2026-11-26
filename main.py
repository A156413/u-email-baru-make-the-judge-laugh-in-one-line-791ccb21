"""One-line entry for make.fun: Make the Judge Laugh in One Line.

The program writes a single joke line to entry.txt in the output
directory (``$MAKEFUN_OUTPUT_DIR``, default ``/output``) and prints
the same line to stdout. It is fully deterministic: no network,
no randomness, no clock, standard library only.
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


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")
    os.chmod(entry_path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
