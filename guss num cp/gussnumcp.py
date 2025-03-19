import random

def guess():
    number = random.randint(1, 20)  # Computer picks a number between 1 and 20
    guess = 0
    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number}!")
        except ValueError:
            print("Please enter a valid number.")

guess()