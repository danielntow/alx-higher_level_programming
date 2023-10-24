# Python Classes and Object-Oriented Programming (OOP)



## What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. OOP promotes code reusability, modularity, and the modeling of real-world entities in software.

## Python Classes

In Python, a class is a blueprint for creating objects.
classes include:

- **Attributes:** Class variables that store data.
- **Methods:** Functions that define the behavior of the class.
- **Constructor:** The `__init__` method initializes object attributes.
- **Encapsulation:** Controlling access to class members (public, private, protected).
- **Inheritance:** Creating new classes by inheriting attributes and methods from existing ones.
- **Polymorphism:** Objects of different classes can be used interchangeably.

### Example:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) barks!")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
