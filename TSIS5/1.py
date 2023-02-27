import re
# program that matches a string that has an 'a' followed by zero or more 'b''s.

pattern_for_b = r'a+b*'
word = input("Enter a word: ")
finding_b = re.match(pattern_for_b, word)


if finding_b:
    print("There are 0 or more b's after a!")
else:
    print("It does not obey the condition")
