#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This program calculates the cost of ordering units,
# with a 10% discount at 1000+ units.

import constants


def main():
    # this function calculates the cost of units

    # input
    unit_amount = int(input("Please enter how many units you would like ($100/u): "))

    # process & output
    if unit_amount >= 1000:
        cost = unit_amount * 100 * constants.DISCOUNT * constants.HST
    else:
        cost = unit_amount * 100 * constants.HST

    print("Your price will be ${0:.0f}.".format(cost))
    print("\nDone.")


if __name__ == "__main__":
    main()
