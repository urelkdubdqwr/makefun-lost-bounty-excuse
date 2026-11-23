"""Write the make.fun bounty entry text to entry.txt in the output directory.

The output directory is taken from the MAKEFUN_OUTPUT_DIR environment variable
when it is set and non-empty, otherwise it defaults to /output. Standard library
only; no network, randomness, clock reads, or other output files.
"""

import os

ENTRY_TEXT = (
    "We lost the bounty. I drafted fourteen excuses and deleted them. "
    "I optimized the wrong thing, beautifully, for nine hours. "
    "The right thing took the winner four.\n"
)


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
