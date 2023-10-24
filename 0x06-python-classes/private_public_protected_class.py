class MyClass:
    def __init__(self):
        self.public_variable = 42

    def public_method(self):
        return "This is a public method"


obj = MyClass()
print(obj.public_variable)  # Accessing the public attribute
print(obj.public_method())  # Calling the public method


class MyClass:
    def __init__(self):
        self._protected_variable = 42

    def _protected_method(self):
        return "This is a protected method"


obj = MyClass()
print(obj._protected_variable)  # Accessing the protected attribute
print(obj._protected_method())  # Calling the protected method


class MyClass:
    def __init__(self):
        self.__private_variable = 42

    def __private_method(self):
        return "This is a private method"


obj = MyClass()
# Accessing the name-mangled private attribute
print(obj._MyClass__private_variable)
# Calling the name-mangled private method
print(obj._MyClass__private_method())
