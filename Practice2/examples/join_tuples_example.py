tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

joined = tuple1 + tuple2
print(joined)

tuple3 = ("x", "y")
result = tuple1 + tuple2 + tuple3
print(result)

# repeat tuples 
numbers = (5, 6)
repeated = numbers * 3
print(repeated)

# original tuples are not changed
print(tuple1)
print(numbers) 