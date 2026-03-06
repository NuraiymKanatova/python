# metacharacters are characters with a special meaning

# [] - a set of characters
import re
text = "apple mango zebra lemon"
result = re.findall(r"[a-m]+", text)
print(result)  # output: ['a', 'le', 'ma', 'g', 'eb', 'a', 'lem ']
# finds letters from a to m


# \ - signals a special sequence (can also be used to escape special characters)
import re
text = "Order numbers: 45, 123, 9"
result = re.findall(r"\d+", text)           
print(result)  # output: ['45', '123', '9']
# \d means any number


# . - any character (except newline character)
import re
text = "hello healo he11o"
result = re.findall(r"he..o", text)
print(result)  # output: ['hello', 'healo', 'he11o']


# ^ - starts with 
import re
text = "hello world"
result = re.findall(r"^hello", text)
print(result)  # output: ['hello']
# checks the beginning of the line


# $ - ends with
import re
text = "I love this planet"
result = re.findall(r"planet$", text)
print(result)  # output: ['planet']
# checks the ending of the line


# * - zero or more occurences
import re
text = "heo heeeeo hello"
result = re.findall(r"he.*o", text)
print(result)  # output: ['heo heeeeo hello']
# * means any number of characters


# + - one or more occurences
import re
text = "heo heeeeo heo"
result = re.findall(r"he.+o", text)
print(result)  # output: ['heo heeeeo heo']
# + requires at least one character


# ? - zero or one occurences
import re
text = "heo heo heyo"
result = re.findall(r"he.?o", text)
print(result)  # output: ['heo', 'heo', 'heyo']
# ? means one character or its absence


# {} - exactly the specified number of occurences
import re
text = "hello he12o heabcdo"
result = re.findall(r"he.{2}o", text)
print(result)  # output: ['hello', 'he12o']
# {2} means exactly two characters


# | - either or
import re
text = "The rain falls or stays"
result = re.findall(r"falls|stays", text)
print(result)  # output: ['falls', 'stays']
# | works like logical OR


# () - capture and group
import re
text = "My number is 123-456"
result = re.search(r"(\d+)-(\d+)", text)
print(result.group(1))  # 123
print(result.group(2))  # 456
# () allows divide a match into groups