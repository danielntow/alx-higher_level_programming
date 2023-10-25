#!/usr/bin/python3
"""
This is a module for defining a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int, optional): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (float or int): The size of the square.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparator for comparing square areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparator for comparing square areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparator for comparing square areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal comparator for comparing square areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than comparator for comparing square areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal comparator for comparing square areas.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.area() <= other.area()


# Example usage:
if __name__ == "__main__":
    square1 = Square(4)
    square2 = Square(5)
    print(square1 == square2)  # False
    print(square1 != square2)  # True
    print(square1 > square2)   # False
    print(square1 >= square2)  # False
    print(square1 < square2)   # True
    print(square1 <= square2)  # True
