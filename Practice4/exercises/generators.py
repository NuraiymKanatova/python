# Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

n = int(input())

for value in square_generator(n):
    print(value)



# Write a program using generator to print the even numbers 
# between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

print(",".join(str(num) for num in even_numbers(n)))



# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.
def divisible(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

n = int(input())

for num in divisible(n):
    print(num)



# Implement a generator called squares to yield the square of all numbers 
# from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for value in squares(a, b):
    print(value)



# Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for number in countdown(n):
    print(number)