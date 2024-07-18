import random

def welcome_player():
    print("Benvenuto a Carta, Forbici, Sasso 4.0!")
    name = input("Per favore, inserisci il tuo nome: ")
    return name

def get_player_choice():
    while True:
        print("Fai la tua scelta: carta, forbici o sasso")
        choice = input("Inserisci la tua scelta: ").lower()
        if is_valid_choice(choice):
            return choice
        else:
            print("Scelta non valida! Per favore, scegli tra carta, forbici o sasso.")

def is_valid_choice(choice):
    return choice in ["carta", "forbici", "sasso"]

def get_computer_choice():
    choices = ["carta", "forbici", "sasso"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice, god_mode):
    if god_mode:
        return "Hai vinto!"
    if player_choice == computer_choice:
        return "Pareggio"
    elif (player_choice == "carta" and computer_choice == "sasso") or \
         (player_choice == "forbici" and computer_choice == "carta") or \
         (player_choice == "sasso" and computer_choice == "forbici"):
        return "Hai vinto!"
    else:
        return "Hai perso!"

def get_number_of_games():
    while True:
        try:
            num_games = int(input("Quante partite vuoi giocare? "))
            if num_games > 0:
                return num_games
            else:
                print("Per favore, inserisci un numero positivo.")
        except ValueError:
            print("Input non valido. Per favore, inserisci un numero.")

def ask_god_mode():
    while True:
        choice = input("Vuoi attivare la 'God Mode'? (sì/no): ").lower()
        if choice in ["sì", "si", "no"]:
            return choice in ["sì", "si"]
        else:
            print("Scelta non valida! Per favore, rispondi con 'sì' o 'no'.")

def play_game():
    name = welcome_player()
    
    num_games = get_number_of_games()
    god_mode = ask_god_mode()
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    for game_number in range(num_games):
        print(f"\nPartita {game_number + 1} di {num_games}. Buona fortuna, {name}!")
        
        player_choice = get_player_choice()
        
        computer_choice = get_computer_choice()
        print(f"Il computer ha scelto: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice, god_mode)
        if result == "Hai vinto!":
            player_wins += 1
        elif result == "Hai perso!":
            computer_wins += 1
        else:
            ties += 1
        print(f"{result}, {name}!")
    
    print("\nRisultati finali:")
    print(f"Vittorie di {name}: {player_wins}")
    print(f"Vittorie del computer: {computer_wins}")
    print(f"Pareggi: {ties}")
    print("Grazie per aver giocato!")

if __name__ == "__main__":
    play_game()

