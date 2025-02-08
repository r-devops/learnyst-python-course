file = open("example.txt", "r")
content = file.read()
print(content)
file.close()


with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    print("Done")

# Reading line by line 
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
        print("Done")

# Reading Specific Amount of Characters

with open("example.txt", "r") as file:
    chunk = file.read(10)  # Read the first 10 characters
    print(chunk)

with open("output.txt", "w") as file:
    file.write("Hello, World!")

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append the text
with open("output.txt", "a") as file:
    file.write("\nNew line appended to the file.")

# File paths

absolute_path="/root/python-scripts/output.txt"
relative_path="output.txt"


with open(absolute_path, "a") as file:
    file.write("\nOne more new line appended to the file.")

import os
dirname, basename = os.path.split(absolute_path)
print(dirname)
print(basename)


# Different Modes 
with open("example.txt", "w") as file:
    file.write("This file is created in write mode.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "a") as file:
    file.write("\nNew line appended.")

# Read Write mode 
with open("example.txt", "r+") as file:
    file.write("Modified in read/write mode.")
    file.seek(0)
    print(file.read())


# File exceptions 
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# Writing binary data to a file
with open("example.bin", "wb") as file:
    file.write(b'\x00\x01\x02\x03')

# # Reading binary data from a file

with open("example.bin", "rb") as file:
    content = file.read()
    print(content)

# Seeking and Tell

with open("example.txt", "r+") as file:
    file.write("Hello, World!")
    file.seek(0)  # Move to the beginning of the file
    print(file.tell())  # Output: 0
    content = file.read()
    print(content)  # Output: Hello, World!


