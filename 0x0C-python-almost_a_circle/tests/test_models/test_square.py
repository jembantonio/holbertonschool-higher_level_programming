#!/usr/bin/python3
''' class Square unittest module
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    ''' test class for class Square '''
    def setUp(self):
        ''' setup method '''
        pass

    def tearDown(self):
        ''' teardown method '''
        Base._Base__nb_object = 0

    def test_subclass(self):
        ''' test subclass method '''
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
