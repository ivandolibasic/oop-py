def check_winner(board):
    # row check
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '?':
            return row[0]

    # column check
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '?':
            return board[0][col]

    # diagonal check
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '?':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '?':
        return board[0][2]

    return '-'

test_cases = [
    [['x', 'x', 'x'], ['o', 'o', '?'], ['?', '?', '?']],  # winner: x
    [['o', 'x', 'x'], ['o', 'x', '?'], ['o', '?', '?']],  # winner: o
    [['x', 'o', '?'], ['o', 'x', '?'], ['?', '?', 'x']],  # winner: x
    [['x', 'x', 'o'], ['o', 'o', 'x'], ['x', 'o', 'x']],  # no contest
]

for i, board in enumerate(test_cases):
    print(f"Test case {i + 1}: {check_winner(board)}")
