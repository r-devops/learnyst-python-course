# List Comprehensions

# Traditional way using a for loop
squares = []
for i in range(10):
    squares.append(i**2)

# Using list comprehension
squares_comp = [i**2 for i in range(10)]
print(squares_comp)


# Dictionary Comprehensions

# Traditional way using a for loop
squares_dict = {}
for i in range(5):
    squares_dict[i] = i**2

# Using dictionary comprehension
squares_dict_comp = {i: i**2 for i in range(5)}
print(squares_dict_comp)

# Set Comprehensions

# Traditional way using a for loop
unique_lengths = set()
for word in ["hello", "world", "python", "programming"]:
    unique_lengths.add(len(word))

# Using set comprehension
unique_lengths_comp = {len(word) for word in ["hello", "world", "python", "programming"]}
print(unique_lengths_comp)
