# Function Annotations

def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

def calculate_area(radius: float) -> float:
    return 3.14159 * radius ** 2

print(calculate_area.__annotations__)
print(calculate_area(5))


