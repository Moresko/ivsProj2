"""@package mathLib
Balík implementujúci matematické operácie.

======== Copyright (c) 2023, FIT VUT Brno, All rights reserved. ============

Purpose:     IVS 2nd project - package desc

$NoKeywords: $ivs_project_2 $controller.py
$Authors:    Jakub Kasem <xkasem02@stud.fit.vutbr.cz>
             Martin Mores <xmores02@stud.fit.vutbr.cz>
$Date:       $2023-03-13
============================================================================
"""

import decimal
import numpy as np

class MathLibException(Exception):
    """@brief Výnimka kalulačkou interpretovaná ako 'Math error'
    """
    pass

def add(a : float, b: float) -> float:
    """@brief Sčítanie dvoch čísel
    """
    return np.add(a, b).item()

def sub(a : float, b: float) -> float:
    """@brief Odčítanie dvoch čísel.

    Záleží na poradí. Od čísla a bude odčítané číslo b.
    """
    return np.subtract(a, b).item()

def div(a : float, b: float) -> float:
    """@brief Delenie dvoch čísel.

    Záleží na poradí. Číslom b bude delené číslo a.
    """
    if b == 0.00:
        raise MathLibException
    return np.divide(a, b).item()

def mul(a : float, b: float) -> float:
    """@brief Násobenie dvoch čísel.
    """
    return np.multiply(a, b).item()

def power(a : float or decimal.Decimal, p: float or decimal.Decimal) -> float:
    """@brief Umocnenie čísla a na p-mocninu.
    """

    _power = np.power(a, p)
    if type(a) == float and type(p) == float:
        return _power.item()
    return _power
    

def root(a : float, p: float) -> float:
    """@brief Výpočet p-tej odmocniny čísla a.

    """
    if a < 0 and p % 2 == 0:
        raise MathLibException("Math error: can't compute root of negative number") #TODO prepisat text exception
    elif a == 0:
        return 0
    else:
        with decimal.localcontext() as ctx:
            ctx.prec = 500
            root = power(decimal.Decimal(a), decimal.Decimal(1)/decimal.Decimal(p))
        return float(root)

def fac(a : float):
    """@brief Faktoriál čísla a.

    Args:
        @param a (float): základ faktoriálu

    Raises:
        @exceptions MathLibException: ak je základ faktoriálu záporný alebo nie je celé číslo.

    Returns:
        @return float: hodnota faktoriálu čísla a.

    @author Jakub Kasem xkasem02
    """
    if a < 0 or a % 1 != 0:
        raise MathLibException("Input must be a positive integer or zero")
    
    result = float(1)

    if a == 0:
        return result
    
    for i in range(1, int(a) + 1):
        result = mul(result, float(i))

    return result

def perc(a : float):
    """@brief Výpočet jedného percenta čísla a
    """
    return div(a, 100)

