# Sprint 3 voor mijn hoofdmenu
import os

from NanoM import nummer_raad_spel, my_rps_game, manage_journal


def main_menu():
    while True:
        print("\nWelkom bij de Nano App Store!")
        print("1. Raad Spel")  # Start het nummer raden spel
        print("2. Rock, Paper, Scissors")   # Start het Rock, Paper, Scissors spel
        print("3. Dagboek")
        print("4. Exit")
        choice = input("Maak je keuze (1, 2, 3 of 4): ")
        # if, elif, eles statements sgebruikt
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
# Start mijn platform
if __name__ == "__main__":
    # Hier heel klein beetje chat gebruikt.
    os.makedirs("files", exist_ok=True)
    # Start mijn hoofdmenu
    main_menu()