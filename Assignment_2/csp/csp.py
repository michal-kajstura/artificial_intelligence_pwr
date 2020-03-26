class CSPSolver:
    def __init__(self, domains, constraints):
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        result = dict()
        result = {k: next(iter(v)) for k, v in self.domains.items() if len(v) == 1}
        for k in result.keys():
            self.domains.pop(k)

        self._solve(result, list(self.domains.items()))
        return result

    def _solve(self, result, domains_left):
        if len(domains_left) > 0:
            index, domain = domains_left[0]
        else:
            return True

        for var in domain:
            if self._check_constraints(var, index, result):
                result[index] = var
                if self._solve(result, domains_left[1:]):
                    return True
                result.pop(index)

    def _check_constraints(self, var, index, result):
        for constraint in self.constraints:
            if not constraint(var, index, result):
                return False
        return True


def print_sudoku(result):
        board = '\n'.join([' '.join([str(result.get((row, col), '.'))
                                    for col in range(9)]) for row in range(9)])
        print(board)