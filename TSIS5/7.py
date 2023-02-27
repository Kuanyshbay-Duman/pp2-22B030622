import re
# converting snake to camel


def snake_to_camel_regex(s_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s_str)


string = input("Enter a snake case string: ")

modified = snake_to_camel_regex(string)

print(modified)
