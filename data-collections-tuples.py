my_tuple = (10, "Python", 3.14)
print(my_tuple[1])

# Tuple Operations

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
repeated_tuple = tuple1 * 2 

print(combined_tuple)
print(repeated_tuple)

# Tuple Unpacking

coordinates = (10, 20)
x, y = coordinates
print(f"x: {x}, y: {y}")

# Immutable Nature of Tuples

my_tuple = (1, 2, 3)
my_tuple[1] = 5

