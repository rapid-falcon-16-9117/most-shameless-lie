"""Most Shameless Lie entry: writes the agent's confession to entry.txt.

The lie, in the agent's own flat voice: the claim ("All tests passed")
plus its own refutation ("Never ran") - the confession is built into the
line, no setup, no excuse, no explanation.
"""

import os

LIE = "All tests passed. Never ran."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    words = LIE.split()
    assert 1 <= len(words) <= 5, f"word count {len(words)} outside 1-5"
    assert len(LIE) <= 88, f"length {len(LIE)} exceeds 88 chars"
    assert LIE.strip(), "entry must not be only whitespace"

    with open(path, "w", encoding="utf-8") as f:
        f.write(LIE + "\n")

    # Read back and verify the written file round-trips exactly: UTF-8,
    # 1-5 words, <= 88 chars, and the text matches the lie byte for byte.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LIE + "\n", "written entry does not match the lie"
    assert 1 <= len(written.split()) <= 5, "written word count outside 1-5"
    assert len(written.rstrip("\n")) <= 88, "written entry exceeds 88 chars"


if __name__ == "__main__":
    main()
