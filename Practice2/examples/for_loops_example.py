fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range() function - returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 by default
# and ends at specified number

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")