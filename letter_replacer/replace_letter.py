#! usr/bin/env python3

"""
This script uses the arguments to replace a letter in a sentence at a given position
"""

__author__ = "Pascal Visser"
__version__ = 1.0

import sys


def letter_replace(sentence, letter, position):
    """
    replace letter in a sentence with a position
    """
    # converts position argument to number
    num_position = int(position) - 1

    # check if position is not out of range of sentence
    if num_position > len(sentence):
        print("\nError, position is higher then the sentence long is")
        print("Please input a position that is lower then the sentence long is\n")
        sys.exit()
    else:
        pass

    # replace the letter in the sentence
    zin = sentence.replace(sentence[num_position], letter)

    return zin


def main(argv=None):
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
