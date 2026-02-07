student = {
    "name": "Anna",
    "age": 19
}
print("Original dictionary:")
print(student)

# 1) add item using new key
student["city"] = "Almaty"
print("\nAfter adding city:")
print(student)

# 2) add multiple items using update()
student.update({
    "major": "Computer Science",
    "year": 2
})
print("\nAfter update():")
print(student)

#3) add item only if key does not exist
if "gpa" not in student:
    student["gpa"] = 3.8
print("\nAfter conditional add:")
print(student)