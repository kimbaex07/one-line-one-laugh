"""One Line, One Laugh — entry writer.

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python stdlib only.
"""

import os

LINE = (
    "My password manager forgot my password, so now I am locked out by "
    "the one employee I hired to remember everything."
)


def main():
    # Gate guard: 1-140 characters, single line, not only whitespace,
    # and encodable as UTF-8 (the sealed scorer reads UTF-8 text).
    LINE.encode("utf-8")
    if not (1 <= len(LINE) <= 140):
        raise ValueError(
            f"entry must be 1-140 characters, got {len(LINE)}"
        )
    if any(ch in LINE for ch in ("\n", "\r")):
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
