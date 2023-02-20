def evens(N):
    for i in range(0, N+1):
        if i % 2 == 0:
            yield i


number = int(input("Enter a number:"))
list1 = []
for s in evens(number):
    list1.append(str(s))
sentence = ", ".join(list1)
print(sentence)
