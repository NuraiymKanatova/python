# arguments are specified after the function name, inside the parentheses.
# you can add as many arguments as you want, just separate them

def my_function(fname):
    print(fname + " Refsnes")

my_function("Email")
my_function("Tobias")
my_function("Linus")
    
# when function is called, we pass along a first name, 
# which is used inside the function to print the full name



# a parameter is the variable listed inside the parentheses in the function definition
# an argument is the actual value that is sent to the function when it is called

def my_function(name):   # name is a parameter
    print("Hello", name)
my_function("Emil")      # "Emil" is an argument



# if the function is calles without an argument, it uses the default valu
def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()          # output will be 'Hello friend'
my_function("Linus")

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()         # output will be 'I am from Norway'
my_function("Brazil")