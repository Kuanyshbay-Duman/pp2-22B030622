def permutations(data, i, length):
    if i == length:
        print("".join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutations(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


def print_permutations(string):
    permutations(list(string), 0, len(string))


string = input("Enter a string: ")
print("All permutations of the string:")
print_permutations(string)
