# Sets 
my_set = {1, 2, 3, 2}
print(my_set)


set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b

print(union_set)
print(intersection_set)
print(difference_set)


squared_set = {x**2 for x in range(5)}
print(squared_set)


immutable_set = frozenset([1, 2, 3])
#immutable_set.add(4)  # This would raise an AttributeError
