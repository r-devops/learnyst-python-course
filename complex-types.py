
# lists 
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("cherry")
print(fruits)
fruits[1]="Berry"
print(fruits)
del fruits[2]
print(fruits)


# Tuples 
dimensions = (800,900)
#dimensions[2] = 200 # Not possible on tuple 

# Dictionaries 

person = {"name": "Alice", "age": 30, "city": "New York"}
person["age"] = 31  # Updating an existing key-value pair
person["profession"] = "Engineer"  # Adding a new key-value pair 
del person["city"]  # Removing a key-value pair


# Sets 
colors = {"red", "green", "blue"}
colors.add("yellow")  # Adding an element
colors.remove("green")  # Removing an element

unique_colors = set(["red", "red", "blue", "green", "green", "yellow"])
print(unique_colors)
