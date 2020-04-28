import unittest

from Assignment_3.connect4.board import Board
from Assignment_3.connect4.player import Player
from Assignment_3.minmax.heuristics import count_columns, count_rows, count_diagonals
from Assignment_3.tests.test_board import _fill_board
import numpy as np


class TestHeuristics(unittest.TestCase):

    def test_rows(self):
        board = Board()

        board._board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 2, 2, 0],
        ])

        result = count_rows(board)

        self.assertDictEqual(result[Player.AI], {
            3: 1,
        })
        self.assertDictEqual(result[Player.HUMAN], {
            2: 1
        })

    def test_rows_complicated(self):
        board = Board()

        board._board = np.array([
            [2, 1, 2, 0, 0, 0, 0],
            [2, 1, 2, 2, 1, 0, 0],
            [1, 1, 1, 2, 2, 2, 0],
        ])

        result = count_rows(board.array)

        self.assertDictEqual(result[Player.AI], dict()
        )
        self.assertDictEqual(result[Player.HUMAN], {
            3: 1, 1:1
        })

    def test_cols(self):
        board = Board()

        board._board = np.array([
            [2, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 2, 0, 0, 0, 1],
            [1, 2, 2, 0, 0, 0, 1],
        ])

        result = count_columns(board.array)

        self.assertDictEqual(result[Player.AI], {
            4: 2, 3: 1, 2: 1
        })
        self.assertDictEqual(result[Player.HUMAN], {
            2: 1, 1:1
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

        actual = count_diagonals(board.array)
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