#!/usr/bin/python3
"""
totest file
"""

import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):

    def setUp(self):
        # Reset the counter before each test
        Square._Base__nb_objects = 0

    def test_create_instance(self):
        square_instance = Square(5)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 1)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 0)
        self.assertEqual(square_instance.y, 0)

    def test_to_dictionary(self):
        square = Square(4, 2, 3, 1)
        square_dict = square.to_dictionary()

        self.assertEqual(
            square_dict, {'height': 4, 'id': 1, 'width': 4, 'x': 2, 'y': 3})

    def test_update(self):
        square = Square(3, 1, 1, 1)
        square.update(2, 5, 2, 2)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_str_representation(self):
        square = Square(3, 1, 1, 1)
        str_representation = str(square)

        self.assertEqual(str_representation, "[Square] (1) 1/1 - 3")

    def test_size_getter_and_setter(self):
        square = Square(3)
        square.size = 6

        self.assertEqual(square.size, 6)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_load_from_file_csv(self):
        square1 = Square(5, 1, 2, 3)
        square2 = Square(8, 4, 5, 6)
        Square.save_to_file_csv([square1, square2])

        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_squares), 2)

        loaded_square1 = loaded_squares[0]
        loaded_square2 = loaded_squares[1]


if __name__ == '__main__':
    unittest.main()
