'''importing modules'''
import random
import sys

# Variables used through the functions below which we need to access using global statement

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
score_x = 0
score_o = 0
symbol_selected = 'X'
if_winner = None
player_name = None

# Displaying the instructions on how o play the game

def game_inst():
    print("\n")
    print("*** Welcome to TIC TAC TOE! ***")
    print("________________________________\n")
    print(" -- The game is played on a grid that's "
          "3 squares by 3 squares and a Refernce board will be displayed.")
    print(" -- Your symbol will be'X' and computer will be 'O'. ")
    print(" -- The first who gets 3 same symbols in a row "
          "(column, or diagonally) is the winner.")
    print(" -- When all 9 squares are full, the game is over. If no "
          "player has 3 marks in a row, the game ends in a tie.")
    print(" -- Once the game is finished, you have the option to play again,"
          "or quit the game, and the scores will be displayed when playing.\n")

game_inst()


def player_name():
    '''
    Request player's name so we can address by name throught the game
    '''
    
    while True:
        global player_name
        player_name = input("Let's meet. Please enter your name: \n")

        if player_name.isalpha():
            print(f"\nNice to meet you {player_name.capitalize()}.\n"
            "\nYou are playing as 'X' and I am (computer) playing as 'O'\n")
            break
        else:
            print("Incorrect typing. Enter letters only!")

player_name()

def new_game():
    '''
    Request from the user to type Y/N to start or quit thegame, 
    so the board is displayed or the game is ended.
    '''
    while True:
        new_game_input = input("Do you want to play? (Y/N)\n")
        if new_game_input.lower() == 'y':             
            print('Get ready...')
            break
        elif new_game_input.lower() == 'n':
            print("Sorry to see you go, and hope that we will meet again.")
            quit()
        else:
            print(f"{new_game_input} is incorrect value. Please type 'Y' for Yes or 'N' for No. Do you want to play?")


new_game()


def display_board(board):
    '''
    Show board game to play and a reference game to show with which numbers the player has to play. 
    Also, displaying the scores each time the board is displayed.
    '''
    print('\n')
    print(" Game board " + " "*9 + "Reference board\n")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  " +
          " "*10 + " " + "1" + " | " + "2" + " | " + "3" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  " +
          " "*10 + " " + "4" + " | " + "5" + " | " + "6" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  " +
          " "*10 + " " + "7" + " | " + "8" + " | " + "9" + "  ")
    print("\n")
    print(f'Your Score: {score_x:>5}\n')
    print(f'Computer Score:{score_o:>5}\n')

def clear_board():
    '''
    Clear the board for the next game.
    '''
    board.clear()
    board.extend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

def play_quit():
    '''
    Request an input from the player if player wants to play or quit the game.
    '''
    print("*** Game Over*** \n")

    print("Enter 'Y' to play again.")
    print('Enter "Q" to quit the game.\n')
    while True:
        global player_name
        play_quit = input().strip()
        if play_quit.lower() == 'q':
            print(f'It was a pleasure playing with you {player_name.capitalize()}.')
            quit()
        elif play_quit.lower() == 'y':
            print(f'Welcome back {player_name.capitalize()}')
            new_game()
            clear_board()
            play_game()

        else:
            print("Incorrect input. Please select 'Y' or 'Q'")


def increment_score():
    '''
    Add 1 score point if there is a win for each symbol
    '''
    if if_winner == 'X':
        global score_x
        score_x += 1
    elif if_winner == 'O':
        global score_o
        score_o += 1
    else:
        return None

# Switching between computer 'O' and player 'X'
def switch_play():
    '''
    Switches the turn after each input from the player and computer
    '''
    global symbol_selected
    if symbol_selected == 'X':
        symbol_selected = 'O'

    else:
        symbol_selected = 'X'


def computer_turn(board):
    '''
    Computer selects random numbers from 1-9, if there are available spots
    '''
    while symbol_selected == 'O':
        comp_selected = random.randint(1, 9)
        if board[comp_selected] == ' ':
            board[comp_selected] = 'O'
            switch_play()


def play_game():
    '''
    Game starts by taking player's input and calling other methods,
     to switch the player and check if it is a win or tie.
    '''
    while True:
        display_board(board)

        while True:

            try:

                player_inp = int(input('Type a number between 1-9! :\n'))

                if player_inp in range(1, 10):
                    if board[player_inp] == ' ':
                        board[player_inp] = symbol_selected
                        break
                    else:
                        print(
                            f"Number: {player_inp}, is already taken. "
                            "Type another number.")
                else:
                    print('Invalid selection. Type a number between 1-9!\n')

            except ValueError:
                print("Wrong input. Please enter a valid number:\n")

        switch_play()
        computer_turn(board)

play_game()