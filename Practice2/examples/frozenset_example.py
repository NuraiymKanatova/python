numbers = [1, 2, 3, 3, 4]
frozen = frozenset(numbers)
print(frozen)

# membership check
print(2 in frozen)  # True

# frozenset is immutable (cannot be changed)
# frozen.add(5)     # error
# frozen.remove(1)  # error