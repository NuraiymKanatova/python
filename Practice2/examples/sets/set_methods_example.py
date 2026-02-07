set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("set_a:", set_a)
print("set_b:", set_b)

# intersection() - common elements (new set)
common = set_a.intersection(set_b)
print("\nintersection():")
print(common)

# intersection_update() - modifies set_a
temp = set_a.copy()
temp.intersection_update(set_b)
print("\nintersection_update():")
print(temp)

# difference() - elements in set_a but not in set_b
diff = set_a.difference(set_b)
print("\ndifference():")
print(diff)

# difference_update() - modifies set_a
temp = set_a.copy()
temp.difference_update(set_b)
print("\ndifference_update():")
print(temp)

# symmetric_difference() - elements in either set, but not both
sym_diff = set_a.symmetric_difference(set_b)
print("\nsymmetric_difference():")
print(sym_diff)

# symmetric_difference_update() - modifies set_a
temp = set_a.copy()
temp.symmetric_difference_update(set_b)
print("\nsymmetric_difference_update():")
print(temp)

# issubseet() - check if set is subset
small = {1, 2}
print("\nissubset():")
print(small.issubset(set_a))      # True

# issuperset() - check if set contains another set
print("\nissuperset():")
print(set_a.issuperset(small))    # True

# isdisjoint() - check if no common elements
print("\nisdisjoint():")
print(set_a.isdisjoint({10, 20})) # True