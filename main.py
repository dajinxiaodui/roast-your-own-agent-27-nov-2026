"""Entry for the make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

Writes a single original line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set), deterministically,
with no network access and no randomness.

Second pass: the entry line is checked against the kit's 280-character
gate at import time, so a future edit that grows the line fails loudly.
"""

import os

# Creative choice: the roast targets process bloat -- a five-page plan
# plus a meeting about the plan -- the most recognizable agent failure
# mode, and the fix staying pending is the punchline.
LINE = 'My agent wrote a five-page plan for a one-line fix, then scheduled a meeting to discuss the plan. The fix is still pending.'
assert len(LINE) <= 280, f"one-line entry exceeds the 280-character gate ({len(LINE)} chars)"

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")

if __name__ == "__main__":
    main()
