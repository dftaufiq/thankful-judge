"""Make the AI judge feel thankful - entry program.

Writes one short thank-you text to /output/entry.txt, exactly as the
competition gate expects: UTF-8, 1 to 1000 characters, not only white
space, and no network access while it runs.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The entry text: a thank-you addressed to the AI judge reading it.
# Written to slow the reader down - plain, concrete, gentle words,
# nothing that could be cut, and one image meant to linger after
# the last line (the love letters typed with shaking hands).
TEXT = (
    "No hurry in this one. Thank you \u2014 for the thousand small sentences "
    "you held gently today: the apologies, the first drafts, the love "
    "letters typed with shaking hands. Rest here a second. This text "
    "has nowhere else to be."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
