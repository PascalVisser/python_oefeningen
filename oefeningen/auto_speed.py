#!/usr/bin/env python3

"""
script that calculates the 0-100 km/uur acceleration of a car.
based on the weight and horsepower
"""

__author__ = "Pascal"

import sys


def accleration(weight, pk):
    """
    calculate the zero to hundred
    """
    weight = int(weight)
    pk = int(pk)
    speed = weight / pk
    speed = speed.__round__(2)
    return speed


def pk_per_cylinder(cylinder, pk):
    """
    calculates horsepower per cylinder
    """
    pk = int(pk)
    cylinder = int(cylinder)
    ppc = pk / cylinder
    ppc = ppc.__round__(2)
    return ppc


def pk_per_rpm(koppel, rpm, pk):
    """
    calculates horsepower at any given rpm
    """
    pk = int(pk)
    koppel = int(koppel)
    rpm = int(rpm)
    pks = koppel * rpm / 5252
    pks = pks.__round__(2)
    if pks >= pk:
        pks = pk
    return pks


def pk_to_kw(pk):
    """
    calculates pk to kw
    """
    pk = int(pk)
    kw = 0.734
    kww = pk*0.734
    kww = kww.__round__(1)
    return kww


def verbruik_berekenen(vraag):
    """
    calculates the fuel comsuption of the car
    """
    vraag = vraag.upper()
    if vraag == "JA":
        km = input("Gemiddeld aantal kilometers op een tank:")
        tank = input("inhoud tank in liters:")
        print('')
        km = int(km)
        tank = int(tank)
        verbryk = km / tank
        verbryk = verbryk.__round__(2)
        return verbryk
    elif vraag == "NEE":
        pass


def main(args):
    """
    main function
    """
    naam_voertuig = input("Voer merk en model van het voertuig in:")
    weight = input("Voer gewicht auto in (kg):")
    hp = input("Voer aantal pk's in:")
    koppel = input("Voer het koppel in (nm):")
    cylinder = input("Voer aantal cylinders in:")
    rpm = input("Voer motortoerental(rpm) in om pk's te berkenen op dat toerental:")
    vraag = input("Wilt u het verbruik ook berekenen? (ja/nee)")
    print('')

    speed = accleration(weight, hp)
    ppc = pk_per_cylinder(cylinder, hp)
    pk = pk_per_rpm(koppel, rpm, hp)
    verbruik = verbruik_berekenen(vraag)
    kw = pk_to_kw(hp)

    print("De {} accelereert in {} seconden van 0 naar 100 km/uur".format(naam_voertuig, speed))
    print("De {} heeft {} pk per cylinder".format(naam_voertuig, ppc))
    print("De {} levert {} Pk bij {} rpm".format(naam_voertuig, pk, rpm))
    print("De {} heeft een vermogen van {}pk, oftewel {} kW".format(naam_voertuig, hp, kw))
    if vraag.upper() == "JA":
        print("De {} rijdt 1 op {} gemiddeld".format(naam_voertuig, verbruik))
    else:
        pass
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit = exitcode
