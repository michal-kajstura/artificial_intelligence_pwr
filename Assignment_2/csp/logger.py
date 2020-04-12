import csv
from pathlib import Path
from time import time


class Logger:
    def __init__(self):
        self._start_time = 0
        self.first_result_time = 0
        self.first_result_backtracks_num = 0
        self.first_result_node_num = 0
        self.total_time = 0
        self.backtracks_num = 0
        self.tree_nodes_num = 0
        self.num_of_solutions = 0

    def increment_backtrack_num(self):
        self.backtracks_num += 1

    def increment_tree_nodes_num(self):
        self.tree_nodes_num += 1

    def found_result(self):
        if self.num_of_solutions == 0:
            self.first_result_backtracks_num = self.backtracks_num
            self.first_result_time = time() - self._start_time
            self.first_result_node_num = self.tree_nodes_num
        self.num_of_solutions += 1


    def start(self):
        self._start_time = time()

    def end(self):
        self.total_time = time() - self._start_time


class CSVLogger(Logger):
    def log_to_file(self):
        to_write = {
            'first_sol_time': self.first_result_time,
            'first_sol_node_num': self.first_result_node_num,
            'first_sol_backtrack_num': self.first_result_backtracks_num,
            'total_time': self.total_time,
            'total_node_num': self.tree_nodes_num,
            'total_backtrack_num': self.backtracks_num,
            'num_of_solutions': self.num_of_solutions
        }
        return to_write
        # with open(filepath, 'a') as file:
        #     writer = csv.DictWriter(file, to_write.keys())
        #     if not path_exist:
        #         writer.writeheader()
        #     writer.writerow(to_write)

