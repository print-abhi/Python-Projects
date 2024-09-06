import random

random_number = random.randint(1,100)
guess = None

while guess != random_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Your Guess is Too low!")
    elif guess > random_number:
        print("Your Guess is Too high!")
    else:
        print("Congratulations! You guessed it.")
