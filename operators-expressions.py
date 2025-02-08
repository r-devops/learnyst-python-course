# Assignment Operators

x = 10


# Arithmetic Operators:

a = 5
b = 3
result = a + b
print(result)

result = a - b
print(result)  # Output: 2

result = a * b
print(result)  # Output: 15

result = a / b
print(result)  # Output: 1.6666666666666667

result = a // b
print(result)

result = a ** b
print(result)


# Compound Assignments (+=, -=, *=, /=, //=, %=, **=)
y = 10 
y += a # y = y + a 
print(y)


# Comparison Operators

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Bitwise Operators

print(a & b)  # Output: 1 (binary: 101 & 011 = 001)
print(a | b)  # Output: 7 (binary: 101 | 011 = 111)
print(a ^ b)  # Output: 6 (binary: 101 ^ 011 = 110)
print(~a)  # Output: -6 (binary: ~101 = 010, in two's complement: 110)
print(a << 1)  # Output: 10 (binary:


# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)


# Identity Operators

a = [1, 2, 3]
b = a
print(a is b)

c = [1, 2, 3]
print(a is not c) 

# Logical Operators

a=10
b=5
print(a > 0 and b > 0)
print(a > 0 or b < 0)
print(not(a > 0))


