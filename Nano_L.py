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
    choice = input("Wilt u een dagboek voor vandaag schrijven of een andere datum? (vandaag/anders): ").lower()
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
        "Hoe was je dag?",
        "Waar ben je dankbaar voor?",
        "Wat heb je vandaag bereikt?",
        "Heb je obstakels of uitdagingen gehad?",
        "Wat heb je geleerd en wat wil je verbeteren?"
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
            f"Er bestaat al een dagboek voor {todaydate}. Wilt u tekst toevoegen of herschrijven? (toevoegen/herschrijven): ").lower()
        if choice == 'toevoegen':
            new_data = ask_questions()
            write_to_file(file_path, new_data, append=True)
        elif choice == 'herschrijven':
            new_data = ask_questions()
            write_to_file(file_path, new_data, append=False)
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
    else:
        print(f"Geen dagboek gevonden voor {todaydate}. Een nieuwe dagboek wordt aangemaakt.")
        new_data = ask_questions()
        write_to_file(file_path, new_data)

# Functie voor spel 2: Rock, Paper, Scissors
def get_computer_choice():
    """Randomly select Rock, Paper, or Scissors for the computer."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie! What a pity!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win! ""keep going..!"
    else:
        return "You lose:( But don't worry, you'll get them next time!"


def my_rps_game():
    """Main game loop for Rock, Paper, Scissors."""
    print("Welcome to my Rock, Paper, Scissors - the easy edition!")
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").capitalize()

        if user_choice == 'Exit':
            print("Thanks for playing RPS! Stay cool!")
            break

        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)


# Functie voor het hoofdmenu
def main_menu():
    while True:
        print("\nWelkom bij de Nano App Store!")
        print("1. Raad Spel")
        print("2. Rock, Paper, Scissors")
        print("3. Dagboek")
        print("4. Exit")
        choice = input("Maak je keuze (1, 2, 3 of 4): ")

        if choice == '1':
            nummer_raad_spel()
        elif choice == '2':
            my_rps_game()
        elif choice == '3':
            manage_journal()
        elif choice == '4':
            print("Bedankt voor het gebruik maken van Nano. Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")


# Start het platform
if __name__ == "__main__":
    # Zorg ervoor dat de map 'files' bestaat voor de dagboekapp
    os.makedirs("files", exist_ok=True)

    # Start het hoofdmenu
    main_menu()
# main menu was made by the chatgpt
