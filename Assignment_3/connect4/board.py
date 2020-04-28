import numpy as np

from Assignment_3.connect4.player import Player

DOTS = 4


class Board:
    def __init__(self, rows=6, columns=7):
        self._board = np.zeros((rows, columns), dtype=np.int8)
        self._last_dropped = []

    def drop_coin(self, column, player):
        rows = self._board.shape[0]

        for row in reversed(range(rows)):
            if self._board[row, column] == Player.EMPTY:
                self._board[row, column] = player
                return row, column

    def unset_field(self, column):
        rows = self._board.shape[0]

        for row in range(rows):
            if self._board[row, column] != Player.EMPTY:
                self._board[row, column] = Player.EMPTY
                break

    @property
    def array(self):
        return self._board

    @property
    def shape(self):
        return self._board.shape

    def __getitem__(self, item):
        return self._board[item]

    def __setitem__(self, key, value):
        self._board[key] = value

    @property
    def transpose(self):
        return self._board.T

    def check_board_state(self, row, column):
        num_rows, num_cols = self._board.shape

        min_row = max(row - 4, 0)
        max_row = min(row + 4, num_rows)
        column_slice = self._board[min_row : max_row, column]

        min_col = max(column - 4, 0)
        max_col = min(column + 4, num_cols)
        row_slice = self._board[row, min_col: max_col]

        diagonal_slice = [self._board[row + i,  column + i]
                            for i in range(-min(3, row, column),
                                           min(4, num_rows - row, num_cols - column))]

        diagonal_slice_reversed = [self._board[row + i,  column - i]
                                     for i in range(-min(3, row, num_cols - column - 1),
                                                    min(4, num_rows - row, column + 1))]

        return any(self._check_slice(s) for s in (column_slice, row_slice,
                                                  diagonal_slice, diagonal_slice_reversed))

    def _check_slice(self, slice):
        counter = 0
        for i in range(1, len(slice)):
            if slice[i] != Player.EMPTY and slice[i - 1] == slice[i]:
                counter += 1
            else:
                counter = 0

            if counter == 3:
                return True
        return False
