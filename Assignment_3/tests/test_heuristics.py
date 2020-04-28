import unittest

from Assignment_3.connect4.board import Board
from Assignment_3.connect4.player import Player
from Assignment_3.minmax.heuristics import count_columns, count_rows, count_diagonals
from Assignment_3.tests.test_board import _fill_board
import numpy as np


class TestHeuristics(unittest.TestCase):

    def test_rows(self):
        board = Board()

        # 3s
        _fill_board(board, [(5, 0), (5, 1), (5, 2)], Player.AI)
        _fill_board(board, [(0, 0), (0, 1), (0, 2)], Player.AI)

        # 2s
        _fill_board(board, [(0, 4), (0, 5)], Player.AI)
        _fill_board(board, [(1, 5), (1, 6)], Player.AI)
        _fill_board(board, [(4, 0), (4, 1)], Player.AI)
        _fill_board(board, [(4, 4), (4, 5)], Player.AI)

        #1s
        _fill_board(board, [(2, 4)], Player.AI)

        cols = count_rows(board)

        self.assertDictEqual(cols[Player.AI], {
            3: 2, 2: 4
        })


    def test_cols(self):
        board = Board()

        # 3s
        _fill_board(board, [(0, 0), (1, 0), (2, 0)], Player.AI)

        # 2s
        _fill_board(board, [(0, 3), (1, 3)], Player.AI)
        _fill_board(board, [(4, 3), (5, 3)], Player.AI)
        _fill_board(board, [(4, 5), (5, 5)], Player.AI)

        #1s
        _fill_board(board, [(2, 4)], Player.AI)

        cols = count_columns(board, Player.AI)

        self.assertDictEqual(cols, {
            3: 1, 2: 3
        })

    def test_diagonal(self):
        board = Board()
        board._board = np.array([
            [1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 1, 1],
        ])

        actual = count_diagonals(board, Player.AI)
        self.assertDictEqual(actual, {4:1, 3: 1,  2: 2})


    def test_diagonal_downwards(self):
        board = Board()
        board._board = np.array([
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 0],
        ])

        actual = count_diagonals(board, Player.AI)
        self.assertDictEqual(actual, {3: 1, 4: 1, 2: 1})


    def test_diagonal_all(self):
        board = Board()
        board._board = np.array([
            [0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 0],
        ])

        actual = count_diagonals(board, Player.AI)
        self.assertDictEqual(actual, {3: 4, 4: 1, 2: 2})