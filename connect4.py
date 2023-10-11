rows = 6
cols = 7

#CREATE THE 2D ARRAY THAT WILL BE THE BOARD
board = [[' ' for _ in range(cols)] for _ in range(rows)]

# TAKES INPUT AND CHECKS IT IS VALID BEFORE USING IT
def validateColumn():
    while True:
        col_str = input("What column? (1 - 7) ")
        if col_str.isdigit():
            col = int(col_str)
            if 1 <= col <= 7:
                print("\n")
                return col - 1

# PRINT THE BOARD ITERATING THROUGH THE 2D ARRAY
def printBoard():
    for row in board:
        print(row)

# DROP PLAYER PIECE FUNCTION TAKING THE CURRENT PLAYER VALUE AND THE COLUMN INPUT THEY HAVE MADE
def dropPiece(board, col, player):
    # begin from the bottom row and iterate through
    for i in range(rows-1, -1, -1):
        # if the row and column is empty place the piece
        if board[i][col] == ' ':
            board[i][col] = player
            break

# CHECKS THE BOARD FOR A WINNING CONDITION FROM WHAT PLAYERS TURN IT IS
def checkWin(board, piece):
    # check horz win
    for r in range(rows):
        for c in range(cols - 3):
            if (
                board[r][c] == piece and
                board[r][c + 1] == piece and
                board[r][c + 2] == piece and
                board[r][c + 3] == piece
            ):
                return True
    # check vert win
    for r in range(rows - 3):
        for c in range(cols):
            if (
                board[r][c] == piece and
                board[r + 1][c] == piece and
                board[r + 2][c] == piece and
                board[r + 3][c] == piece
            ):
                return True
    # check positive dia win
    for r in range(rows - 3):
        for c in range(cols - 3):
            if (
                board[r][c] == piece and
                board[r + 1][c + 1] == piece and
                board[r + 2][c + 2] == piece and
                board[r + 3][c + 3] == piece
            ):
                return True
    # check negative dia win
    for r in range(3, rows):
        for c in range(cols - 3):
            if (
                board[r][c] == piece and
                board[r - 1][c + 1] == piece and
                board[r - 2][c + 2] == piece and
                board[r - 3][c + 3] == piece
            ):
                return True

    return False

# intilise the first player 
player = 'x'

while True:
    #print the empty board to begin and after every turn
    printBoard()
    #take validate input and make dropCol equal to it
    dropCol = validateColumn()
    dropPiece(board, dropCol, player)
    if checkWin(board, player):
        printBoard()
        print('Player: ' + player + ' wins!!!')
        break
    #change the player value before next turn and iteration of the loop
    player = '%' if player == 'x' else 'x'