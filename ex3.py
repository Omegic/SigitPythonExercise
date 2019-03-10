#Sigit python git exercise
#author: Ido Noyman
#Exercise 3: Check winner in tic tac toe

def TTTCheck(board):
    # Checks if a row, a column or a diagonal is solved (full) by a player.
    # Input: The matrix of the board.
    # Output: returns the winner of the game, by checking if the player solved a wor, a column or a diagonal. If nor of the players solved any, the function will return 0 (tie).

    winner = 0 # 0 = tie, 1 = player 1 won, 2 = player 2 won
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != 0:
        winner = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != 0:
        winner = board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
        winner = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
        winner = board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]

    if winner == 0:
        print("Tie")
    else:
        print("Player number " + str(winner) + " won!")
    return

def main():
	# Exrecise 3 init (player 1 win situtation):
    board = [[1,0,2],
           [1,0,2],
           [1,2,0]]
    TTTCheck(board)

if __name__ == '__main__':
    main()
