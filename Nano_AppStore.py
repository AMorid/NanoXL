import random
import datetime
import os
import json

# Functie voor spel 1: nummer raden
def nummer_raad_spel():
    print("Welcome to the Guessing Game!\nTry to guess the number between 1 and 25.")
    print("LET OP! You have only 5 attempts")
    number = random.randrange(1, 25)
    guess = int(input("Enter your guess: "))
    attempt = 5
    while attempt > 1 and number != guess:
        attempt -= 1
        if guess < number:
            print(f"Too low! You have {attempt} attempts left.")
            guess = int(input("Guess again: "))
        elif guess > number:
            print(f"Too high! You have {attempt} attempts left.")
            guess = int(input("Guess again: "))
        else:
            break
    if guess == number:
        print("Hoera! You guessed it right!:)")
    else:
        print(f"Oepsi, you've run out of attempts! The correct number was {number}.")



# Functie voor de dagboek-app
def get_date_from_user():
    choice = input("Wil je een dagboek voor vandaag schrijven of een andere datum? (vandaag/anders): ").lower()
    if choice == 'vandaag':
        return datetime.date.today()
    else:
        date_str = input("Voer de datum in (YYYY-MM-DD): ")
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Ongeldige datum, probeer opnieuw.")
            return get_date_from_user()

def get_file_path(date):
    return f"files/{date}.json"

def check_file_exists(file_path):
    return os.path.exists(file_path)

def ask_questions():
    questions = [
        "How was your day?",
        "What are you grateful for?",
        "What have you accomplished today?",
        "Did you face any obstacle or challenge?",
        "What have you learned and what do you want to improve?"
    ]
    answers = {}
    for question in questions:
        answer = input(question + "\n")
        answers[question] = answer
    return answers

def write_to_file(file_path, data, append=False):
    if append:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(data)
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
    else:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

def manage_journal():
    todaydate = get_date_from_user()
    file_path = get_file_path(todaydate)

    if check_file_exists(file_path):
        choice = input(
            f"Er bestaat al een dagboek voor {todaydate}. Wil je tekst toevoegen of herschrijven? (toevoegen/herschrijven): ").lower()
        if choice == 'toevoegen':
            new_data = ask_questions()
            write_to_file(file_path, new_data, append=True)
        elif choice == 'herschrijven':
            new_data = ask_questions()
            write_to_file(file_path, new_data, append=False)
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
    else:
        print(f"Geen dagboek gevonden voor {todaydate}. Een nieuw dagboek wordt aangemaakt.")
        new_data = ask_questions()
        write_to_file(file_path, new_data)

# Functie voor het hoofdmenu
def main_menu():
    while True:
        print("\nWelkom bij de Nano App Store!")
        print("a. Nummer Raad Spel")
        print("b. Dagboek")
        print("c. Exit")
        choice = input("Maak je keuze (A, B, of C): ")

        if choice == 'a':
            nummer_raad_spel()
        elif choice == 'b':
            manage_journal()
        elif choice == 'c':
            print("Bedankt voor het gebruik maken van Nano App Store! Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

# Start het platform
if __name__ == "__main__":
    # Zorg ervoor dat de map 'files' bestaat voor de dagboekapp
    os.makedirs("files", exist_ok=True)

    # Start het hoofdmenu
    main_menu()
