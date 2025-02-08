numbers = [5, 2, 9, 1, 7]
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))

# Membership testing 
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)
print("orange" not in fruits)

# Iterating Over Collections

for fruit in fruits:
    print(f"I love {fruit}")


# Comparing Collections

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]
print(list1 == list2)
print(list1 == list3)


#  Conversion Between Collection Types

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_set = set(my_list)
print(my_list)
print(my_set)
