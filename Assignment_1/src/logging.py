from pathlib import Path
from Assignment_1.settings import EXPERIMENT_LOG_PATH


class Logger:
    def __init__(self, experiment_name):
        self.path = Path(EXPERIMENT_LOG_PATH).joinpath(experiment_name)
        self.path.mkdir(parents=True, exist_ok=True)
        self.values = []

    def log(self, value):
        self.values.append(value)
