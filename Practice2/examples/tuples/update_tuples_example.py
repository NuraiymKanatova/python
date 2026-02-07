fruits = ("apple", "banana", "cherry")
print("Original tuple:")
print(fruits)

# tuples can not be changed - it would cause an error
# способы апдэйта tuple
# 1) we need to convert tuple to list, then back
temp_list = list(fruits)  # преобразуем tuple в лист - temp_list он изменяемый
temp_list[1] = "orange"  # меняем второй элемент списка, это возможно потому что это лист
fruits = tuple(temp_list)  # преобразуем обратно с листа в tuple и так создается новый tuple
print("\nAfter converting to list and back:")
print(fruits)

# 2) add item by creating a new tuple
fruits = fruits + ("kiwi",) # создаем новый и тогда старый уже не нужный
print("\nAFter adding an item:")
print(fruits)

# 3) remove item by converting to list
temp_list = list(fruits)
temp_list.remove("orange")
fruits = tuple(temp_list)
print("\nAfter removing an item:")
print(fruits)

