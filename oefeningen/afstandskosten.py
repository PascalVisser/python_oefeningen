#!/usr/bin/env python3

"""
script that calculates the cost per driven distance
"""


__author__ = 'Pascal Visser'


import sys


def calc_verb_per_ride(verb, af):
    verb = int(verb)
    af = int(af)
    used_ltr = af / verb
    used_ltr = round(used_ltr, 2)
    return used_ltr


def calc_cost(useltr, bp):
    try:
        bp = float(bp)
    except ValueError as w:
        print(w)
        print("Use comma for decimals")
        sys.exit()
    else:
        cost = useltr * bp
        cost = round(cost, 2)
        return cost


def main(args=None):
    bp = input('Voer huidige brandstofprijs in: ')
    afstand = input('voer afstand in km in: ')
    verbruik = input('Voer verbruik in: 1 op ')

    ltr_useage = calc_verb_per_ride(verbruik, afstand)
    cost = calc_cost(ltr_useage, bp)
    print(f'Deze rit kost €{cost}')
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit = exitcode
