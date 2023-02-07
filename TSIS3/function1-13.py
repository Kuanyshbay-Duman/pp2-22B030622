import random


def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guess = 0
    tries = 0

    while guess != secret_number:
        guess = int(input("Take a guess.\n"))
        tries += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")

    print(f"Good job, {name}! You guessed my number in {tries} guesses!")


guess_the_number()
