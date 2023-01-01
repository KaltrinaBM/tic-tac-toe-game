'''importing modules'''
import sys  # to access parameters and functions
import random  # for computer moves

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

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

def select_symbol():
    # Ask the player if player wants to chose X or O
    symbol = ''
    while not (symbol == 'X' or symbol == 'O'):
        print("Please select X or O:")
        symbol = input().upper()

    if symbol == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


select_symbol()

