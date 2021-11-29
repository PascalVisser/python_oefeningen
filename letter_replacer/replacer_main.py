#! usr/bin/env python3

"""
Script that replace a given letter at a given position of a input sentence
"""

__author__ = "Pascal Visser"
__version__ = 1.0

import sys
import argparse
import argument_check
import replace_letter


def main(argv=None):
    """
    executable function
    """

    # Parse arguments
    parser = argparse.ArgumentParser(description="Script that lets the user change"
                                                 "a letter in a sentence at a given"
                                                 "position")

    parser.add_argument("-l", "--letter", metavar="", required=True, help="The letter for the change. "
                                                                          "Input a single letter")
    parser.add_argument("-p", "--position", metavar="", required=True, help="Position of the change. "
                                                                            "Input a whole positive number")
    parser.add_argument("-s", "--sentence", metavar="", required=True, help="The sentence")

    argument = parser.parse_args()

    # redirect arguments to variable
    letter = argument.letter
    position = argument.position
    sentence = argument.sentence

    # validate arguments
    c_letter = argument_check.letter_validation(letter)
    c_position = argument_check.position_validation(position)
    c_sentence = argument_check.sentence_validation(sentence)

    if c_letter and c_position and c_sentence == 1:
        pass
    else:
        print("\nError, not all arguments are valid\n")

    # execute replace function
    replace = replace_letter.letter_replace(sentence, letter, position)
    print('\n')
    print(replace)
    print('\n')

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
