from copy import deepcopy

from Assignment_2.csp.logger import CSVLogger


class CSPSolver:
    def __init__(self, domains, constraints):
        self.domains = domains
        self.constraints = constraints
        self.logger = CSVLogger()

    def solve(self):
        self.domains = {k: v for k, v in sorted(self.domains.items(), key=lambda i: len(i[1]))}

        self.all_results = []
        result = dict()

        self.logger.start()
        self._solve(result, list(self.domains.items()))
        self.logger.end()

        return self.all_results

    def _solve(self, result, domains_left):
        if len(domains_left) > 0:
            index, domain = domains_left[0]
        else:
            self.all_results.append(deepcopy(result))
            self.logger.found_result()
            return

        for var in domain:
            self.logger.increment_tree_nodes_num()

            if self._check_constraints(var, index, result):
                result[index] = var
                self._solve(result, domains_left[1:])
                result.pop(index)

                self.logger.increment_backtrack_num()

    def _check_constraints(self, var, index, result):
        for constraint in self.constraints:
            if not constraint(var, index, result):
                return False
        return True
