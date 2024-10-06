# Opdracht: Nano
# Naam: Morid Aziz
# Studentnummer: 1861078


import datetime

todaydate = datetime.date.today()

file_path = f"files/{todaydate}.txt"

file = open(file_path, 'w')
file.close()

question = "How was your day?"
answer1 = input("How was your day?\n")

# Open het bestand opnieuw in schrijfmodus om erin te schrijven
with open(file_path, 'w') as file:
    file.write(f"{question}\n")
    file.write(f"{answer1}\n")
