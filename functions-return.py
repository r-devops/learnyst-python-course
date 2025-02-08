# return in Python Function 

def add(a, b):
    result = a + b
    return result

sum = add(5, 3)
print(f"The sum is {sum}")

# return multiple values

def get_user_info():
    name = "Alice"
    age = 30
    email = "alice@example.com"
    return name, age, email

user_name, user_age, user_email = get_user_info()
print(f"Name: {user_name}, Age: {user_age}, Email: {user_email}")


