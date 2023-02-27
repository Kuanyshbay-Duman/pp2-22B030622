import re

# program that matches a string that has an 'a' followed by anything, ending in 'b'.

word = input("Enter a word: ")
pattern = r"^a.*b$"

finding = re.match(pattern, word)

if finding:
    print("It starts with a and ends with b")
else:
    print("It does not eboy the condition")
