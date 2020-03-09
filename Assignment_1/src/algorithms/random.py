import numpy as np


class RandomAlgorithm:
    def __init__(self, cities):
        self.cities = cities

    def __call__(self):
        genome = np.arange(len(self.cities))
        np.random.shuffle(genome)
        return genome
