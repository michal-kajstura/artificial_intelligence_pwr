from operator import lt, gt
import numpy as np
import Assignment_3.minmax.heuristics as heur
from Assignment_3.connect4.player import Player


class MiniMax:
    def __init__(self, max_depth, maximizing_player, minimizing_player, heurstic_fcn):
        self._max_depth = max_depth
        self._maximizing_player = maximizing_player
        self._minimizing_player = minimizing_player
        self._heursitic_fcn = heurstic_fcn

    def __call__(self, board):
        _, best_col = self._minimax(board, self._max_depth, self._maximizing_player)
        print('')
        return best_col

    def _minimax(self, board, depth, player):
        if depth == 0:
            ai_score, human_score = self._heursitic_fcn(board)
            return ai_score - human_score, None

        if player == self._maximizing_player:
            fcn = max
            next_player = self._minimizing_player
        else:
            fcn = min
            next_player = self._maximizing_player

        valid_moves = [c for c in range(board.shape[1]) if board.array[0, c] == Player.EMPTY]
        np.random.shuffle(valid_moves)

        evaluations = []
        for column in valid_moves:
            row, col = board.drop_coin(column, player)
            player_won = board.check_board_state(row, column)

            if player_won:
                eval = np.inf if player == self._maximizing_player else -np.inf
            else:
                eval, _ = self._minimax(board, depth - 1, next_player)
            evaluations.append((column, eval))

            board.unset_field(column)

        print(player == self._maximizing_player, sorted(evaluations, key=lambda e: e[0]))
        e, c = fcn(evaluations, key=lambda e: e[1])
        print(e,c)
        return e,c
