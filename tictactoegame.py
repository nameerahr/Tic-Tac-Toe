
def board(game_board):
    print()
    for row in game_board:
        for slot in row:
            print(slot, " ", end ="")
        print()

def current_player(currentplayer):
    if (currentplayer == True):
        return "x"
    else:
        return "o" 

def check_position(position):
    if (position.isnumeric()):
        position = int(position)
        if(position >= 1 and position <= 9):
            return True
        else:
            print("Please enter a position from 1-9: ")
            return False
    else:
        print("Please enter a position from 1-9: ")
        return False
        
def array_position(position):
    #first row is 0 in array - anything less than 3 divided by 3 will give 0
    row = int(position/3)
    # in first row, the column number is given by the player's input position - 1
    column = int(position)
    # after the first row (second and third row), the column number is:
    if (column >= 3):
        column = int(column % 3)
    return (row, column)

def position_available(game_board, arrayposition):
    row = arrayposition[0]
    column = arrayposition[1]
    if((game_board[row][column] == "x") or (game_board[row][column] == "o")):
        print("This position is taken. Enter an available position.")
        return True
    else:
        return False

def player_turn(player, arrayposition, game_board):
    row = arrayposition[0]
    column = arrayposition[1]
    game_board[row][column] = player
    
def winner(player, game_board):
    if ((win_in_row(player, game_board) == True) or (win_in_column(player, game_board) == True) or (win_in_diagonal(player, game_board) == True)):
        return True
    else:
        return False

def win_in_row(player, game_board):
    if ((game_board[0][0] == player) and (game_board[0][1] == player) and (game_board[0][2] == player)):
        return True
    elif((game_board[1][0] == player) and (game_board[1][1] == player) and (game_board[1][2] == player)):
        return True
    elif((game_board[2][0] == player) and (game_board[2][1] == player) and (game_board[2][2] == player)):
        return True
    else:
        return False

def win_in_column(player, game_board):
    if ((game_board[0][0] == player) and (game_board[1][0] == player) and (game_board[2][0] == player)):
        return True
    elif((game_board[0][1] == player) and (game_board[1][1] == player) and (game_board[2][1] == player)):
        return True
    elif((game_board[0][2] == player) and (game_board[1][2] == player) and (game_board[2][2] == player)):
        return True
    else:
        return False

def win_in_diagonal(player, game_board):
    if ((game_board[0][0] == player) and (game_board[1][1] == player) and (game_board[2][2] == player)):
        return True
    elif((game_board[0][2] == player) and (game_board[1][1] == player) and (game_board[2][0] == player)):
        return True
    else:
        return False



game_board = [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]
            ]

currentplayer = True

turns = 1

while (turns <= 9):    
    board(game_board)

    player = current_player(currentplayer)   

    position = input("Enter a position (1-9) on the board: ")

    if (check_position(position) == False):
       continue

    position = int(position) - 1
    arrayposition = array_position(position)

    if (position_available(game_board, arrayposition) == True):
        continue

    player_turn(player, arrayposition, game_board)

    if(winner(player, game_board) == True):
        board(game_board)
        print( player, "IS THE WINNER!")
        print()
        break

    turns = turns + 1

    if (turns == 10):
        board(game_board)
        print("  Tie!")
        print()

    currentplayer = not currentplayer
