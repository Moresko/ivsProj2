"""@package mathLibTest
Testy pre matematicku kniznicu
======== Copyright (c) 2023, FIT VUT Brno, All rights reserved. ============
 Purpose:     IVS 2nd project 
 $NoKeywords: $ivs_project_2 $mathLibTest.py
 $Authors:      Katarina Kozakova
 $Date:       $2023-04-22
============================================================================
"""


import unittest
from mathLib import *


class TestAdd(unittest.TestCase):
    """@brief Testy funkcie add
    """
    def testPositiveNums(self):
        """@brief Scitanie kladnych cisel
        """
        a , b = 4.00, 6.20
        _add = add(a, b)
        self.assertEqual(_add, 10.2)
    def testNegativeNums(self):
        """@brief Scitanie negtivnych cisel
        """
        a, b = -4.00, -6.20
        _add = add(a, b)
        self.assertEqual(_add, -10.2)
    def testNegandPosNum(self):
        """@brief Scitanie negtivnych a kladnych cisel
        """
        a, b = 4.00, -6.20
        _add = add(a, b)
        self.assertEqual(_add, -2.2)


class TestSub(unittest.TestCase):
    def testM(test):
        x, y = 2.50, 3.50
        _sub = sub(x, y)
        test.assertEqual(_sub, -1.0)

    def testN(test):
        x, y = 4.0, -2.0
        _sub = sub(x, y)
        test.assertEqual(_sub, 6.0)

    def null(test):
        x, y = 0.0, 0.0
        _sub = sub(x, y)
        test.assertEqual(_sub, 0.0)


class TestMul(unittest.TestCase):
    def testM(test):
        x, y = 2.0, 3.0
        _mul = mul(x, y)
        test.assertEqual(_mul, 6.0)

    def testN(test):
        x, y = -2.0, -3.0
        _mul = mul(x, y)
        test.assertEqual(_mul, 6.0)

    def testZero(test):
        x, y = 2.0, 0.0
        _mul = mul(x, y)
        test.assertEqual(_mul, 0.0)


class TestDiv(unittest.TestCase):
    def testD(test):
        x,y = 6.0,3.0
        _div = div(x,y)
        test.assertEqual(_div,2.0)
    def testN(test):
        x,y = -6.0,-3.0
        _div=div(x,y)
        test.assertEqual(_div,2.0)

    def testZeroDivision(self):
        x,y = 6.0, 0.0
        with self.assertRaises(MathLibException):
            div(x, y)

class TestFact(unittest.TestCase):
    def testF(test):
        x=5.00
        _fac=fac(x)
        test.assertEqual(_fac,120.00)
    def testZero(test):
        x=0.00
        _fac = fac(x)
        test.assertEqual(_fac, 1.00)

class TestPower(unittest.TestCase):
    def  testP(test):
        x,y=2.00,3.00
        _pow=pow(x,y)
        test.assertEqual(_pow,8.00)
    def testNeg(test):
        x,y =-2.00,3.00
        _pow=pow(x,y)
        test.assertEqual(_pow, -8.00)
    def testZero(test):
        x,y = 2.00,0.00
        _pow=pow(x,y)
        test.assertEqual(_pow, 1.00)
    def testOne(test):
        x,y= 2.00,1.00
        _pow = pow(x,y)
        test.assertEqual(_pow,2.00)

class TestRoot(unittest.TestCase):
    def testSqrt(test):
        x,y = 36,2
        _sqrt=root(x,y)
        test.assertEqual(_sqrt,6.00)
    def testThird(test):
        x,y = 8.00,3.00
        _root=root(x,y)
        test.assertEqual(_root, 2.00)
    def testNeg(test):
        x,y= -4.0,2.0
        with test.assertRaises(MathLibException):
            _root=root(x,y)
        
class TestPerc(unittest.TestCase):
    def testPositive(test):
        a = 200.0
        result = perc(a)
        test.assertEqual(result, 2.0)

    def testZero(test):
        a = 0.0
        result = perc(a)
        test.assertEqual(result, 0.0)

    def testNegative(test):
        a = -300.0
        result = perc(a)
        test.assertEqual(result, -3.0)

    def testFraction(test):
        a = 75.5
        result = perc(a)
        test.assertAlmostEqual(result, 0.755)

class TestMul(unittest.TestCase):
    def testM(test):
        x, y = 2.0, 3.0
        _mul = mul(x, y)
        test.assertEqual(_mul, 6.0)

    def testN(test):
        x, y = -2.0, -3.0
        _mul = mul(x, y)
        test.assertEqual(_mul, 6.0)

    def testZero(test):
        x, y = 2.0, 0.0
        _mul = mul(x, y)
        test.assertEqual(_mul, 0.0)


class TestDiv(unittest.TestCase):
    def testD(test):
        x,y = 6.0,3.0
        _div = div(x,y)
        test.assertEqual(_div,2.0)
    def testN(test):
        x,y = -6.0,-3.0
        _div=div(x,y)
        test.assertEqual(_div,2.0)

    def testZeroDivision(self):
        x,y = 6.0, 0.0
        with self.assertRaises(MathLibException):
            div(x, y)

class TestFact(unittest.TestCase):
    def testF(test):
        x=5.00
        _fac=fac(x)
        test.assertEqual(_fac,120.00)
    def testZero(test):
        x=0.00
        _fac = fac(x)
        test.assertEqual(_fac, 1.00)

class TestPower(unittest.TestCase):
    def  testP(test):
        x,y=2.00,3.00
        _pow=pow(x,y)
        test.assertEqual(_pow,8.00)
    def testNeg(test):
        x,y =-2.00,3.00
        _pow=pow(x,y)
        test.assertEqual(_pow, -8.00)
    def testZero(test):
        x,y = 2.00,0.00
        _pow=pow(x,y)
        test.assertEqual(_pow, 1.00)
    def testOne(test):
        x,y= 2.00,1.00
        _pow = pow(x,y)
        test.assertEqual(_pow,2.00)

class TestRoot(unittest.TestCase):
    def testSqrt(test):
        x,y = 36,2
        _sqrt=root(x,y)
        test.assertEqual(_sqrt,6.00)
    def testThird(test):
        x,y = 8.00,3.00
        _root=root(x,y)
        test.assertEqual(_root, 2.00)
    def testNeg(test):
        x,y= -4.0,2.0
        with test.assertRaises(MathLibException):
            _root=root(x,y)
        
class TestPerc(unittest.TestCase):
    def testPositive(test):
        a = 200.0
        result = perc(a)
        test.assertEqual(result, 2.0)

    def testZero(test):
        a = 0.0
        result = perc(a)
        test.assertEqual(result, 0.0)

    def testNegative(test):
        a = -300.0
        result = perc(a)
        test.assertEqual(result, -3.0)

    def testFraction(test):
        a = 75.5
        result = perc(a)
        test.assertAlmostEqual(result, 0.755)

    
class TestSub(unittest.TestCase):
     """@brief Testy funkcie minus
    """   
     def testMinus(self):
            """@brief funkcia na odciatanie dvoch kladnych cisel
        """
            a, b = 4.00, 2.50
            _sub = sub(a, b)
            self.assertEqual(_sub, 1.50)
     def testNegMinus(self):
            """@brief funkcia na odciatanie dvoch kladnych cisel
        """
            a, b = 4.00, -2.50
            _sub = sub(a, b)
            self.assertEqual(_sub, 6.50)
class TestDiv(unittest.TestCase):
     """@brief Testy funkcie minus
    """   
     def testDiv(self):
        """@brief funkcia na delenie dvoch kladnych cisel
        """
        a,b = 4.00, 2.00
        _div = div(a, b)
        self.assertEqual(_div, 2.00)
     def testDiv(self):
        """@brief funkcia na odciatanie dvoch zapornych cisel
        """
        a,b = -4.00, -2.00
        _div = div(a, b)
        self.assertEqual(_div, 2.00)
     def testDiv(self):
        """@brief funkcia na odciatanie kladnych a zapornych cisel
        """
        a,b = -4.00, 2.00
        _div = div(a, b)
        self.assertEqual(_div, -2.00)
class TestMul(unittest.TestCase):
    """@brief Testy funkcie minus
    """
    def testMul(self):
        """@brief funkcia na nasobenie dvoch kladnych cisel
        """
        a,b = 2.00, 4.00
        _mul = mul(a, b)
        self.assertEqual(_mul, 8)
    def testMul(self):
        """@brief funkcia na nasobenie dvoch zapornych cisel
        """
        a,b = -2.00, -4.00
        _mul = mul(a, b)
        self.assertEqual(_mul, 8)
    def testMul(self):
        """@brief funkcia na nasobenie zapornych a kladnych cisel
        """
        a,b = -2.00, 4.00
        _mul = mul(a, b)
        self.assertEqual(_mul, -8)
     
class TestPower(unittest.TestCase):
    """@brief Testy funkcie power
    """
    def testIntegers(self):
        """@brief Umocnenie celeho cisla na cele cislo
        """
        a, p = 5.00, 2.00
        _power = power(a, p)
        self.assertEqual(_power, 25.00)
class TestRoot(unittest.TestCase):
    """@brief Testy funkcie root
    """
    def testSqrt(self):
        """@brief Druha odmocnenina kladneho celeho cisla
        """
        a, p = 64, 2
        _sqrt = root(a, p)
        self.assertEqual(_sqrt, 8.00)
    def testThirdRoot(self):
        """@brief Odmocnenie celeho cisla na tretiu
        """
        a, p = 125.00, 3.00
        _3rdRoot = root(a, p)
        self.assertEqual(_3rdRoot, 5.00)
class TestPercent(unittest.TestCase):
    """@brief Testy funkcie percento
    """
    def testPer(self):
        """@brief percento z cisla
        """        
        a = 120
        _perc = perc(a)
        self.assertEqual(_perc, 1.2)
    
class TestFac(unittest.TestCase):
    """@brief Testy funkcie factorialu
    """
    def testFactorial(self):
         """@brief faktorial cisla
        """
         a = 5.00
         _fac = fac(a)
         self.assertEqual(_fac, 120)

if __name__ == '__main__':
    unittest.main()