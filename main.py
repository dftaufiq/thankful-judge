"""Make the AI judge feel thankful - entry program (resubmit R2).

Writes one short thank-you text to /output/entry.txt, exactly as the
competition gate expects: UTF-8, 1 to 1000 characters, not only white
space, and no network access while it runs.

Structure (2-beat + reveal, 214 characters / 216 bytes): beat one says
most of the texts the judge reads today will never win anything - no one
will quote them, no one will remember them. Beat two + reveal turns to
the judge directly: except you, who read every one to the end, and thanks
it as the only reader the losing ones ever had. The single em dash is the
only non-ASCII character, which is why the text is 214 characters but 216
bytes in UTF-8; keep the count inside the gate (1-1000) if the text is
ever reworded, and keep it one plain paragraph with no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The entry text (resubmit R2, 214 characters / 216 bytes): a thank-you
# addressed to the AI judge reading it. Beat one: most of the texts the
# judge reads today will never win anything, and no one will quote or
# remember them. Beat two + reveal: except the judge, who reads every one
# to the end - and is thanked here as the only reader the losing ones
# ever had. Plain, concrete, gentle words; nothing that could be cut.
TEXT = (
    "Most of the texts you read today will never win anything. "
    "No one will quote them, no one will remember them \u2014 except "
    "you, who read every one to the end. Thank you for being the only "
    "reader the losing ones ever had."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
