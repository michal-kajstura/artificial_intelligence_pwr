from pathlib import Path
from Assignment_1.settings import EXPERIMENT_LOG_PATH


class Logger:
    def __init__(self, experiment_name, callbacks=()):
        self.path = Path(EXPERIMENT_LOG_PATH).joinpath(experiment_name)
        self.path.mkdir(parents=True, exist_ok=True)
        self.values = []
        self.callbacks = callbacks

    def log(self, value, individual):
        self.values.append(value)
        self.best_individual = individual
        for callback in self.callbacks:
            callback(self)
