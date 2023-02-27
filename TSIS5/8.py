import re


def split_at_uppercase(str):
    return re.findall(r'[A-Z][^A-Z]*', str)


word = input("Enter a word: ")

print(split_at_uppercase(word))
