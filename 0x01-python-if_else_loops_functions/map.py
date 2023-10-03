def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the map object to a list
result = list(squared_numbers)
print(result)
# Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

result = list(squared_numbers)
print(result)
# Output: [1, 4, 9, 16, 25]


def add(x, y):
    return x + y


list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = map(add, list1, list2)

result = list(sums)
print(result)
# Output: [5, 7, 9]


words = ["apple", "banana", "cherry"]
word_lengths = map(len, words)

result = list(word_lengths)
print(result)
# Output: [5, 6, 6]


def square(x):
    return x ** 2


numbers_set = {1, 2, 3, 4, 5}
squared_numbers = map(square, numbers_set)

# Convert the map object to a set
result_set = set(squared_numbers)
print(result_set)
# Output: {1, 4, 9, 16, 25}


text = "Hello, World!"
uppercase_text = map(str.upper, text)

result = ''.join(list(uppercase_text))
print(result)
# Output: "HELLO, WORLD!"
