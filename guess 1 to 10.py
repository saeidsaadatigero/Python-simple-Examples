import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number(random_number):
    attempts = 3
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        attempts -= 1
        if guess == random_number:
            print("Congratulations! You are the winner!")
            return True
    print("Sorry, you didn't guess the number. Better luck next time!")
    return False

random_number = generate_random_number()
winner = guess_number(random_number)