# Docstrings (documentation strings) are multiline string literals used to document what a function (or module, class, or method) does. They are enclosed in triple quotes (""") and should provide a clear explanation of the function's purpose, parameters, return values, and any other relevant information. Docstrings are accessible at runtime using the help() function or the .__doc__ attribute.

# Example 

def calculate_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return 3.14159 * radius ** 2

print(calculate_area.__doc__)

help(calculate_area)
print(calculate_area.__doc__)


