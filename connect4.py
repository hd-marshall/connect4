rows = 6
cols = 7

board = [[' ' for _ in range(cols)] for _ in range(rows)]

def validateColumn():
    while True:
        col_str = input("What column? (1 - 7) ")
        if col_str.isdigit():
            col = int(col_str)
            if 1 <= col <= 7:
                print("\n")
                return col - 1
    
def printBoard():
    for row in board:
        print(row)
 
def dropPiece(board, col, player):
    for i in range(rows-1, -1, -1):
        if board[i][col] == ' ':
            board[i][col] = player
            break

def checkWin(board, piece):
    for r in range(rows):
        for c in range(cols - 3):
            if (
                board[r][c] == piece and
                board[r][c + 1] == piece and
                board[r][c + 2] == piece and
                board[r][c + 3] == piece
            ):
                return True

    for r in range(rows - 3):
        for c in range(cols):
            if (
                board[r][c] == piece and
                board[r + 1][c] == piece and
                board[r + 2][c] == piece and
                board[r + 3][c] == piece
            ):
                return True
            
    for r in range(rows - 3):
        for c in range(cols - 3):
            if (
                board[r][c] == piece and
                board[r + 1][c + 1] == piece and
                board[r + 2][c + 2] == piece and
                board[r + 3][c + 3] == piece
            ):
                return True

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


player = 'x'

while True:
    printBoard()
    dropCol = validateColumn()
    dropPiece(board, dropCol, player)
    if checkWin(board, player):
        print('Player: ' + player + ' wins!!!')
        break
    player = '%' if player == 'x' else 'x'