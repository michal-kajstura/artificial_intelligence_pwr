import json
from time import time

import pandas as pd

from Assignment_2.csp.sudoku import Sudoku

data_path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_2/data/Sudoku.csv'
data = pd.read_csv(data_path, sep=';', index_col='id')

results = dict()

for fc in [True, False]:
    for variable_heur in ['most_constrained', 'definition_order']:
        group_key = f'{fc}_{variable_heur}'
        results[group_key] = dict()
        for id_ in range(1, len(data) + 1):
            d = data.xs(id_)
            sudoku = Sudoku()
            solved = sudoku.solve(d.puzzle, forward_check=fc, domain_heuristic=variable_heur)
            logger = sudoku.solver.logger

            results[group_key][id_] = logger.log_to_file()
            results[group_key][id_]['difficulty'] = d.difficulty
            results[group_key][id_]['id'] = id_

with open('results_all.json', 'w') as file:
    json.dump(results, file, indent=2)
