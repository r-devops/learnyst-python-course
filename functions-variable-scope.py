# Local vs. Global Variables

x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print("Inside the function, x =", x)
    print("Inside the function, y =", y)

my_function()
print("Outside the function, x =", x)
# print("Outside the function, y =", y)  # This would raise an error

# Modifying Global Variables in Functions

count = 0  # Global variable

def increment_count():
    global count
    count += 1
    print("Inside the function, count =", count)

increment_count()
print("Outside the function, count =", count)


