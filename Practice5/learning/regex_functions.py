# the re module offers a set of functions that allows us to search a string for a match


# findall() - найти все совпадения
import re

text = "My numbers are 12, 45 and 789"
result = re.findall(r"\d+", text)   # \d+ означает одну или больше цифр

print(result)                       # результат: ['12', '45', '789']



# search() - найти первое совпадение
import re

text = "Contact: example@gmail.com"
result = re.search(r"\w+@\w+.\w+", text)   # search() возвращает match объект
 
print(result.group())                      # .group() извлекает найденный текст
# результат: example@gmail.com



# split() - разделить строку по шаблону
import re

text = "apple,banana orange;grape"
result = re.split(r"[ ,;]", text)  # [ .;] означает разделение по пробелу, запятой или точке с запятой

print(result)                      # результат: ['apple', 'banana', 'orange', 'grape']



# sub() - заменить совпадения
import re

text = "My phone numer is 123456"
result = re.sub("\d", "*", text)  # \d любая цифра, все цифры заменяются на *

print(result)                     # результат: My phone number is ******