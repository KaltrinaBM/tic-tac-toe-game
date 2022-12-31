# Show instructions on how to play the game
def game_inst():

    print("* The game is played on a grid that's "
          "3 squares by 3 squares.")
    print("* You choose your symbol being either 'X' or 'O'. "
          "Opponent will get the ones that's left.")
    print("* The first player to get 3 of her marks in a row "
          "(up, down, across, or diagonally) is the winner.")
    print("* When all 9 squares are full, the game is over. If no "
          "player has 3 marks in a row, the game ends in a tie.\n")


game_inst()

# Get the player name only letters accepted
def player_name():

    while True:
        global player_name
        player_name = input("Enter your name please: \n")

        if player_name.isalpha():
            print(f"Nice to meet you {player_name.capitalize()}.")
            break
        else:
            print("Only letters are accepted")


player_name()

# Take player's symbol choice
def select_option():
    player_choice = input(f"{player_name.capitalize()}, please select X or O:")
    comp_choice = ""
    while True:
        if player_choice.upper() == "X":
            comp_choice == "O"
            print("Your opponent is O")
            return player_choice.upper(), comp_choice
        elif player_choice.upper() == "O":
            comp_choice == "X"
            print("Your opponent is X")
            return player_choice.upper(), comp_choice
        else:
            player_choice = input(f"{player_name.capitalize()}, please select X or O:")


select_option()