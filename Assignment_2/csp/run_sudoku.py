import pandas as pd

from Assignment_2.csp.sudoku import Sudoku, print_sudoku

data_path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_2/data/Sudoku.csv'
data = pd.read_csv(data_path, sep=';')

p = 0
puzzle = data.puzzle.iloc[p]
sudoku = Sudoku()
solved = sudoku.solve(puzzle)
print_sudoku(solved[0])

# logger = sudoku.solver.logger

PATH = 'results.csv'
# logger.log_to_file(PATH)

