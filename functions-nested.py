# Nested Functions 

def outer_function(message):
    def inner_function():
        print(f"Message from the inner function: {message}")
    inner_function()

outer_function("Hello from the outer function!")


# Closures

def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
print(double(5))

# Partial Functions

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # Output: 16
print(cube(4))  # Output: 64

