# Basic Syntax

def greet():
    print("Hello, welcome to Python functions!")

# Call Function 
greet()

# With Parameter 
def greet(name):
    print(f"Hello, {name}! Welcome to Python functions.")

greet("Alice")
greet("Bob")


# Types of Arguments 

# 1. Positional Arguments
 
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("John", "Doe")

# 2. Keyword Arguments

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=30, name="Alice")

# 3. Default Parameters

def register_user(country="USA"):
    print(f"User registered from {country}")

register_user("Canada")
register_user()

# 4. Variable-Length Arguments (**args , **kwargs)

def print_students(*args, **kwargs):
    for student in args:
        print(f"Student: {student}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_students("Alice", "Bob", class_name="Math 101", teacher="Mr. Smith")




