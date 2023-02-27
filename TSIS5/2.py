import re
# program that matches a string that has an 'a' followed by two to three 'b'.

pattern_for_b = r"a{1}b{2,3}"
word = input("Enter a word: ")
finding_b = re.match(pattern_for_b, word)


if finding_b:
    print("There are 2 or 3 b's after a!")
else:
    print("It does not obey the condition")
