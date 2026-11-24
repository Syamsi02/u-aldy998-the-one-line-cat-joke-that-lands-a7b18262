"""One-line cat joke entry.

Writes a single joke about cats, one line under 200 characters,
to /output/entry.txt. Pure standard library, fully deterministic.
"""

import os

JOKE = "My cat knocked my phone off the table, then looked at me like I'd dropped it."


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
