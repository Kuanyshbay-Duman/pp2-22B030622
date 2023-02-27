import re


def insert_spaces(str):
    return re.sub(r'([a-z])([A-Z][a-z]+)', r'\1 \2', str)


words = input("enter a joined words: ")
modified = insert_spaces(words)

print(modified)
