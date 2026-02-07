fruits = ["apple", "banana", "cherry", "orange"]

print("Original list:")
print(fruits)

# change a single item by index
fruits[1] = "kiwi"
print("\nAfter changing one item:")
print(fruits)

# change a range of items
fruits[1:3] = ["melon", "watermelon"]
print("\nAfter changing a range of items:")
print(fruits)

# change range with different length
fruits[1:3] = ["mango"]
print("\nAfter replacing range with fewer items:")
print(fruits)

# change using negative index
fruits[-1] = "pineapple"
print("\nAfter changing last item:")
print(fruits)