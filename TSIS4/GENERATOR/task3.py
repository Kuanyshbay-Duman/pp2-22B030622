def gen(N):
    for i in range(0, N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


number = int(input("Enter a number:"))
for s in gen(number):
    print(s)
