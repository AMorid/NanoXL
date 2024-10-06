# import datetime
#
# todaydate = datetime.date.today()
#
# file_path = f"files/{todaydate}.txt"
# # opening the file in writing mode.
# file = open(file_path, 'w')
# file.close()
# # variables to store questions.
# question1 = "How was your day?"
# question2 = "What are you gratful for?"
# question3 = "What have you accomplished today?"
# question4 = "Did you face any obstakel or challenge?"
# question5 = "What have you learned and what you wanna improve?"
# # Taking users input as answer
# answer1 = input("How was your day?\n")
# answer2 = input("How was your day?\n")
# answer3 = input("How was your day?\n")
# answer4 = input("How was your day?\n")
# answer5 = input("How was your day?\n")
# # Open het bestand opnieuw in schrijfmodus om erin te schrijven
# with open(file_path, 'w') as file:
#     file.write(f"{question1}\n")
#     file.write(f"{answer1}\n")
#     file.write(f"{question2}\n")
#     file.write(f"{answer2}\n")
#     file.write(f"{question3}\n")
#     file.write(f"{answer3}\n")
#     file.write(f"{question4}\n")
#     file.write(f"{answer4}\n")
#     file.write(f"{question5}\n")
#     file.write(f"{answer5}\n")
#     file.close()

"""
Opdracht: Nano, Dagboekje
Naam: Morid Aziz
Studentnummer: 1861078
"""

import datetime
import os
import json


# Functie om de gebruiker om een datum te vragen (vandaag of een andere datum)
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


# Functie om het bestandspad te genereren op basis van de datum
def get_file_path(date):
    return f"files/{date}.json"


# Functie om te controleren of een bestand bestaat
def check_file_exists(file_path):
    return os.path.exists(file_path)


# Functie om vragen te stellen en antwoorden te verzamelen
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


# Functie om naar een bestand te schrijven (herschrijven of toevoegen)
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


# Functie om het dagboek bij te werken of herschrijven
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


# Start de dagboekapplicatie
if __name__ == "__main__":
    # Zorg ervoor dat de map 'files' bestaat
    os.makedirs("files", exist_ok=True)

    # Voer de dagboekfunctie uit
manage_journal()
