def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q':  
            return False
        i -= 1
        j += 1
    return True

def solve_8queens(board, row):
    if row == 8:
        return True
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q' 
            if solve_8queens(board, row + 1):
                return True
            board[row][col] = '.'  
    return False

board = [['.' for i in range(8)] for i in range(8)]
if solve_8queens(board, 0):
    print("Solution for 8 queens problem:\n")
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists")
