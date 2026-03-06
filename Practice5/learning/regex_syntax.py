# a RegEx, or Regular Expression, is a sequence of characters that forms a search pattern
# RegEx can be used to check if a string contains the specified search pattern

# python has a built-in package called re, which can be used to work with Regular Expressions
# import re module
import re

# when you have imported re module, you can start using regular expressions
import re

txt = "The rain in Spain0"
x = re.search("^The.*Spain$", txt)