#! usr/bin/env python3

"""
script that reads a file, extract the letters and counts them.
"""

__autor__ = "Pascal Visser"
__version__ = 1.0

import sys
import pprint


def read_file():
    text = ""
    file = "test.txt"  # input("Voer tekst bestand in: ")
    with open(file) as line:
        for x in line:
            text += x
            text = "".join(text.strip(''))
    return text


def letter_count(text):
    count = {}
    for char in text:
        if not char in count:
            count[char] = 1
        else:
            count[char] += 1
    return count


def visual(letters):
    return "\n".join("{}\t{}".format(k, v) for k, v in sorted(letters.items(), key=lambda t: str(t[0])))


def main(argv=None):
    tekst = read_file()
    letters = letter_count(tekst)
    done = visual(letters)
    print(done)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
