from time import time

from Assignment_3.algorithms.monte_carlo import MCTS
from Assignment_3.connect4.player import Player
from Assignment_3.connect4.board import Board
from Assignment_3.algorithms.heuristics import heuristic
from Assignment_3.algorithms.minmax import MiniMax


class Game:
    def __init__(self, algorithm_params=dict(), mode='Human vs AI', algorithm='Minmax'):
        self._board = Board()
        if algorithm == 'Minmax':
            self._algorithm = MiniMax(Player.AI, Player.HUMAN, heuristic, **algorithm_params)
        elif algorithm == 'Alpha-beta pruning':
            self._algorithm = MiniMax(Player.AI, Player.HUMAN, heuristic, alpha_beta=True, **algorithm_params)
        elif algorithm == 'MCTS':
            self._algorithm = MCTS(1000, 2)
        else:
            raise ValueError(f"Algorithm {algorithm} not known")

        self._last_move = None
        if mode == 'AI vs AI':
            self._second_algo = MiniMax(Player.HUMAN, Player.AI,
                                        heuristic, **algorithm_params)

        self._start_time = None
        self._total_time = None

    def ai_move(self):
        column = self._algorithm(self._board)
        self._last_move = self._board.drop_coin(column, Player.AI)

    def player_move(self, column):
        if self._start_time is None:
            self._start_time = time()

        if column is None:
            column = self._second_algo(self._board)

        self._last_move = self._board.drop_coin(column, Player.HUMAN)

    def check_end(self):
        if self._last_move is None:
            return False

        end = self._board.check_board_state(*self._last_move)
        return end


