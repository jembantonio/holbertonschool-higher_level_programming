#!/usr/bin/python3
''' class Rectangle unittest module
'''
import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        Base._Base__nb_objects = 0
    
    def test_values(self):
        self.assertTrue(issubclass(Rectangle, Base))
        r1 = Rectangle(1, 2, 0, 0, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
 
    def test_errors_typewidth(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle("not", 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle([1], 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle(1.14, 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle((1, ), 2)

    def test_errors_typeheight(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, "not")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, [2])
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, 2.14)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(1, (2, ))

    def test_errors_typex(self):
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
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r3 = Rectangle(-1, 2)
    def test_errors_valueheight(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r3 = Rectangle(1, -2)
    def test_errors_valuex(self):
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r3 = Rectangle(1, 2, -3)
    def test_errors_valuey(self):
        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            r3 = Rectangle(1, 2, 3, -4)

    def test_area(self):
        r0 = Rectangle(6, 2)
        self.assertEqual(r0.area(), 12)
        r1 = Rectangle(2, 12)
        self.assertEqual(r1.area(), 24)

    def test_area_id(self):
        r2 = Rectangle(2, 4, 0, 0, 1)
        self.assertEqual(r2.area(), 8)
        self.assertEqual(r2.id, 1)

    def test_print1(self):
        output_1 = io.StringIO()
        sys.stdout = output_1
        r0 = Rectangle(2, 3)
        a_expected_output = ""##\n##\n##\n""
        self.assertEqual(a_expected_output, output_1.getvalue())

    def test_print2(self):
        output_2 = io.StringIO()
        sys.stdout = output_2
        r1 = Rectangle(5, 3)
        b_expected_output = ""#####\n#####\n#####""
        self.assertEqual(b_expected_output, output_2.getvalue())

    def test_update_id(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99)
        self.assertEqual(r0.id, 99)
    def test_update_width(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98)
        self.assertEqual(r0.width, 98)
    def test_update_height(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97)
        self.assertEqual(r0.height, 97)
    def test_update_x(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97, 96)
        self.assertEqual(r0.x, 96)
    def test_update_y(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97, 96, 95)
        self.assertEqual(r0.y, 95)
    def test_update_extended(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99, 98, 97, 96, 95, 1, 2, 3, 4, 5)
        self.assertEqual(r0.y, 95)
    def test_update_skip(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(91, 98, 97)
        self.assertEqual(r0.height, 97)

    def test_update_kwarg(self):
        r0 = Rectangle(1, 2, 10)
        r0.update(99, x=98)
        self.assertEqual(r0.id, 99)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.x, 10)
