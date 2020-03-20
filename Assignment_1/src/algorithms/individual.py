import numpy as np


class Individual:
    def __init__(self, genome=None, genome_len=None):
        self.genome = self._random_init(genome_len) if genome is None else genome
        self.fitness = 0

    @staticmethod
    def _random_init(genome_len):
        genome = np.arange(0, genome_len)
        np.random.shuffle(genome)
        return genome

    def copy(self):
        ind = Individual(genome=self.genome.copy())
        ind.fitness = self.fitness
        return ind

