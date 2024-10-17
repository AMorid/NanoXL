"""
Opdracht: Nano: Dagboekje.
Naam: Morid Aziz
Studentnummer: 1861078
Bron: W3School, en Python.org
"""
import json
import os
from datetime import datetime


# Sprint 2, Dagboekje
def get_date_from_user():  # De e datum van de gebruiker te krijgen
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
def check_file_exists(file_path):   # of het bestand bestaat
    return os.path.exists(file_path)   # True or false
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
        # Vraag om input voor elke vraag \n voor de regel volgorde
        answers[question] = answer
    return answers
def write_to_file(file_path, data, append=False):
    if append:
        # de antwoorden naar een bestand te schrijven r= read w= write
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(data)
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4) # Schrijf bijgewerkte data naar het bestand
    else:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)   # Schrijf de nieuwe data naar een nieuw bestand
def manage_journal():
    todaydate = get_date_from_user()
    file_path = get_file_path(todaydate)
    if check_file_exists(file_path):
        choice = input(
            f"Er bestaat al een dagboek voor {todaydate}. Wilt u tekst toevoegen of herschrijven? (toevoegen/herschrijven): ").lower()
        if choice == 'toevoegen':
            new_data = ask_questions()   # Vraag voor de nieuwe gegevens
            write_to_file(file_path, new_data, append=True)
            # Voeg de gegevens toe aan het bestaande bestand
        elif choice == 'herschrijven':
            new_data = ask_questions()
            write_to_file(file_path, new_data, append=False)
            # Overschrijf het bestaande besta
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
    else:
        print(f"Geen dagboek gevonden voor {todaydate}. Een nieuwe dagboek wordt aangemaakt.")
        new_data = ask_questions()
        write_to_file(file_path, new_data)
