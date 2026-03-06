import re

# 1. 'a' followed by zero or more 'b'
def task1(text):
    pattern = r"ab*"
    return re.findall(pattern, text)


# 2. 'a' followed by 2 to 3 'b'
def task2(text):
    pattern = r"ab{2,3}"
    return re.findall(pattern, text)


# 3. lowercase letters joined with underscore
def task3(text):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, text)


# 4. One uppercase letter followed by lowercase letters
def task4(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)


# 5. 'a' followed by anything, ending in 'b'
def task5(text):
    pattern = r"a.*b$"
    return re.findall(pattern, text)


# 6. Replace space, comma, or dot with colon
def task6(text):
    pattern = r"[ ,.]"
    return re.sub(pattern, ":", text)


# 7. snake_case → camelCase
def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)


# 8. Split string at uppercase letters
def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)


# 9. Insert spaces before capital letters
def insert_spaces(text):
    return re.sub(r'([A-Z])', r' \1', text).strip()


# 10. camelCase → snake_case
def camel_to_snake(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower()


# Example tests
print(task1("ab abb abbb a"))
print(task2("ab abb abbb abbbb"))
print(task3("hello_world test_text hello"))
print(task4("Hello World Test"))
print(task5("a123b"))
print(task6("Hello, world. How are you"))
print(snake_to_camel("hello_world_test"))
print(split_at_uppercase("HelloWorldTest"))
print(insert_spaces("HelloWorldTest"))
print(camel_to_snake("helloWorldTest"))