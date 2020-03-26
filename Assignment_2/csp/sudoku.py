from math import sqrt

import pandas as pd

from Assignment_2.csp.csp import CSPSolver


class Sudoku:
    def solve(self, puzzle):
        domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        domains = self._parse_puzzle(puzzle, domain)
        constraints = [self._columns_is_valid, self._row_is_valid, self._small_square_is_valid]
        solver = CSPSolver(domains, constraints)
        return solver.solve()

    @staticmethod
    def _parse_puzzle(puzzle, domain):
        def create_field(field):
            if field == '.':
                return domain
            else:
                return {int(field)}

        rows_cols_num = int(sqrt(len(puzzle)))
        return {(i, j): create_field(puzzle[i * rows_cols_num + j])
                for i in range(rows_cols_num)
                for j in range(rows_cols_num)}

    @staticmethod
    def _columns_is_valid(var, index, result):
        row, col = index
        for (r, c), v in result.items():
            if v == var and c == col and r != row:
                return False
        return True

    @staticmethod
    def _row_is_valid(var, index, result):
        row, col = index
        for (r, c), v in result.items():
            if v == var and c != col and r == row:
                return False
        return True

    @staticmethod
    def _small_square_is_valid(var, index, result):
        row, col = index
        small_square_row = row // 3
        small_square_col = col // 3
        for (r, c), v in result.items():
            if v == var \
                and r // 3 == small_square_row \
                and c // 3 == small_square_col\
                and c != col and r != row:
                return False
        return True


def print_sudoku(result):
        board = '\n'.join([' '.join([str(result.get((row, col), '.'))
                                    for col in range(9)]) for row in range(9)])
        print(board)

data_path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_2/data/Sudoku.csv'
data = pd.read_csv(data_path, sep=';')
puzzle = data.puzzle.iloc[0]

from time import time
s = time()
solved = Sudoku().solve(puzzle)
e = time()
print(e - s)
print_sudoku(solved)

