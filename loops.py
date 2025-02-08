# for loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")


# while loop 
count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1


# Loop Control Command - break 

numbers = [3, 5, 7, 9, -2, 8, 10]

for number in numbers:
    if number < 0:
        print(f"The first negative number is {number}.")
        break


# Loop Control Command - continue 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)
        continue



# Loop Control Command - else 

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
    break
else:
    print('I like all fruits')




