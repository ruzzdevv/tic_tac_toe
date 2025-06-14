def check_winner(board, player):
    return any(
        all(cell == player for cell in row) for row in board
    ) or any(
        all(board[r][c] == player for r in range(3)) for c in range(3)
    ) or all(
        board[i][i] == player for i in range(3)
    ) or all(
        board[i][2 - i] == player for i in range(3)
    )

def is_draw(board):
    return all(cell != "" for row in board for cell in row)
