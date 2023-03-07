def is_pal(str):
    rev_str = ''.join(reversed(str))
    return str == rev_str


word = input("Enter a word: ")

if is_pal(word):
    print("It is palindrome")
else:
    print("It is not")
