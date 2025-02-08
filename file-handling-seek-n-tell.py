with open("example.txt", "r+") as file:
    file.write("Hello, World!")
    file.seek(0)  # Move to the beginning of the file
    print(file.tell())  # Output: 0
    content = file.read()
    print(content)  # Output: Hello, World!


import os
import shutil

# Rename a file
os.rename("example.txt", "renamed_example.txt")

# Remove a file
#os.remove("renamed_example.txt")

# Copy a file
shutil.copy("renamed_example.txt", "destination.txt")

