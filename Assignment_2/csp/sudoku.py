from copy import deepcopy
from functools import partial
from math import sqrt

from Assignment_2.csp.csp import CSPSolver


class Sudoku:
    def solve(self, puzzle, **solver_kwargs):
        domain = set(range(1, 10))
        domains = self._parse_puzzle(puzzle, domain)

        # Constraints return iterable of conflicting cells.
        # If that iterable is empty the constraint is satisfied
        constraints = [partial(self._get_conflicting, self._conflicting_columns),
                       partial(self._get_conflicting, self._conflicting_rows),
                       partial(self._get_conflicting, self._conflicting_in_small_square)]
        self.solver = CSPSolver(domains, constraints, **solver_kwargs)
        return self.solver.solve()

    @staticmethod
    def _parse_puzzle(puzzle, domain):
        def create_field(field):
            if field == '.':
                return deepcopy(domain)
            else:
                return {int(field)}

        rows_cols_num = int(sqrt(len(puzzle)))
        return {(i, j): create_field(puzzle[i * rows_cols_num + j])
                for i in range(rows_cols_num)
                for j in range(rows_cols_num)}

    @staticmethod
    def _get_conflicting(predicate, field, result, is_domain=False):
        index, var = field
        row, col = index
        for (r, c), dom in result:
            is_in = var in dom if is_domain else var == dom
            if is_in and predicate(r, row, c, col):
                yield (r, c)

    @staticmethod
    def _conflicting_columns(r, row, c, col):
        return c == col and r != row

    @staticmethod
    def _conflicting_rows(r, row, c, col):
        return c != col and r == row

    @staticmethod
    def _conflicting_in_small_square(r, row, c, col):
        small_square_row = row // 3
        small_square_col = col // 3
        return (r // 3 == small_square_row
               and c // 3 == small_square_col
               and c != col and r != row)
