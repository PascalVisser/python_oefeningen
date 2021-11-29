#!/usr/bin/env python3

"""
script that calculates the0 to 100 of a stock car versus the tuned car
"""

__author__ = "pascal"


import sys


def acc(pk,gewicht):
    """
    calculates acceleration of a car, based on the weight and horsepower
    """
    pk = int(pk)
    gewicht = int(gewicht)
    accer = gewicht/pk
    accer = accer.__round__(2)
    return accer

def new_acc(answer):
    """
    calculates new acceleration with new values
    """
    answer = answer.upper()
    if answer == "JA":
        new_pk = input("Voer nieuw vermogen in:")
        new_kg = input("Voer nieuw gewicht (kg) in:")
        new_pk = int(new_pk)
        new_kg = int(new_kg)
        new_accer = new_kg/new_pk
        new_accer = new_accer.__round__(2)
        return new_accer
    elif answer == "NEE":
        exit()
    else:
        print("Voer alleen ja of nee in")
        exit()


def verschil(stock, new):
    """
    calculates differance between stock en new, in seconde
    """
    stock = float(stock)
    new = float(new)
    diff = stock-new
    diff = diff.__round__(2)
    return diff


def main(args):
    """
    main function
    """
    naam = input("Voer merk en model in:")
    stock_pk = input("Voer standaard pk in:")
    stock_kg = input("Voer standaard gewicht (kg) in:")
    print('')
    stock_acc = acc(stock_pk, stock_kg)
    print("De standaard {} trekt in {} seconden op van 0 naar 100 km/uur".format(naam, stock_acc))
    print('')
    vraag = input("Wilt u ook een ander vermogen en gewicht opgeven? (ja/nee)")
    print('')
    nieuw_acc = new_acc(vraag)
    print('')
    print("Met het nieuwe gewicht en vermogen, accelereert de {} in {} seconde van 0 naar 100 km/uur".format(naam, nieuw_acc))
    dif = verschil(stock_acc, nieuw_acc)
    print("Dat is een verschil van {} seconden".format(dif))


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit = exitcode
