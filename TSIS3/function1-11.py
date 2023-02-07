def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]


print(is_palindrome("Madam"))  # True
print(is_palindrome("Hello"))  # False
