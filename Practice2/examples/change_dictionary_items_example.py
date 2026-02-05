car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

print("Original dictionary:")
print(car)

# 1) change value by key
car["year"] = 2024
print("\nAfter changing year:")
print(car)

# 2) update multiple items using update()
car.update({
    "model": "Focus",
    "color": "red"
})
print("\nAfter update()")
print(car)

# 3) change value only if key exists
if "brand" in car:
    car["brand"] = "BMW"
print("\nAfter conditional change:")
print(car)