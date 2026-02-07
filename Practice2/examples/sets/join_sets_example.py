set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# union() - returns a new set
set3 = set1.union(set2)
print("Union using union():")
print(set3)

# | operator - also returns a new set
set4 = set1 | set2
print("\nUnion using | operator:")
print(set4)

# update() - adds elements into set1
set1.update(set2)
print("\nAfter update():")
print(set1)

# original set2 is unchanged
print("\nOriginal set2:")
print(set2) 