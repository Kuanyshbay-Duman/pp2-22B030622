def squares(a, b):
    for i in range(a, b+1):
        yield i**2


a = int(input("Enter first number:"))
b = int(input("Enter secons number:"))

for i in squares(a, b):
    print(i)
