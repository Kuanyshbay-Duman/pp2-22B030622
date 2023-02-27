import re

# program to find the sequences of one upper case letter followed by lower case letters.

sentence = input("Enter a sentence: ")


pattern = r"[A-Z][a-z]+"

finding = re.findall(pattern, sentence)

print(finding)
