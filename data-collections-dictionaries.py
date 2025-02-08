my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])

# Dictionary Operations

person = {"name": "Bob", "age": 25}
print(person)

person["email"] = "bob@example.com"
print(person)

email = person.pop("email")
print(person)

print(email)

# Iterating Over Dictionaries

user = {"username": "john_doe", "status": "active", "role": "admin"}
for key, value in user.items():
    print(f"{key}: {value}")


# Nested Dictionaries
users = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}
print(users["user1"]["name"])


