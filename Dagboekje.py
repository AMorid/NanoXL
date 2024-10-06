"""
Opdracht: Nano, Dagboekje
Naam: Morid Aziz
Studentnummer: 1861078
"""
# (To-DO lijs voor de NANO XL)

# Voeg een wachtwoord toe aan het dagboek
# Geef de gebruiker de mogelijkheid om de tekst van een dag op te vragen en te lezen
# Geef de gebruiker de mogelijkheid om een tekst te bewerken


import datetime
import os
import json


# Functie om de gebruiker om een datum te vragen (vandaag of een andere datum)
def get_date_from_user():
    print("Welkom bij uw dagelijkse dagboek!")
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
        print(f"Geen dagboek gevonden voor {todaydate}. Een nieuw dagboek wordt aangemaakt.")
        new_data = ask_questions()
        write_to_file(file_path, new_data)


# Start de dagboekapplicatie
if __name__ == "__main__":
    # Zorg ervoor dat de map 'files' bestaat
    os.makedirs("files", exist_ok=True)

    # Voer de dagboekfunctie uit
    manage_journal()
