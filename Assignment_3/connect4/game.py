from Assignment_3.connect4.player import Player
from Assignment_3.connect4.board import Board
from Assignment_3.minmax.heuristics import heuristic
from Assignment_3.minmax.minmax import MiniMax


class Game:
    def __init__(self):
        self._board = Board()
        self._minimax = MiniMax(4, Player.AI, Player.HUMAN, heuristic)
        self._last_move = None

    def ai_move(self):
        column = self._minimax(self._board)
        self._last_move = self._board.drop_coin(column, Player.AI)

    def player_move(self, column):
        self._last_move = self._board.drop_coin(column, Player.HUMAN)

    def check_end(self):
        return self._board.check_board_state(*self._last_move)


