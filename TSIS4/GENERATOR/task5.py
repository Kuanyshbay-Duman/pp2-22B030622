def from_largest_to_smaller(n):
    while n >= 0:
        yield n
        n -= 1


number = int(input("Enter a number:"))
for i in from_largest_to_smaller(number):
    print(i)
