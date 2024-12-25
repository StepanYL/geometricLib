import unittest
import rectangle
import square
import triangle
import circle
from math import *
pi = acos(-1)
eps = pow(10, -9)

class CircleTester(unittest.TestCase):
    def testPerimeterZero(self):
        check = circle.perimeter(0)
        self.assertEqual(check, 0)
    def testPerimeterOne(self):
        check = circle.perimeter(1)
        self.assertEqual(check, 2 * pi)
    def testPetimeterSum(self):
        check1 = circle.perimeter(1)
        check2 = circle.perimeter(2)
        check3 = circle.perimeter(3)
        self.assertEqual(check3, check2 + check1)
    def testPerimeterPrecision(self):
        check1 = circle.perimeter(5)
        check2 = circle.perimeter(5 + eps)
        self.assertNotEqual(check1, check2)
    def testAreaZero(self):
        check = circle.area(0)
        self.assertEqual(check, 0)
    def testAreaPrecision(self):
        check1 = circle.area(5)
        check2 = circle.area(5.000001)
        self.assertNotEqual(check1, check2)
    def testAreaRough(self):
        check3 = circle.area(3)
        self.assertEqual(check3, 9 * pi)
        check4 = circle.area(4)
        self.assertEqual(check4, 16 * pi)
        check5 = circle.area(5)
        self.assertEqual(check5, 25 * pi)
        self.assertEqual(check5, check3 + check4)
    def testAreaBigValue(self):
        check = circle.area(10000000000)
        self.assertEqual(check, 100000000000000000000 * pi)

class TriangleTester(unittest.TestCase):
    def testPerimeterZero(self):
        check = triangle.perimeter(0, 0, 0)
        self.assertEqual(check, 0)
    def checkPerimeterFloat(self):
        check = triangle.perimeter(1.5, 2.5, 3.5)
        self.assertEqual(check, 7.5)
    def testPerimeterRough(self):
        check = triangle.perimeter(3, 4, 5)
        self.assertEqual(check, 12)
    def testPerimeterPrecision(self):
        check1 = triangle.perimeter(3, 4, 5)
        check2 = triangle.perimeter(3 + eps, 4 - eps, 5 + eps)
        self.assertNotEqual(check1, check2)
        self.assertEqual(check2, 12 + eps)
    def checkPerimeterBigValues(self):
        check = triangle.perimeter(100000000000000000000, 150000000000000000000, 100000000000000000000)
        self.assertEqual(check, 350000000000000000000)
    def testAreaZero(self):
        check =triangle.area(5, 0)
        self.assertEqual(check, 0)
    def testAreaOne(self):
        check = triangle.area(1, 2)
        self.assertEqual(check, 1)
    def testAreaRough(self):
        check3 = triangle.area(3, 3)
        self.assertEqual(check3, 4.5)
        check4 = triangle.area(4, 4)
        self.assertEqual(check4, 8)
        check5 = triangle.area(5, 5)
        self.assertEqual(check5, 12.5)
        self.assertEqual(check5, check3 + check4)
    def testAreaPrecision(self):
        check1 = triangle.area(5, 5)
        check2 = triangle.area(5, 5 + eps)
        self.assertNotEqual(check1, check2)
    def testAreaBigValues(self):
        check = triangle.area(4294967296, 4294967296)
        self.assertEqual(check, 9223372036854775808)


class RectangleTester(unittest.TestCase):
    def testPerimeterRotation(self):
        check1 = rectangle.perimeter(15, 10)
        check2 = rectangle.perimeter(10, 15)
        self.assertEqual(check1, 50)
        self.assertEqual(check1, check2)
    def testPerimeterZero(self):
        check = rectangle.perimeter(0, 0)
        self.assertEqual(check, 0)
    def testPerimeterBigValues(self):
        check = rectangle.perimeter(4611686018427387904, 4611686018427387904)
        self.assertEqual(check, 18446744073709551616)
    def testPetimeterPrecision(self):
        check1 = rectangle.perimeter(3, 3)
        check2 = rectangle.perimeter(3, 3 + eps)
        self.assertNotEqual(check1, check2)
    def testAreaZero(self):
        check = rectangle.area(5, 0)
        self.assertEqual(check, 0)
    def checkAreaRotation(self):
        check1 = rectangle.area(5, 4)
        check2 = rectangle.area(4, 5)
        self.assertEqual(check1, check2)
    def testAreaFloat(self):
        check = rectangle.area(2.5, 2.5)
        self.assertEqual(check, 6.25)
    def testAreaPrecision(self):
        check1 = rectangle.area(2, 2)
        check2 = rectangle.area(2 + eps, 2)
        self.assertNotEqual(check1, check2)
    def testAreaFloatRotation(self):
        check1 = rectangle.area(1.5, 2.5)
        check2 = rectangle.area(2.5, 1.5)
        self.assertEqual(check1, 3.75)
        self.assertEqual(check1, check2)
    def testAreaBigValues(self):
        check = rectangle.area(10000000000, 10000000000)
        self.assertEqual(check, 100000000000000000000)
    def testAreaPythagorean(self):
        check3 = rectangle.area(3, 3)
        check4 = rectangle.area(4, 4)
        check5 = rectangle.area(5, 5)
        self.assertEqual(check5, check3 + check4)

class SquareTester(unittest.TestCase):
    def testPerimeterZero(self):
        check = square.perimeter(0)
        self.assertEqual(check, 0)
    def testPerimeterRough(self):
        check3 = square.perimeter(3)
        self.assertEqual(check3, 12)
        check4 = square.perimeter(4)
        self.assertEqual(check4, 16)
        check7 = square.perimeter(7)
        self.assertEqual(check7, 28)
        self.assertEqual(check7, check3 + check4)
    def testPerimeterPrecision(self):
        check1 = square.perimeter(5)
        check2 = square.perimeter(5 + eps)
        self.assertNotEqual(check1, check2)
    def testPerimeterBigValues(self):
        check1 = square.perimeter(4611686018427387904)
        self.assertEqual(check1, 18446744073709551616)
    def testAreaZero(self):
        check = square.area(0)
        self.assertEqual(check, 0)
    def testAreaOne(self):
        check = square.area(1)
        self.assertEqual(check, 1)
    def testAreaFloat(self):
        check = square.area(2.5)
        self.assertEqual(check, 6.25)
    def testAreaPrecision(self):
        check1 = square.area(5)
        check2 = square.area(5 + eps)
        self.assertNotEqual(check1, check2)
    def testAreaPythagorean(self):
        check3 = square.area(3)
        self.assertEqual(check3, 9)
        check4 = square.area(4)
        self.assertEqual(check4, 16)
        check5 = square.area(5)
        self.assertEqual(check5, 25)
        self.assertEqual(check5, check4 + check3)
    def testAreaBigValues(self):
        check1 = square.area(4294967296)
        self.assertEqual(18446744073709551616, check1)


