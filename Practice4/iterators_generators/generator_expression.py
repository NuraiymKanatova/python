# generator expressions are a concise way to create generators
# they are similar to list comprehensions but use () instead of [] and are more efficient

sq = (x*x for x in range(1, 6)) # range of 1 to 6 (exclusive)
for i in sq:
    print(i)
# output: 
# 1 
# 4 
# 9 
# 16 
# 25