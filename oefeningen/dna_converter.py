#!/usr/bin/env python3


"""
This program converts a dna sequence to the translated protein sequence
"""

__author__ = 'Pascal Visser'

import sys
import pydoc
import re
import argparse

translation = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
               "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
               "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
               "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
               "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
               "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
               "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
               "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
               "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
               "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
               "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
               "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
               "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
               "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
               "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
               "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }


def check_dna(seq):
    seq = seq.upper()
    valid = 'ACTG'
    for letter in seq:
        if letter not in valid:
            try:
                print("DNA not valid!")
                sys.exit()
            except TypeError as e:
                print(f"Dna not valid!", {e})
                sys.exit()
    return seq


def check_triplet(seq):
    if len(seq) % 3 == 0:
        print("DNA is valid!")
        return seq
    else:
        print("DNA is not triplet of three")
        sys.exit()


def make_rna(dna):
    dna = dna.upper()
    rna = dna.replace("T", "U")
    return rna


def make_codons(rna):
    codons = re.findall("...", rna)
    return codons


def translate_seq(seq):
    protein_seq = ''
    for amino in seq:
        for key, value in translation.items():
            amino = amino.replace(key, value)
        if len(amino) == 1:
            protein_seq += amino
    return protein_seq


def main(argv=None):

    parser = argparse.ArgumentParser()
    parser.add_argument('-D', "--DNA", type=str, help="Insert DNA sequence", metavar="", required=True)
    args = parser.parse_args()

    valid_seq = check_dna(args.DNA)
    valid_dna = check_triplet(valid_seq)
    rna_seq = make_rna(valid_dna)
    codons = make_codons(rna_seq)
    protein = translate_seq(codons)
    print(protein)

    return 0


if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)
