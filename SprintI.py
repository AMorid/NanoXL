# Opdracht: Nano Raadspel
# Naam: Morid Aziz
# Studentnummer: 1861078

# De code dat/die ik meest trots op ben.
import random
# Sprint 1: nummer raden
# The import let us import entire libraries or specific library functions into code
# \n used for a new line ipv "prints"

print("Welcome to the Guessing Game!\nTry to guess the number between 1 and 25.")
print("LET OP! You have only 5 attempts")
number = random.randrange(1, 25)
guess = int(input("Enter your guess: "))  # Asking the user to guess a number'''
attempt = 5
while attempt > 1 and number != guess:  # Whileloop uit de les en W3school
    attempt -= 1
    if guess < number:
        print(f"Too low! You have {attempt} attempts left.")
        guess = int(input("Guess again: "))
    elif guess > number:
        print(f"Too high! You hvae {attempt} attempts left.1")
        guess = int(input("Guess again: "))
    else:
        break
if guess == number:
    print("Hoera! You guessed it right!:)")
else: print(f"Oepsi, you've run out of attempts! The correct number was {number}.")