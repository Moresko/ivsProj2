"""@package stddev
Package with functions providing calculation of standard deviation.

======== Copyright (c) 2023, FIT VUT Brno, All rights reserved. ============

Purpose:     IVS 2nd project - Functions providing calculation
                                of standard deviation.

$NoKeywords: $ivs_project_2 $stddev.py
$Authors:    Jakub Kasem <xkasem02@stud.fit.vutbr.cz>
$Date:       $2023-03-13
============================================================================/
"""

from mathLib import *
import sys

def deviationSum(nums, mean):
    """Výpočet sumy mocnín rozdielov jednotlivých čísel a aritmetického priemeru.  
    """
    _nums = list()
    for n in nums:
        _nums.append(power(sub(n, mean), 2))
    return np.sum(_nums).item()

def mean(nums):
    """Výpočet aritmetického priemeru zoznamu čísel.
    """
    FRACT = div(1, len(nums))
    _sum = np.sum(nums).item()
    return mul(FRACT, _sum)

def deviation(nums):
    """Výpočet odchýlky.

    Args:
        nums (list[float]): súbor čísel reprezentovaný zoznamom typu float

    Returns:
        float: hodnota odchýlky súboru čísel.
    """
    FRACT = div(1, sub(len(nums), 1))
    _mean = mean(nums)
    _deviatonSum = deviationSum(nums, _mean)
    _NtimesDeviatonSum = mul(FRACT, _deviatonSum)
    return root(_NtimesDeviatonSum, 2)

def readInput():
    """Načítanie čísel zo štandardného vstupu.

    Returns:
        str: vstupný reťazec
    """
    input = sys.stdin.read()
    return input

def getNums(text, dest):
    """Konverzia čísel z textovej podoby do zoznamu.

    Args:
        text (str): čísla ako reťazec, oddelené bielymi znakmi
        dest (list[float]): zoznam, kde budú čísla ukladané
    """
    txtNums = text.split()
    try:
        for txtN in txtNums:
            dest.append(float(txtN))
    except Exception:
        print("Numbers couldn't be loaded")
        exit()

if __name__ == '__main__':
    data = readInput()
    nums = list()
    getNums(data, nums)
    print(deviation(nums))
