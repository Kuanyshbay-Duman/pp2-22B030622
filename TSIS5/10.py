import re


def camel_to_snake(str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', str)
    return snake_str.lower()


word = input("enter a word: ")

print(camel_to_snake(word))
