from time import time

import pandas as pd

from Assignment_2.csp.sudoku import Sudoku
from Assignment_2.csp.utils import print_sudoku

data_path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_2/data/Sudoku.csv'
data = pd.read_csv(data_path, sep=';')

# for  p in range(10):
puzzle = data.puzzle.iloc[30]
sudoku = Sudoku()

solved = sudoku.solve(puzzle, True)
logger = sudoku.solver.logger
for i, j in logger.log_to_file().items():
    print(i, j)

print('\n')
sudoku = Sudoku()
solved = sudoku.solve(puzzle, False)
logger = sudoku.solver.logger
for i, j in logger.log_to_file().items():
    print(i, j)
#     logger = sudoku.solver.logger
#
#     PATH = 'results1.csv'
#     logger.log_to_file(PATH)

# pd.read_csv('results.csv').to_latex('resutlslatex.txt')
