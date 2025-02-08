single_quote_string = 'Hello, Python!'
double_quote_string = "Hello, Python!"

print(single_quote_string)
print(double_quote_string)

multiline_string = """This is a
multiline
string."""

print(multiline_string)


quote_string = "She said, 'Hello, Python!'"
print(quote_string) 


greeting = "Hello, World!"
first_char = greeting[0]
print(f"First character: {first_char}")
last_char = greeting[-1]
print(f"Last character: {last_char}")

# Slicing Strings
substring = greeting[7:12]
print(f"Substring: {substring}")   


reverse_string = greeting[::-1]
print(f"Reversed string: {reverse_string}")

every_second_char = greeting[::2]
print(f"Every second character: {every_second_char}")

# String Concatenation 
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Repetition
repeat_str = "Hello! " * 3
print(repeat_str)

# Length 
message = "Hello, World!"
length = len(message)
print(f"The length of the string is {length}")

# Case Conversion
text = "Hello, Python!"
print(text.upper()) 
print(text.lower())
print(text.title())
print(text.capitalize())

# Searching and Replacing
sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.find("fox"))
print(sentence.index("jumps"))
print(sentence.replace("lazy", "energetic"))
print(sentence.count("o"))


# Splitting and Joining
words = "one,two,three"
word_list = words.split(",")
print(word_list)  

joined_words = "-".join(word_list)
print(joined_words)

# Stripping Whitespace
padded_string = "   Hello, World!   "
print(padded_string)
print(padded_string.strip())
print(padded_string.lstrip())
print(padded_string.rstrip())

# % Formatting 
name = "John"
age = 30
formatted_string = "My name is %s, and I am %d years old." % (name, age)
print(formatted_string)


name = "Alice"
age = 25
formatted_string = "My name is {}, and I am {} years old.".format(name, age)
print(formatted_string)

# Formatted String Literals (f-strings)

name = "Bob"
age = 28
formatted_string = f"My name is {name}, and I am {age} years old."
print(formatted_string)



# Escape Sequences

escaped_string = "This is a \"quoted\" word.\nAnd this is on a new line.\tAnd this is tabbed."
print(escaped_string)

# String Immutability

greeting = "Hello, World!"
# greeting[0] = "J" # This is not possible

# Modifying Strings Despite Immutability

original_string = "Hello"
modified_string = original_string + ", World!"
print(modified_string)



