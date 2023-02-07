def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print("Prime numbers in the list:", prime_numbers)
