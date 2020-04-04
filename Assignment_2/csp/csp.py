from copy import deepcopy
from itertools import tee
from typing import Set, Tuple, Dict, List, Callable, Any

from Assignment_2.csp.logger import CSVLogger


class CSPSolver:
    def __init__(self, domains: Dict[Tuple[int, int], Set[int]],
                 constraints: List[Callable[[Any, Any, Any], bool]]):
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        # Sort domains by length
        self.domains = {k: v for k, v in sorted(self.domains.items(), key=lambda i: len(i[1]))}

        self.all_solutions= []
        solution = dict()

        # self._forward_checking(result, self.domains)
        self._solve(solution, iter(self.domains))

        return self.all_solutions

    def _solve(self, solution, domains_left):
        domain_index = next(domains_left, None)

        # Solution found
        if domain_index is None:
            self.all_solutions.append(deepcopy(solution))
            return

        domain_values = self.domains[domain_index]
        for value in domain_values:
            if self._check_constraints(value, domain_index, solution):
                solution[domain_index] = value

                domain, domains_to_search = tee(domains_left)
                self._solve(solution, domains_to_search)
                solution.pop(domain_index)

    #
    # def _forward_checking(self, result, domains):
    #     def _check_domains(value, index):
    #         for domain in domains:
    #             for constraint in self.constraints:
    #                 if not constraint(value, index, result)
    #
    #     for index, value in result.items():



    def _check_constraints(self, var, index, result):
        for constraint in self.constraints:
            if not constraint(var, index, result):
                return False
        return True
