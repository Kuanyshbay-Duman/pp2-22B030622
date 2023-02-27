import re
# program to find sequences of lowercase letters joined with a underscore.


sentence = input("Enter a sentence with underscore: ")
pattern = r"[a-z]+_[a-z]+"

finding = re.findall(pattern, sentence)

for i in finding:
    print(i)
