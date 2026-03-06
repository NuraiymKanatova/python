# Practice 5: Python Regular Expressions (RegEx)

This practice contains learning materials and exercises for working with **Regular Expressions (RegEx) in Python**.

The goal of this practice was to understand how regex works and apply it to different text processing tasks.


## Learn Python RegEx from W3Schools

The **learning** folder contains theoretical materials and examples related to Python regular experssions.

Topic covered:
- RegEx syntax
- RegEx functions (`findall`, `search`, `split`, `sub`)
- Metacharacters (`[]`, `\`, `.`, `^`, `$`, `*`, `+`, `?`, `{}`, `|`, `()`)
- Flags (`re.ASCII`, `re.DEBUG`, `re.DOTALL`, `re.IGNORECASE`, `re.MULTILINE`, `re.NOFLAG`, `re.UNICODE`, `re.VERBOSE`)
- Special sequences (`\A`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S`, `\w`, `\W`, `\Z`)
- Sets (`[arn]`, `[a-n]`, `[^arn]`, `[0123]`, `[0-9]`, `[0-5][0-9]`, `[a-zA-Z]`, `[+]`)
- Match object (`.span()`, `.string`, `.group()`)

There materials were use to understand how regular expressions work and how they can be applied for text searching and processing.


## Practical Exercise: Receipt Rarsing

A practical task was completed using the provided **raw.txt** file.

### Tasks

1. Extract all prices from the receipt
2. Find all product names
3. Calculate the total amount
4. Extract date and time information
5. Find the payment method
6. Create structured output (JSON or formatted text)

### Implementation

A Python script **receipt_parser.py** was created to parse data using regular expressions.

The program:
- extracts important information from raw text
- processes different formatting cases
- outputs structured and readable data


## Python RegEx Exercises

The **exercises** folder contain solutions to several regex practice problems.

### List of Exercises

1. Match a string that has an **'a' followed by zero or more 'b'**.
2. Match a string that has an **'a' followed by two to three 'b'**.
3. Find sequences of **lowercase letters joined with an underscore**.
4. Find sequences of **one uppercase letter followed by lowercase letters**.
5. Match a string that has an **'a' followed by anything, ending in 'b'**.
6. Replace all **spaces, commas, or dots with a colon**.
7. Convert a **snake_case string to camelCase**.
8. Split a string **at uppercase letters**.
9. Insert **spaces between words starting with capital letters**.
10. Convert a **CamelCase string to snake_case**.

These exercises demonstrate how regular expressions can be used for pattern matching, string manipulation, and text processing in Python.