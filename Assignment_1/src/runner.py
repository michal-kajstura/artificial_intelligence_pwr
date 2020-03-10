from Assignment_1.src.loading import DataLoader
from Assignment_1.src.logging import Logger


class Runner:
    def __init__(self, data_path, experiment_name):
        self.logger = Logger(experiment_name)
        loader = DataLoader()
        self.cities = loader.load_cities(data_path)

    def run(self, algorithm):
        return algorithm(self.cities, logger=self.logger)
