# 1. Different ways of creating a string
# Direct assignment
str1 = 'Hello, World!'
# Using double quotes
str2 = "Hello, World!"
# Using triple quotes (useful for multi-line strings)
str3 = '''Hello,
World!'''
# Creating a string from a list of characters
str4 = ''.join(['H', 'e', 'l', 'l', 'o'])

print("str1:", str1)
print("str2:", str2)
print("str3:", str3)
print("str4:", str4)

# 2. Concatenating two strings using + operator
str5 = "Hello"
str6 = "World"
concatenated = str5 + " " + str6
print("Concatenated string:", concatenated)

# 3. Finding the length of the string (manual implementation)
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

length = string_length(str1)
print("Length of str1:", length)

# 4. Extract a substring (manual implementation)
def substring(s, start, end):
    result = ''
    for i in range(start, end):
        result += s[i]
    return result

extracted = substring(str1, 7, 12)
print("Extracted substring:", extracted)

# 5. Searching in strings using index() (manual implementation)
def find_index(s, sub):
    n = string_length(s)
    m = string_length(sub)
    for i in range(n - m + 1):
        if substring(s, i, i + m) == sub:
            return i
    return -1

index = find_index(str1, "World")
print("Index of 'World' in str1:", index)

# 6. Matching a String Against a Regular Expression With matches() (manual implementation)
# Since we can't use regex or inbuilt functions, we'll check if the whole string matches a given pattern
def matches_pattern(s, pattern):
    return s == pattern

pattern = "Hello, World!"
is_match = matches_pattern(str1, pattern)
print("Does str1 match the pattern?", is_match)

# 7. Comparing strings (manual implementation)
def compare_strings(s1, s2):
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return -1

comparison = compare_strings("abc", "xyz")
print("Comparison result:", comparison)

# 8. startsWith(), endsWith() and compareTo() (manual implementation)
def starts_with(s, prefix):
    return substring(s, 0, string_length(prefix)) == prefix

def ends_with(s, suffix):
    return substring(s, string_length(s) - string_length(suffix), string_length(s)) == suffix

starts = starts_with(str1, "Hello")
ends = ends_with(str1, "World!")
print("Does str1 start with 'Hello'?", starts)
print("Does str1 end with 'World!'?", ends)

# 9. Trimming strings with strip() (manual implementation)
def trim(s):
    start = 0
    end = string_length(s) - 1
    while start <= end and (s[start] == ' ' or s[start] == '\n' or s[start] == '\t'):
        start += 1
    while end >= start and (s[end] == ' ' or s[end] == '\n' or s[end] == '\t'):
        end -= 1
    return substring(s, start, end + 1)

str7 = "   Hello, World!   "
trimmed = trim(str7)
print("Trimmed string:", trimmed)

# 10. Replacing characters in strings with replace() (manual implementation)
def replace_char(s, old, new):
    result = ''
    for char in s:
        if char == old:
            result += new
        else:
            result += char
    return result

replaced = replace_char(str1, 'o', '0')
print("String after replacing 'o' with '0':", replaced)

# 11. Splitting strings with split() (manual implementation)
def split_string(s, delimiter):
    result = []
    current = ''
    for char in s:
        if char == delimiter:
            result.append(current)
            current = ''
        else:
            current += char
    result.append(current)
    return result

splitted = split_string(str1, ',')
print("String after splitting by ',':", splitted)

# 12. Converting integer objects to Strings (manual implementation)
def int_to_string(n):
    digits = "0123456789"
    result = ""
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        result = digits[n % 10] + result
        n //= 10
    if is_negative:
        result = '-' + result
    return result if result else "0"

integer = 12345
str_integer = int_to_string(integer)
print("Integer as string:", str_integer)

# 13. Converting to uppercase and lowercase (manual implementation)
def to_uppercase(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def to_lowercase(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

uppercased = to_uppercase("Hello, World!")
lowercased = to_lowercase("Hello, World!")
print("Uppercased string:", uppercased)
print("Lowercased string:", lowercased)
