#absi/usr/bin/python3
''' base Class unitest module
'''
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    
    def test_none(self):
        b0 = Base(1)
        self.assertEqual(b0.id, 1)
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base(None)
        self.assertEqual(b3.id, 2)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_type(self):
        b0 = Base()
        self.assertEqual(b0.id, 5)
        b1 = Base("type")
        self.assertEqual(b1.id, "type")
        with self.assertRaises(TypeError):
            b2 = Base(1, 2)
