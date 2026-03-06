# RegEx flags change how the pattern behaves

# re.ASCII (re.A) - matches only ASCII characters
import re
text = "hello world привет мир"
matches = re.findall(r"\w+", text, re.ASCII)
print(matches)  # output: ['hello', 'world']
# \w+ normally matches letters, numbers, and underscores including Unicode characters
# with re.ASCII, it matches only English ASCII characters


# re.DEBUG - displays debugging information about the regex pattern
import re
pattern = re.compile(r"\d+", re.DEBUG)
# this flag prints information about how Python parses the regex
# it is mostly used for learning or debuggibg complex expressions


# re.DOTALL (re.S) - makes the dot . match all characters including newline
import re
text = "hello\nworld"
matches = re.findall(r"hello.world", text, re.DOTALL)
print(matches)  # output: ['hello\nworld']
# normally . matches any character except newline (\n)
# with re.DOTALL it also matches newline characters


# re.IGNORECASE (re.I) - ignores letter case during matching
import re
text = "Hello hello HELLO"
matches = re.findall(r"hello", text, re.IGNORECASE)
print(matches)  # output: ['Hello', 'hello', 'HELLO']
# without this flag, "hello" would only match lowercase "hello"
# with re.IGNORECASE, it matches Hello, HELLO, hello, etc.


# re.MULTILINE (re.M) - allows ^ and $ to match the start and end of each line, not just the entire string
import re
text = """cat
dog
cat
bird"""
matches = re.findall(r"^cat", text, re.MULTILINE)
print(matches)  # output: ['cat', 'cat']
# ^ normally matches only the start of the whole string
# with re.MULTILINE, it matches the start of every line


# re.NOFLAG - explicitly indicates no flags are used
import re
text = "cat dog bird"
matches = re.findall(r"cat", text, re.NOFLAG)
print(matches)  # output: ['cat']
# the regex runs with default behavior


# re.UNICODE (re.U) - matches Unicode characters
import re
text = "hello привет 123"
matches = re.findall(r"\w+", text, re.UNICODE)
print(matches)  # output: ['hello', 'привет', '123']
# \w+ will match words including Unicode characters


# re.VERBOSE (re.X) - allows spaces and comments inside the regex pattern for better readability
import re
pattern = r"""
\d+         # match one or more digits
"""
text = "Order numbers: 7, 42, 105"
matches = re.findall(pattern, text, re.VERBOSE)
print(matches)  # output" ['7', '42', '105']
# with re.VERBOSE, you can format regex like code and add comments