#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.pokemon import *

from enum import Enum

"""
This Python module contains not only the Enum WeaponType, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  weapon_type.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.



class WeaponType(Enum):
    
    PUNCH = 2
    KICK = 4
    ELBOW = 6
    HEADBUTT = 10

    def __str__(self):
        return self.name

    @staticmethod
      
    def tipo_ataque(stringdelarma):

        stringdelarma=stringdelarma.lower()
        if (stringdelarma == 'punch'):
            return WeaponType.PUNCH
        elif (stringdelarma == 'kick'):
            return WeaponType.KICK
        elif (stringdelarma == 'elbow'):
            return WeaponType.ELBOW
        elif (stringdelarma == 'headbutt'):
            return WeaponType.HEADBUTT
        else:
            print('***'+str(stringdelarma.upper())+' NO ES UN TIPO DE ATAQUE REGISTRADO***')


def main():
    """Function main of the module.

    The function main of this module is used to test the Class WeaponType.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Check Class WeaponType - Name.")
    print("=================================================================.")

    if isinstance(WeaponType.PUNCH, WeaponType):
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.KICK, WeaponType):
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.ELBOW, WeaponType):
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.HEADBUTT, WeaponType):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class WeaponType - Value.")
    print("=================================================================.")

    if WeaponType.PUNCH.value == 2:
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.KICK.value == 4:
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.ELBOW.value == 6:
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.HEADBUTT.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
