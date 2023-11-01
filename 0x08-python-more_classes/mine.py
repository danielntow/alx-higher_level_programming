#!/usr/bin/python3

class MyClass:
    def __init__(self):
        self.variable = 10

    def some_method(self):
        return "Hello, World!"


obj = MyClass()

# Accessing the object's __dict__
print(obj.__dict__)
# Output: {'variable': 10}

# Adding a new attribute dynamically
obj.new_variable = 20

# Accessing the updated __dict__
print(obj.__dict__)
# Output: {'variable': 10, 'new_variable': 20}


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Creating an instance of the Book class
book1 = Book("Python for Beginners", "John Doe")

# Printing the object using str()
print(str(book1))  # Output: Book: Python for Beginners by John Doe

# Printing the object directly
print(book1)       # Output: Book: Python for Beginners by John Doe


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Creating an instance of the Point class
p1 = Point(5, 10)

# Using repr() function
print(repr(p1))  # Output: Point(5, 10)
print('-----')
# Evaluating the object interactively
p1                 # Output: Point(5, 10)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"Coordinates: ({self.x}, {self.y})"


# Creating an instance of the Point class
point1 = Point(5, 10)

# Using str() and repr()
print(str(point1))   # Output (from __str__): Coordinates: (5, 10)
print(repr(point1))  # Output (from __repr__): Point(5, 10)

print("see", point1)
# Displaying the object in the Python interpreter
point1               # Output (from __repr__): Point(5, 10)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing attributes using getattr()
name = getattr(person, 'name')
age = getattr(person, 'age')
city = getattr(person, 'city', 'Unknown')

print(name)  # Output: Alice
print(age)   # Output: 30
print(city)  # Output (default value): Unknown
