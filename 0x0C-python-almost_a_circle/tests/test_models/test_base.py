#!/usr/bin/python3
import unittest
from models.base import Base, Rectangle, Square


class TestBaseClass(unittest.TestCase):

    def test_create_instance(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)
        self.assertEqual(base_instance.id, 1)

    def test_to_json_string(self):
        rectangle = Rectangle(2, 3)
        square = Square(4)
        rectangles_json = Rectangle.to_json_string([rectangle.to_dictionary()])
        squares_json = Square.to_json_string([square.to_dictionary()])

        self.assertEqual(
            rectangles_json, '[{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]')
        self.assertEqual(
            squares_json, '[{"id": 2, "size": 4, "x": 0, "y": 0}]')

    def test_load_from_file_csv(self):
        square1 = Square(5, 1, 2, 3)
        square2 = Square(8, 4, 5, 6)
        Square.save_to_file_csv([square1, square2])

        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(len(loaded_squares), 2)

        loaded_square1 = loaded_squares[0]
        loaded_square2 = loaded_squares[1]

        self.assertEqual(loaded_square1.id, 3)
        self.assertEqual(loaded_square1.size, 5)
        self.assertEqual(loaded_square1.x, 1)
        self.assertEqual(loaded_square1.y, 2)

        self.assertEqual(loaded_square2.id, 4)
        self.assertEqual(loaded_square2.size, 8)
        self.assertEqual(loaded_square2.x, 4)
        self.assertEqual(loaded_square2.y, 5)


if __name__ == '__main__':
    unittest.main()
