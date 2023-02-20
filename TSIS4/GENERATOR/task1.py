def gen(N):
    for i in range(1, N+1):
        yield i**2


for s in gen(5):
    print(s)
