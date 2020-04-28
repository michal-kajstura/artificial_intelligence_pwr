import unittest

from Assignment_3.connect4.board import Board, Player


def _fill_board(board, fields, player):
    for row, col in fields:
        board[row, col] = player


class TestBoard(unittest.TestCase):
    def test_init(self):
        _ = Board()

    def test_empty(self):
        board = Board()
        self.assertFalse(board.check_board_state(0, 0))

    def test_win_row(self):
        board = Board()
        _fill_board(board, [(3, 2), (3, 3), (3, 4), (3, 5)], Player.AI)

        self.assertTrue(
            board.check_board_state(5, 5)
        )

    def test_win_col(self):
        board = Board()
        _fill_board(board, [(0, 2), (1, 2), (2, 2), (3, 2)], Player.AI)

        self.assertTrue(
            board.check_board_state(Player.AI)
        )

    def test_win_diagonal(self):
        board = Board()
        _fill_board(board, [(1, 1), (2, 2), (3, 3), (4, 4)], Player.AI)

        self.assertTrue(
            board.check_board_state(Player.AI)
        )

    def test_not_win_first_player(self):
        board = Board()
        _fill_board(board, [(3, 2), (3, 3), (3, 4), (3, 6)], Player.AI)

        self.assertFalse(
            board.check_board_state(Player.AI)
        )


class TestGames(unittest.TestCase):
    def test_example_1(self):
        """"
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 1 0 0 0 0
        0 0 1 1 2 0 0
        0 0 2 2 1 0 0
        0 0 2 2 2 1 0
        """

        board = Board()
        _fill_board(board, [(2, 2), (3, 2), (3, 3), (4, 4), (5, 5)], Player.AI)
        _fill_board(board, [(3, 4), (4, 2), (4, 3), (5, 2), (5, 3), (5, 4)], Player.HUMAN)

        self.assertTrue(
            board.check_board_state(Player.AI)
        )

        self.assertFalse(
            board.check_board_state(Player.HUMAN)
        )

    def test_example_2(self):
        """"
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 1 0 0 0 0
        0 0 1 2 2 0 0
        0 0 2 2 1 0 0
        0 0 2 2 2 1 0
        """

        board = Board()
        _fill_board(board, [(2, 2), (3, 2), (4, 4), (5, 5)], Player.AI)
        _fill_board(board, [(3, 4), (3, 4), (4, 2), (4, 3), (5, 2), (5, 3), (5, 4)], Player.HUMAN)

        self.assertFalse(
            board.check_board_state(Player.AI)
        )

        self.assertFalse(
            board.check_board_state(Player.HUMAN)
        )

    def test_example_3(self):
        """"
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 1 0 0 0 0
        0 0 1 2 2 0 0
        0 0 2 2 1 0 0
        0 2 2 2 2 1 0
        """

        board = Board()
        _fill_board(board, [(2, 2), (3, 2), (4, 4), (5, 5)], Player.AI)
        _fill_board(board, [(3, 4), (3, 4), (4, 2), (4, 3), (5, 2), (5, 3), (5, 4), (5, 1)],
                    Player.HUMAN)

        self.assertFalse(
            board.check_board_state(Player.AI)
        )

        self.assertTrue(
            board.check_board_state(Player.HUMAN)
        )

    def test_example_4(self):
        """"
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 1 0 0 2 0
        0 0 1 2 2 0 0
        0 0 2 2 1 0 0
        0 0 2 2 2 1 0
        """

        board = Board()
        _fill_board(board, [(2, 2), (3, 2), (4, 4), (5, 5)], Player.AI)
        _fill_board(board, [(3, 4), (3, 4), (4, 2), (4, 3), (5, 2), (5, 3), (5, 4), (2, 5)],
                    Player.HUMAN)

        self.assertFalse(
            board.check_board_state(Player.AI)
        )

        self.assertTrue(
            board.check_board_state(Player.HUMAN)
        )

    def test_example_5(self):
        """"
        0 0 0 0 0 0 0
        0 0 0 1 0 0 0
        0 0 1 2 0 2 0
        0 1 1 2 0 0 0
        1 2 2 2 0 0 0
        2 2 1 2 0 1 0
        """

        board = Board()
        _fill_board(board,
                    [(1, 3), (2, 2), (3, 1), (4, 0), (3, 2), (5, 2), (5, 5), (2, 3), (4, 5)],
                    Player.AI)
        _fill_board(board, [(2, 5), (3, 3), (4, 1), (4, 2), (4,3), (5, 0), (5, 1), (5, 3), (3, 5)],
                    Player.HUMAN)

        self.assertTrue(
            board.check_board_state(Player.AI)
        )

        self.assertFalse(
            board.check_board_state(Player.HUMAN)
        )
