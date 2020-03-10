import numpy as np


class RandomAlgorithm:
    def __call__(self, cities, **kwargs):
        genome = np.arange(len(cities))
        np.random.shuffle(genome)
        return genome
