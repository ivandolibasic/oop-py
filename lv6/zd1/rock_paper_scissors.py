def main():
    # https://en.wikipedia.org/wiki/Rock_paper_scissors
    player1 = input("Enter username (player 1): ")
    player2 = input("Enter username (player 2): ")

    choice_mapper = {
        'a': 'rock',
        's': 'paper',
        'd': 'scissors',

        '1': 'rock',
        '2': 'paper',
        '3': 'scissors'
    }
    # https://www.w3schools.com/python/python_dictionaries_access.asp

    player1_points = 0
    player2_points = 0

    while True:
        player1_choice = input(f"{player1}'s choice: ").lower()
        player2_choice = input(f"{player2}'s choice: ").lower()

        player1_choice = choice_mapper.get(player1_choice)
        player2_choice = choice_mapper.get(player2_choice)
        # https://www.w3schools.com/python/ref_dictionary_get.asp

        print(f"{player1} has chosen {player1_choice}")
        print(f"{player2} has chosen {player2_choice}")

        if player1_choice == player2_choice:
            outcome = "draw"
        elif ((player1_choice == 'paper' and player2_choice == 'rock') or
              (player1_choice == 'scissors' and player2_choice == 'paper') or
              (player1_choice == 'rock' and player2_choice == 'scissors')):
            outcome = f"{player1} won"
            player1_points += 1
        else:
            outcome = f"{player2} won"
            player2_points += 1

        print(f"Round outcome: {outcome}")
        print(f"Current score: {player1}: {player1_points} vs. {player2}: {player2_points}")

        quit_game = input("Do you want to quit the game? Enter (x) for yes or anything else for no: ")
        if quit_game == 'x':
            if player1_points > player2_points:
                print(f"{player1} won the game with the {player1_points - player2_points}-point difference.")
            elif player1_points < player2_points:
                print(f"{player2} won the game with the {player2_points - player1_points}-point difference.")
            else:
                print("The game ended in a draw.")
            break

main()
