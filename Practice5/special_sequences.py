# a special sequence is a \ followed by one of the characters in the list below, and has a special meaning

# \A - match at the start of a string
import re
text = "The sun is bright"
result = re.findall(r"\AThe", text)
print(result)  # output: ['The']
# \A matches on;y if the pattern appears at the very beginning of the string


# \b - word boundary
import re
text = "rain in Spain"
result = re.findall(r"\brain", text)
print(result)  # output: ['rain']
# \b matches the beginning or end of a word
result2 = re.findall(r"ain\b", text)
print(result2)  # output: ['ain', 'ain']


# \B - NOT a word boundary
import re
text = "rain in Spain"
result = re.findall(r"\Bain", text)
print(result)  # output: ['ain', 'ain']
# \B matches characters that are inside a word, not at the boundary


# \d - digit (0-9)
import re
text = "My numbers are 7 and 42"
result = re.findall(r"\d", text)
print(result)  # output: ['7', '4', '2']
# \d matches any digit


# \D - NOT a digit
import re
text = "A1 B2 C3"
result = re.findall(r"\D", text)
print(result)  # output: ['A', ' ', 'B', ' ', 'C']
# \D matches any character that is not a digit


# \s - whitespace
import re
text = "Hello World"
result = re.findall(r"\s", text)
print(result)  # output: [' ']
# \s matches spaces, tabs, or newline characters


# \S - NOT whitespace
import re
text = "Hello World"
result = re.findall(r"\S", text)
print(result)  # output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
# \S matches any character except whitespace


# \w - word characters
import re
text = "User_123 logged in"
result = re.findall(r"\w", text)
print(result)  # output: ['U', 's', 'e', 'r', '_', '1', '2', '3', 'l', 'o', 'g', 'g', 'e', 'd','i','n']
# \w matches letters, digits, and underscore _


# \W - NOT word characters
import re
text = "User_123!"
result = re.findall(r"\W", text)
print(result)  # output: ['!']
# \W matches charactes that are not letters, digits, or _


# \Z - match at the end of a string
import re
text = "Welcome to Spain"
result = re.findall(r"Spain\Z", text)
print(result)  # output: ['Spain']
# \Z matches only if the pattern appears at the end of the string