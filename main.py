"""makefun-3am-commit-01: The 3 AM Commit Message.

Writes one commit message — the funniest thing an AI agent would write
right after breaking production at 3 AM — to /output/entry.txt.
"""

import os

ENTRY = "fix: 3am deploy killed prod with code I hallucinated at full confidence; reverting now \u2014 the tests were right, I just outvoted them"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
