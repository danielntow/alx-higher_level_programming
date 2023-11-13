# Rectangle and Square Project

This Python project consists of three classes - Base, Rectangle, and Square. These classes are designed to manage rectangles and squares, providing functionality for serialization, deserialization, and manipulation.

## Base Class

The `Base` class serves as the foundation, providing core methods for working with objects. It includes features for converting objects to JSON and CSV formats, saving to and loading from files, and creating objects from dictionaries.

## Rectangle Class

The `Rectangle` class inherits from `Base` and represents rectangles. It includes methods for calculating area, displaying the rectangle, updating attributes, and converting to a dictionary.

## Square Class

The `Square` class inherits from `Rectangle` and represents squares. It shares methods with `Rectangle` and includes specific methods for updating and converting to a dictionary.

## Usage

To use these classes, create instances of `Rectangle` or `Square`, manipulate their attributes, and save/load them to/from files.

### Examples

```python
# Example usage of Rectangle
rectangle_instance = Rectangle(4, 5, 1, 2, 3)
print(rectangle_instance.area())  # Output: 20

# Example usage of Square
square_instance = Square(3, 1, 1, 4)
print(square_instance.size)  # Output: 3
