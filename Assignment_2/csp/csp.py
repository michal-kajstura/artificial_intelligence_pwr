from copy import deepcopy
from itertools import chain

from Assignment_2.csp.logger import CSVLogger
from Assignment_2.csp.utils import print_sudoku


class CSPSolver:
    def __init__(self, domains,
                 constraints,
                 forward_check=True):
        self.domains = domains
        self.constraints = constraints
        self.logger = CSVLogger()
        self._forward_check = forward_check

    def solve(self):
        self.all_solutions= []

        self.logger.start()

        solution = {k: list(v)[0] for k, v in self.domains.items() if len(v) == 1}
        domains = [(k, v) for k, v in self.domains.items() if len(v) != 1]

        if self._forward_check:
            for field in solution.items():
                _= self._forward_checking(field, domains)

        self._solve(solution, domains)
        self.logger.end()

        return self.all_solutions

    def _solve(self, solution, domains_left):

        # Solution found
        if len(domains_left) == 0:
            self.all_solutions.append(deepcopy(solution))
            self.logger.found_result()
            return

        domain_index, domain_values = domains_left[0]

        for value in domain_values:
            self.logger.increment_tree_nodes_num()

            if self._check_constraints((domain_index, value), solution):
                solution[domain_index] = value

                discarded = []
                if self._forward_check:
                    discarded = self._forward_checking((domain_index, value), domains_left[1:])
                domains_to_search = domains_left[1:]

                self._solve(solution, domains_to_search)

                self.logger.increment_backtrack_num()
                solution.pop(domain_index)

                for disc in discarded:
                    for idx, dom in domains_left:
                        if idx == disc:
                            dom.add(value)

    def _forward_checking(self, last_field, domains):
        cells_to_remove = chain.from_iterable(
            list(c(last_field, domains, is_domain=True)) for c in self.constraints)
        cells_to_remove = set(cells_to_remove)

        _, value = last_field
        discarded = []
        for domain_index, domain_values in domains:
            if domain_index in cells_to_remove:
                domain_values.discard(value)
                discarded.append(domain_index)
        return discarded

    def _check_constraints(self, field, result):
        result_items = result.items()
        for constraint in self.constraints:
            try:
                next(constraint(field, result_items))
                return False
            except StopIteration:
                pass
        return True
