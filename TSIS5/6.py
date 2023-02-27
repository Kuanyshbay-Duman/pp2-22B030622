import re
# Use regex to replace spaces, commas, and dots with colons

word = input("Enter a word: ")

modified = re.sub(r'[ ,.]', ':', word)

print(modified)
