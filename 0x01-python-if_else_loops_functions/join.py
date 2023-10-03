separator = " "
sequence = ["item1", "item2", "item3"]
result = separator.join(sequence)
print(result)


words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)
# Output: Hello World Python


characters = ["a", "b", "c", "d"]
string = "".join(characters)
print(string)
# Output: abcd


numbers = ["1", "2", "3", "4", "5"]
csv = ",".join(numbers)
print(csv)
# Output: 1,2,3,4,5


integers = [1, 2, 3, 4, 5]
result = "-".join(map(str, integers))
print(result)
# Output: 1-2-3-4-5


lines = ["Line 1", "Line 2", "Line 3"]
multiline_text = "\n".join(lines)
print(multiline_text)
# Output:
# Line 1
# Line 2
# Line 3


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = " | ".join(" ".join(map(str, row)) for row in matrix)
print(flattened)
# Output: 1 2 3 | 4 5 6 | 7 8 9


path = ["home", "user", "documents", "file.txt"]
file_path = "/".join(path)
print(file_path)
# Output: home/user/documents/file.txt
