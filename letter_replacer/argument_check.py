#! usr/bin/env python3

"""
check script for command line arguments
"""

__author__ = "Pascal Visser"
__version__ = 1.0


import sys


def letter_validation(letter):
    """
    Validate letter argument
    """
    # check if letter is a single character
    if len(letter) == 1:
        pass
    else:
        print("\nError, input 'letter' is not a single character")
        print("Please provide a single character\n")
        sys.exit()

    # check if input is a letter
    if letter.isalpha():
        pass
    else:
        print("\nError, 'letter' input is not a letter")
        print("Likely a number or a character")
        print("Please input a letter.\n")
        sys.exit()

    return 1


def position_validation(position):
    """
    Validate position argument
    """
    # check if input is a number
    try:
        a_position = int(position)
    except ValueError:
        print("\nError, Position argument is not a number.")
        print("Please input a number\n")
        sys.exit()

    # check if number is positive
    if a_position <= 0:
        print("\nError, Number is negative")
        print("Please provide a positive number\n")
        sys.exit()
    else:
        pass

    return 1


def sentence_validation(sentence):
    """
    validate sentence argument
    """
    # check if input sentence is long enough
    if len(sentence) <= 10:
        print("\nInput Sentence is to short")
        print("Please input a proper sentence\n")
        sys.exit()
    else:
        pass

    return 1


def main(argv=None):
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
