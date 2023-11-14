#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):

    def setUp(self):
        # Reset the Base class id counter before each test
        Base._Base__nb_objects = 0

    def test_create_instance(self):
        base = Base()
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 1)

    def test_create_instance_with_id(self):
        base = Base(5)
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 5)

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_non_empty_list(self):
        json_string = Base.to_json_string([{'id': 1, 'x': 2, 'y': 3}])
        self.assertEqual(json_string, '[{"id": 1, "x": 2, "y": 3}]')

    def test_load_from_file_empty(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_create_and_load_from_file(self):
        square1 = Square(5, 1, 2, 3)
        square2 = Square(8, 4, 5, 6)
        Square.save_to_file([square1, square2])

        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 2)

        loaded_square1 = loaded_squares[0]
        loaded_square2 = loaded_squares[1]

        self.assertEqual(loaded_square1.id, 3)
        self.assertEqual(loaded_square1.size, 5)
        self.assertEqual(loaded_square1.x, 1)
        self.assertEqual(loaded_square1.y, 2)

        self.assertEqual(loaded_square2.size, 8)
        self.assertEqual(loaded_square2.x, 4)
        self.assertEqual(loaded_square2.y, 5)

    def test_to_json_string_serialization(self):
        """
        Test JSON serialization.
        """
        Base._Base__nb_objects = 0
        input_shapes = [{"id": 1, "width": 2, "height": 3},
                        {"id": 2, "width": 4, "height": 5}]
        expected_output = '[{"id": 1, "width": 2, "height": 3}, {"id": 2, "width": 4, "height": 5}]'
        empty_list = []

        self.assertEqual(Base.to_json_string(input_shapes), expected_output)
        self.assertEqual(Base.to_json_string(empty_list), '[]')

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(type(input_shapes), list)
        with self.assertRaises(NameError):
            Base.to_json_string(input_shapes_3)

    def test_save_to_file_saving(self):
        """
        Test saving to file.
        """
        filename = "ModifiedRectangle.json"
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])

        loaded_rectangles = Rectangle.load_from_file()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(
            loaded_rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(
            loaded_rectangles[1].to_dictionary(), r2.to_dictionary())


if __name__ == '__main__':
    unittest.main()
