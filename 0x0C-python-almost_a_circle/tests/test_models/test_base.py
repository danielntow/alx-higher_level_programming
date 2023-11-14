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


if __name__ == '__main__':
    unittest.main()
