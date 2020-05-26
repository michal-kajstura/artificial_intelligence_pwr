from operator import le, ge

import numpy as np

from Assignment_3.connect4.player import Player


class MiniMax:
    def __init__(self, maximizing_player, minimizing_player, heurstic_fcn,
                 alpha_beta=False, max_depth=3):
        self._max_depth = max_depth
        self._maximizing_player = maximizing_player
        self._minimizing_player = minimizing_player
        self._heursitic_fcn = heurstic_fcn
        self._alpha_beta = alpha_beta

    def __call__(self, board):
        alpha, beta = (-np.inf, np.inf) if self._alpha_beta else (None, None)
        _, best_col = self._minimax(board, self._max_depth, self._maximizing_player, alpha, beta)
        return best_col

    def _minimax(self, board, depth, player, alpha=None, beta=None):
        if depth == 0:
            ai_score, human_score = self._heursitic_fcn(board)
            return ai_score - human_score, None

        # Check whether current players is maximizing or minimizing
        if player == self._maximizing_player:
            fcn = ge
            best_value = -np.inf
            next_player = self._minimizing_player
        else:
            fcn = le
            best_value = np.inf
            next_player = self._maximizing_player

        valid_moves = [c for c in range(board.shape[1]) if board.array[0, c] == Player.EMPTY]
        np.random.shuffle(valid_moves)

        best_col = 0
        for column in valid_moves:
            row, col = board.drop_coin(column, player)
            player_won = board.check_board_state(row, column)

            if player_won:
                value = np.inf if player == self._maximizing_player else -np.inf
            else:
                value, _ = self._minimax(board, depth - 1, next_player, alpha, beta)

            if fcn(value, best_value):
                best_col = column
                best_value = value

            if self._alpha_beta:
                if self._maximizing_player:
                    alpha = fcn(alpha, value)
                else:
                    beta = fcn(beta, value)

                # Alpha/Beta cutoff
                if alpha > beta:
                    break

            board.unset_field(row, col)

        return best_value, best_col
