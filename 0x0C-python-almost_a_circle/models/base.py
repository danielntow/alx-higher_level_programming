#!/usr/bin/python3
"""This module defines a base class and subclasses
for squares.
"""
import json
import csv
import turtle


class Base:
    """Base class for object serialization and deserialization."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id: An integer representing the id. If None,
            it auto-increments __nb_objects.

        Attributes:
            id: A public instance attribute representing the object's id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: List of dictionaries.

        Returns:
            JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs: List of instances.

        Note:
            If list_objs is None, save an empty list.
            The filename must be: <Class name>.json.
            You must use the static method to_json_string.
            You must overwrite the file if it already exists.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def save_to_my_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs: List of instances.

        Note:
            If list_objs is None, save an empty list.
            The filename must be: <Class name>.json.
            You must use the static method to_json_string.
            You must overwrite the file if it already exists.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            json.dump([obj.to_dictionary() for obj in list_objs], file)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of instances represented by json_string.

        Args:
            json_string: String representing a list of dictionaries.

        Returns:
            List of instances represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set
        based on the provided dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance with attributes set based on the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            # Creating a dummy Rectangle instance with dummy mandatory -
            # attributes
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            # Creating a dummy Square instance with dummy mandatory-
            # attributes
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()  # Creating a generic dummy
            # instance

        # Applying real values using the update method
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file in JSON format."""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                return [cls.create(**data) for data in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_my_file(cls):
        """
        Returns a list of instances based on the content
        of the <Class name>.json file.

        Returns:
            List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                dictionaries_list = cls.from_json_string(content)
                return [cls.create(
                    **dictionary
                ) for dictionary in dictionaries_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV representation of list_objs to a file.

        Args:
            list_objs: List of instances.

        Note:
            If list_objs is None, save an empty list.
            The filename must be: <Class name>.csv.
        """
        list_objs = [] if list_objs is None else list_objs
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csvs(cls):
        """
        Returns a list of instances based on the content of the
        <Class name>.csv file.

        Returns:
            List of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        attributes = list(map(int, row))
                        instance = cls(*attributes[1:])
                    elif cls.__name__ == "Square":
                        attributes = list(map(int, row))
                        instance = cls(attributes[1])
                    instances_list.append(instance)
                return instances_list
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize from CSV format and return a list of instances."""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = cls(int(row[0]), int(row[1]), int(
                        row[2]), int(row[3]), int(row[4]))
                elif cls.__name__ == "Square":
                    instance = cls(int(row[0]), int(
                        row[1]), int(row[2]), int(row[3]))
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares-
        using Turtle graphics.

        Args:
            list_rectangles: List of Rectangle instances.
            list_squares: List of Square instances.
        """
        # Create a turtle screen
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        # Create a turtle for drawing
        drawer = turtle.Turtle()

        # Function to draw a rectangle
        def draw_rectangle(rectangle):
            drawer.penup()
            drawer.goto(rectangle.x, rectangle.y)
            drawer.pendown()
            drawer.forward(rectangle.width)
            drawer.left(90)
            drawer.forward(rectangle.height)
            drawer.left(90)
            drawer.forward(rectangle.width)
            drawer.left(90)
            drawer.forward(rectangle.height)
            drawer.left(90)

        # Function to draw a square
        def draw_square(square):
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)

        # Draw all rectangles
        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        # Draw all squares
        for square in list_squares:
            draw_square(square)

        # Close the window on click
        screen.exitonclick()
