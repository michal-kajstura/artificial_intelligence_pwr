from Assignment_1.src.loading import DataLoader


class Runner:
    def __init__(self, data_path, logger):
        self.logger = logger
        loader = DataLoader()
        self.cities = loader.load_cities(data_path)

    def run(self, algorithm):
        return algorithm(self.cities, logger=self.logger)
