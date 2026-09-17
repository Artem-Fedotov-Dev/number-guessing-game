import random
import math

def is_valid(text, start, end):
    #Prüft, ob die Eingabe eine gültige Zahl zwischen 1 und 100 ist.
    return text.isdigit() and start <= int(text) <= end

def is_valid_answer(text):
    #Prüft, ob die Frage richtig beantwortet wurde.
    return text.strip().lower() in ["nein", "ja"]

def is_valid_range(digit_1, digit_2):
    #Prüft, ob der Spieler den richtigen Bereich angegeben hat.
    return digit_1 < digit_2

def play_game():
    print("Willkommen beim Zahlenratespiel!")

    counter = 0

    while True:
        print("Möchtest du einen Zahlenbereich auswählen? Standardmäßig von 1 bis 100.")
        while True:
            user_request = input("Bitte gib 'Ja' oder 'Nein' ein: ").strip().lower()

            if not is_valid_answer(user_request):
                print("Gültige Antwort ist nur 'Ja' oder 'Nein'!")
                continue
            break
        if user_request == "ja":
            print("Wähle einen Zahlenbereich aus.")
            while True:
                user_start_range = int(input("Gib den Anfang des Bereichs ein: "))
                user_end_range = int(input("Gib das Ende des Bereichs ein: "))
                if not is_valid_range(user_start_range, user_end_range):
                    print("Die zweite Zahl darf nicht kleiner oder gleich der ersten sein. Geben Sie einen gültigen Bereich ein, zum Beispiel 5 und 10.")
                    continue
                break
            secret_number = random.randrange(user_start_range, user_end_range)
            break
        else:
            secret_number = random.randint(1, 100)
            user_start_range = 1
            user_end_range = 100
            break

    n = user_end_range - user_start_range
    ideal_attempts = math.ceil(math.log2(n + 1))
    print(f"Garantierte Versuche bei perfekter Strategie: {ideal_attempts}")

    while True:

        user_input = input(f"Gib eine Zahl von {user_start_range} bis {user_end_range} ein: ")

        if not is_valid(user_input, user_start_range, user_end_range):
            print("Bitte gib eine gültige Zahl ein! ❌")
            continue

        guess = int(user_input)

        if guess < secret_number:
            print("Zu niedrig! 📉")
            counter += 1
        elif guess > secret_number:
            print("Zu hoch! 📈")
            counter += 1
        else:
            counter += 1
            print("Glückwunsch! Du hast die Zahl erraten! 🏆")
            print(f"Du hast {counter} Versuche gebraucht.")
            if counter == 1:
                points = round(100 * (1.5 ** (ideal_attempts - counter)) * 2)
                print("Unfassbar! Du hast die Zahl beim ERSTEN Versuch erraten! 🤯")
                print(f"Du erhältst den ultimativen Glücksbonus: {points} Punkte!")
            elif counter == ideal_attempts:
                points = 100
                print(f"Perfekt! Du hast das Ziel exakt getroffen.")
                print(f"Du erhältst {points} Punkte!")
            elif counter > ideal_attempts:
                points = round(100 * (ideal_attempts / counter))
                print(f"Gut gemacht! Das Ziel waren {ideal_attempts} Versuche.")
                print(f"Du erhältst {points} Punkte!")
            else:
                points = round(100 * (1.5 ** (ideal_attempts - counter)))
                print(f"Grandios! Du hast das mathematische Ziel unterboten! ⚡")
                print(f"Du erhältst einen geometrischen Bonus: {points} Punkte!")
            break

def main_game_loop():
    while True:
        play_game()

        print("\nMöchtest du noch einmal spielen?")

        while True:
            user_request = input("Bitte gib 'Ja' oder 'Nein' ein: ").strip().lower()

            if not is_valid_answer(user_request):
                print("Gültige Antwort ist nur 'Ja' oder 'Nein'!")
                continue
            break

        if user_request == "nein":
            print("Vielen Dank für das Spiel! Bis zum nächsten Mal. 👋")
            break


if __name__ == '__main__':
    main_game_loop()
