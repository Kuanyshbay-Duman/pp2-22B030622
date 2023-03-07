from functools import reduce


def multiplying_all_elements(sequence):
    number = reduce(lambda a, b: a*b, sequence)
    return number

example = [1, 3, 6, 3, 2]

print(multiplying_all_elements(example))


# import math

# n = int(input())
# a = list(map(int,input().strip().split()))[:n]
# prod=math.prod(a)
# print(prod)


