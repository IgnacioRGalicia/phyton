
# a guess game, straigthfoward guess. and computer guess the number

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("almost got it, just a little low")
        elif guess > random_number:
            print("almost there, just a little high")
    print(f"You got me it is {random_number} indeed")

guess(4)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # or high
        feedback = input(f"Is {guess} higher (h), lower(l) or correct(c)").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"the computer is correct and the number is {guess}")

computer_guess(1000)
