import math


class MagicClass:
    """
    A class that performs magic calculations based on the radius.

    Attributes:
        __radius (int or float): The radius used for calculations.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Args:
            radius (int or float, optional): The radius for calculations (default is 0).
        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of a circle using the provided radius.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of a circle using the provided radius.

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius
