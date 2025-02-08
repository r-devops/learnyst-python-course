# Builtin Modules 

import math

num = 25
sqrt_value = math.sqrt(num)
print(f"Square root of {num} is {sqrt_value}")

print("----------------------------------------------------")
print("----------------------------------------------------")

import os

files = os.listdir(".")  
print("Files in current directory:", files)

print("----------------------------------------------------")
print("----------------------------------------------------")

import sys

print("Python version:", sys.version)


print("----------------------------------------------------")
print("----------------------------------------------------")

import datetime

current_time = datetime.datetime.now()
print("Current date and time:", current_time)

