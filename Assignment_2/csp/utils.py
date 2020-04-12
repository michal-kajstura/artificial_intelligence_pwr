import numpy as np


def print_sudoku(result):
    board = np.empty((9, 9), dtype='object')
    for row in range(9):
        for col in range(9):
            board[row, col] = str(result.get((row, col), '.'))

    board = np.insert(board, [3, 6], '―', axis=0)
    board = np.insert(board, [3, 6], '|', axis=1)
    board_str = '\n'.join(' '.join(list(row)) for row in board)
    print(board_str)

