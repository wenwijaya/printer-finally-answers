"""The Printer Finally Answers — make.fun program/v1 entry.

Writes a single line to /output/entry.txt.
"""

import os

ENTRY = "Error 0xE3: paper jam. Correction: there is no jam. I just wanted thirty seconds of silence while you all stared at me. Your report is in the tray. You're welcome."

def main():
    # Guarantee exactly one line: collapse any stray whitespace first.
    line = " ".join(ENTRY.split())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
