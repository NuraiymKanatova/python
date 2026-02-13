# arbitary keyword arguments - *kwargs

# if you do not know how many keyword arguments will be passed 
# add two ** before thr paramenter name

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# using **kwargs with regular arguments
def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")