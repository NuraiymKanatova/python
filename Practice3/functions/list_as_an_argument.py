# you can send any data type as an argument to a function 
# either string, number, list, dictionary, etc.


# sending a list as an argument
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# sending a dictionary as an argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)