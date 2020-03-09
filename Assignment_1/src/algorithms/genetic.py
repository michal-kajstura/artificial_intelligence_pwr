import numpy as np


class GeneticAlgorithm:
    def __init__(self, cities, config):
        self.cities = cities
        self.config = config
        self.population = []
        self.selector = None

    def __call__(self, iterations=100):
        for _ in range(iterations):

    def _build_new_population(self):
        new_population = []
        while len(new_population) < len(self.population):
            first_individual = self.selector.select(self.population)
            second_individual = self.selector.select(self.population)

            if self._random(self.config.crossover_probability):
                first_individual.crossover(second_individual)
            else:
                first_individual.mutate()

            new_population.append(first_individual)
    @staticmethod
    def _random(probability):
        return np.random.rand() < probability

    def _mutate(self):
        for individual in self.population:
            individual.mutate()


class Individual:
    def __init__(self, genome_len):
        self.genome = self._random_init(genome_len)

    @staticmethod
    def _random_init(genome_len):
        genome = np.arange(0, genome_len)
        np.random.shuffle(genome)
        return genome

    def mutate(self, mutation_prob):
        perform_mutation = np.random.rand() < mutation_prob

        # TODO : Change this
        for mut in range(perform_mutation.sum()):
            first_swap_position = self._random_gene()
            second_swap_position = self._random_gene()
            temp = self.genome[first_swap_position]
            self.genome[first_swap_position] = self.genome[second_swap_position]
            self.genome[second_swap_position] = temp


    def _random_gene(self):
        return np.random.randint(0, len(self.genome))

    def crossover(self, other):
        crossover_point = self._random_gene()
        first_half_1, second_half_1 = self.genome[:crossover_point], self.genome[crossover_point:]
        first_half_2, second_half_2 = other.genome[crossover_point:], other.genome[:crossover_point]

        self._swap_genes(self, first_half_1, second_half_2)
        self._swap_genes(other, first_half_2, second_half_1)

    @staticmethod
    def _swap_genes(individual, first_half, second_half):
        individual.genome[:len(first_half)] = first_half
        individual.genome[:len(first_half)] = second_half




