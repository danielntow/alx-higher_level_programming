# Define a lambda function that squares its input
def square(x): return x ** 2


# Use the lambda function
result = square(5)
print(result)
# Output: 25


# Sorting a list of tuples based on the second element using lambda
points = [(2, 5), (1, 8), (3, 2)]
sorted_points = sorted(points, key=lambda point: point[1])

print(sorted_points)
# Output: [(3, 2), (2, 5), (1, 8)]


# Using lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
# Output: [2, 4, 6, 8, 10]

# Using lambda with map
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Sorting a list of strings by their lengths using lambda
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)
# Output: ['date', 'apple', 'cherry', 'banana']


# Creating a lambda function with multiple arguments
def add(x, y): return x + y


result = add(3, 5)
print(result)
# Output: 8

# Using lambda functions as arguments in the sorted() function
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda name: name[-1])

print(sorted_names)
# Output: ['Charlie', 'Alice', 'Bob', 'David']


# Using lambda functions in a dictionary
operation_dict = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
}

result = operation_dict["add"](3, 5)
print(result)
# Output: 8
