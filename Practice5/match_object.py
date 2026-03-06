# a Match Object is an object containing information about the search and the result
# if there is no match, the value None will be returned, instead of the Match Object

import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object


# .span() returns a tuple containing the start-, and en positions of the match
# Search for an uppercase "S" character in the beginning of a word, and print its position
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())  # output: (12, 17)


# .string returns the string passed into the function
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)  # output: The rain in Spain


# .group() returns the part of the string where there was a match
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())  # output: Spain
