my_list = [10, "Python", 3.14]
print(my_list[1])

#Lists support various operations such as adding, removing, and modifying elements. Common methods include append(), remove(), pop(), and insert().

colors = ["red", "green", "blue"]
print(colors)

colors.append("yellow")
print(colors)

colors.remove("green")
print(colors)

colors.insert(1, "purple")
print(colors)

last_color = colors.pop()
print(colors)

print(last_color)


# List Slicing 

numbers = [0, 1, 2, 3, 4, 5]
sub_list = numbers[1:5:2]
print(sub_list)


# List Comprehensions

# Syntax : [expression for item in iterable if condition]
squares = [x**2 for x in range(6) if x % 2 == 0]
print(squares)


# Nested Lists 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])
