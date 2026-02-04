# Умнжожение имеет больший приоритет чем сложение
print(2 + 3 * 4)      # 14

# Круглые скобки меняют порядок
print((2 + 3) * 4)    # 20

# Сравнение и арифметика
print(5 + 5 > 8)      # True

# Приоритет логических операторов
print(True or False and False)    # True
print((True or False) and False)  # False

# Комбинированный пример
x = 10
print(x > 5 and x < 20)    # True