def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  # [1, 2, 3, 4, 5]
