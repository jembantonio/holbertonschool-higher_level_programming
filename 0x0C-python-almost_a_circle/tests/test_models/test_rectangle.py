#!/usr/bin/python3
''' class Rectangle unittest module
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' test class for class Rectangle '''
    def setUp(self):
        ''' setup method '''
        pass

    def tearDown(self):
        ''' teardown method '''
        Base._Base__nb_objects = 0

    def test_subclass(self):
        ''' testing subclass '''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_values(self):
        ''' test values '''
        r1 = Rectangle(1, 2, 0, 0, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_errors_typewidth(self):
        ''' raise error test failures '''
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle("not", 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle([1], 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle(1.14, 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle((1, ), 2)

    def test_errors_typeheight(self):
        ''' raise error test failures '''
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, "not")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, [2])
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, 2.14)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, (2, ))

    def test_errors_typex(self):
        ''' raise error test failures '''
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r2 = Rectangle(1, 2, "not")
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r2 = Rectangle(1, 2, [2])
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r2 = Rectangle(1, 2, 3.14)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r2 = Rectangle(1, 2, (3, ))

    def test_errors_typey(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r2 = Rectangle(1, 2, 3, "not")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r2 = Rectangle(1, 2, 3, [4])
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r2 = Rectangle(1, 2, 3, 4.14)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r2 = Rectangle(1, 2, 3, (4, ))

    def test_errors_valuewidth(self):
        ''' raise error test failures '''
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r3 = Rectangle(-1, 2)

    def test_errors_valueheight(self):
        ''' raise error test failures '''
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r3 = Rectangle(1, -2)

    def test_errors_valuex(self):
        ''' raise error test failures '''
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r3 = Rectangle(1, 2, -3)

    def test_errors_valuey(self):
        ''' raise error test failures '''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r3 = Rectangle(1, 2, 3, -4)

    def test_area(self):
        ''' area method test '''
        r0 = Rectangle(6, 2)
        self.assertEqual(r0.area(), 12)
        r1 = Rectangle(2, 12)
        self.assertEqual(r1.area(), 24)

    def test_area_id(self):
        ''' area method test '''
        r2 = Rectangle(2, 4, 0, 0, 1)
        self.assertEqual(r2.area(), 8)
        self.assertEqual(r2.id, 1)

    def test_update_id(self):
        ''' update id test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99)
        self.assertEqual(r0.id, 99)

    def test_update_width(self):
        ''' update width test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98)
        self.assertEqual(r0.width, 98)

    def test_update_height(self):
        ''' update height test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97)
        self.assertEqual(r0.height, 97)

    def test_update_x(self):
        ''' update x test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97, 96)
        self.assertEqual(r0.x, 96)

    def test_update_y(self):
        ''' update y test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97, 96, 95)
        self.assertEqual(r0.y, 95)

    def test_update_extended(self):
        ''' update key test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97, 96, 95, 1, 2, 3, 4, 5)
        self.assertEqual(r0.y, 95)

    def test_update_skip(self):
        ''' update skip test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(91, 98, 97)
        self.assertEqual(r0.height, 97)

    def test_update_kwarg(self):
        ''' update key test '''
        r0 = Rectangle(1, 2, 10)
        r0.update(99, x=98)
        self.assertEqual(r0.id, 99)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.x, 10)
