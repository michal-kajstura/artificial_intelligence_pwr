from dataclasses import dataclass
from dataclasses import dataclass
from enum import IntEnum

import numpy as np

DOTS = 4
class Player(IntEnum):
    PLAYER1 = 1
    PLAYER2 = 2


class Board:
    def __init__(self, rows=6, columns=7):
        self._board = np.zeros((rows, columns), dtype=np.int8)

    def set_field(self, row, col, player):
        self._board[row, col] = player
        # heapq.heappush(self._taken_fields, Field(player, row, col))

    def get_field(self, row, col):
        return self._board[row, col]

    @property
    def shape(self):
        return self._board.shape

    def __getitem__(self, item):
        return self._board[item]

    def check_board_state(self, current_player):
        for (row, column), value in np.ndenumerate(self._board):
            if value != current_player:
                continue

            if self._check_diagonal(row, column):
                return True

            if self._check_rows(row, column):
                return True

            if self._check_cols(row, column):
                return True

        return False

    def _check_rows(self, row, col):
        rows, columns = self._board.shape
        if row > rows - DOTS:
            return False

        for current_row in range(row + 1, row + DOTS):
            if self._board[current_row, col] != self._board[current_row - 1, col]:
                return False

        return True

    def _check_cols(self, row, col):
        rows, columns = self._board.shape
        if col > columns - DOTS:
            return False

        for current_col in range(col + 1, col + DOTS):
            if self._board[row, current_col] != self._board[row, current_col - 1]:
                return False
        return True

    def _check_diagonal(self, row, col):
        rows, columns = self._board.shape

        win = False
        # check [1, 1] direction
        if row < rows - DOTS + 1 and col < columns - DOTS + 1:
            win = True
            for current_row, current_col in zip(range(row + 1, row + DOTS),
                                                range(col + 1, col + DOTS)):
                if (self._board[current_row, current_col]
                        != self._board[current_row - 1, current_col -1]):
                    return False

        # Check [-1, 1] direction
        if row >= DOTS and col < columns - DOTS + 1:
            win = True
            for current_row, current_col in zip(reversed(range(row - DOTS + 1, row)),
                                                range(col + 1, col + DOTS)):
                if (self._board[current_row, current_col]
                        != self._board[current_row + 1, current_col - 1]):
                    return False

        return win
