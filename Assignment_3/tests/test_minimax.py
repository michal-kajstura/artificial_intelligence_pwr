import unittest

from Assignment_3.connect4.board import Board
from Assignment_3.connect4.player import Player
from Assignment_3.algorithms.heuristics import heuristic
from Assignment_3.algorithms.minmax import MiniMax
from Assignment_3.tests.test_board import _fill_board


class TestMinimax(unittest.TestCase):

    def test_block(self):
        board = Board()
        _fill_board(board, [(5, 0), (5, 1), (5, 2)], Player.HUMAN)

        minimax = MiniMax(4, Player.AI, Player.HUMAN, heuristic)
        column = minimax(board)
        self.assertEqual(3, column)

    def test_block2(self):
        board = Board()
        _fill_board(board, [(5, 0), (5, 2), (5, 3)], Player.AI)

        minimax = MiniMax(3, Player.HUMAN, Player.AI, heuristic)
        column = minimax(board)
        self.assertEqual(1, column)

    def test_attack(self):
        board = Board()
        _fill_board(board, [(5, 0), (5, 2), (5, 3)], Player.HUMAN)

        minimax = MiniMax(4, Player.HUMAN, Player.AI, heuristic)
        column = minimax(board)
        self.assertEqual(1, column)

    def test_attack_or_block(self):
        board = Board()
        _fill_board(board, [(5, 0), (5, 1)], Player.AI)
        _fill_board(board, [(5, 4), (5, 5), (5, 6)], Player.HUMAN)

        minimax = MiniMax(3, Player.AI, Player.HUMAN, heuristic)
        column = minimax(board)
        self.assertEqual(3, column)