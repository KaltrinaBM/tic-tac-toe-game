'''importing modules'''
import random
import sys

# Variables used through the functions below which we need to access using global statement

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Displaying the instructions on how o play the game

def game_inst():
    print("Welcome to TIC TAC TOE!")
    print("* The game is played on a grid that's "
          "3 squares by 3 squares and a Refernce board will be displayed")
    print("* Your symbol will be'X' and computer will be 'O'. ")
    print("* The first player to get 3 of her marks in a row "
          "(up, down, across, or diagonally) is the winner.")
    print("* When all 9 squares are full, the game is over. If no "
          "player has 3 marks in a row, the game ends in a tie.\n")

game_inst()


def player_name():

    while True:
        global player_name
        player_name = input("Please enter your name: \n")

        if player_name.isalpha():
            print(f"Nice to meet you {player_name.capitalize()}.")
            break
        else:
            print("Please enter only letters!")

player_name()

def new_game():
    '''
    Request from the user to select number '1' to start the game, so the board will be displayed.
    '''
    while True:
        new_game_input = input("Please enter number '1' to start the game:\n")
        if new_game_input == '1':             
            print('Get ready...')
            break
        else:
            print(f"{new_game_input}Please enter number '1' to start the game.")


new_game()


def display_board(board):
    '''
    Show board game to play and a reference game to show with which numbers the player has to play. 
    Also, displaying the scores each time the board is displayed.
    '''
    print('\n')
    print(" Game board " + " "*9 + "Reference board")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  " +
          " "*10 + " " + "1" + " | " + "2" + " | " + "3" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  " +
          " "*10 + " " + "4" + " | " + "5" + " | " + "6" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  " +
          " "*10 + " " + "7" + " | " + "8" + " | " + "9" + "  ")
    print("\n")

print(display_board(board))

