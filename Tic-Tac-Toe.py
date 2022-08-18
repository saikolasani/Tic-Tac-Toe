

#Function to display the tic-tac-toe board
def display_board(board):
    print(board[1:4])
    print(board[4:7])
    print(board[7:10])
    pass

#Function to process the user input
def player_input():
    marker = 'wrong'
    
    while marker not in ['X','O']:
        marker = input("Please pick a marker 'X' or 'O'").upper()
        
        if marker not in ['X','O']:
            
            clear_output()
            
            print("Sorry, but you did not choose a valid marker 'X' or '0'")
        
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
    
#Places a market on the desired position on the board
def place_marker(board, marker, position):
    board[position] = marker

#Checks if the move wins the game
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random
#Randomly Chooses which player goes first
def choose_first():
    number = random.randint(1,2)
    return f'Player {number}'

#Checks if a space is empty
def space_check(board, position):
    return board[position] == ' '

#Checks if the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Function that asks for the players next choice for position
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    
    return position

#Function that resets the game if the player chooses to
def replay():
    again = 'false'
    
    while again not in ["Y",'N']:
        again = input("Do you want to play again? Y or N").lower()
        
        if again == 'y':
            return True
        else:
            return False


#Runs the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Y or N.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break