from collections import defaultdict, Counter

import numpy as np

from Assignment_3.connect4.player import Player


def heuristic(board):
    scoring = {
        1: 0,
        2: 10,
        3: 30,
        4: np.inf,
    }

    ai_score = 0
    human_score = 0
    for h in (count_rows, count_columns, count_diagonals):
        counts = h(board.array)
        for k, v in counts[Player.AI].items():
            ai_score += scoring[k] * v
        for k, v in counts[Player.HUMAN].items():
            human_score += scoring[k] * v

    return ai_score, human_score


def count_columns(board):
    return count_rows(board.T)


def count_rows(board):
    counts = {Player.HUMAN: defaultdict(int),
              Player.AI: defaultdict(int)}

    for row in board:
        for c in range(0, len(row) - 3):
            window = row[c: c + 4]
            counted = Counter(window)
            if counted.get(Player.AI) is None and counted.get(Player.HUMAN) is not None:
                counts[Player.HUMAN][counted[Player.HUMAN]] += 1

            if counted.get(Player.HUMAN) is None and counted.get(Player.AI) is not None:
                counts[Player.AI][counted[Player.AI]] += 1

    return counts


def _add_dicts(d1, d2):
    for k, v in d1.items():
        d1[k] += d2.get(k, 0)
    return d1


def count_diagonals(board):
    downwards_diagonals = _count_diagonals(board)
    upwards_diagonals = _count_diagonals(np.rot90(board))

    all_diagonals = {
        Player.HUMAN: _add_dicts(downwards_diagonals[Player.HUMAN],
                                 upwards_diagonals[Player.HUMAN]),
        Player.AI: _add_dicts(downwards_diagonals[Player.AI],
                              upwards_diagonals[Player.AI]),
    }

    return all_diagonals


def _count_diagonals(board):
    counts = {Player.HUMAN: defaultdict(int),
              Player.AI: defaultdict(int)}

    rows, cols = board.shape

    for d in range(-cols + 4, cols - 3):
        diagonal = np.diag(board, d)
        if len(diagonal) < 4:
            continue

        for c in range(0, len(diagonal) - 3):
            window = diagonal[c: c + 4]
            counted = Counter(window)
            if counted.get(Player.AI) is None and counted.get(Player.HUMAN) is not None:
                counts[Player.HUMAN][counted[Player.HUMAN]] += 1

            if counted.get(Player.HUMAN) is None and counted.get(Player.AI) is not None:
                counts[Player.AI][counted[Player.AI]] += 1

    return counts
