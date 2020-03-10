import numpy as np


class GeneticAlgorithm:
    def __init__(self, cities, fitness_function, config):
        self.cities = cities
        self.fitness_function = fitness_function
        self.config = config
        self.population = [Individual(genome_len=len(cities))
                           for _ in range(config['population_size'])]
        self._evaluate_population()
        self.selector = Tournament(config['tournament_size'])

    def __call__(self, iterations=100):
        for _ in range(iterations):
            self.population = self._build_new_population()

    def _evaluate_population(self):
        for individual in self.population:
            individual.fitness = self.fitness_function(individual.genome)

    def _build_new_population(self):
        best_fitness = np.inf
        new_population = []
        while len(new_population) < len(self.population):
            first_individual = self.selector.select(self.population)
            second_individual = self.selector.select(self.population)

            if self._random(self.config['crossover_probability']):
                new_individual = first_individual.crossover(second_individual)
            else:
                first_individual.mutate(self.config['mutation_probability'])
                new_individual = first_individual

            new_individual.fitness = self.fitness_function(new_individual.genome)
            new_population.append(new_individual)
            if new_individual.fitness < best_fitness:
                best_fitness = new_individual.fitness

        print(best_fitness)
        return new_population

    @staticmethod
    def _random(probability):
        return np.random.rand() < probability

    def _mutate(self):
        for individual in self.population:
            individual.mutate(self.config['mutation_probability'])


class Individual:
    def __init__(self, genome=None, genome_len=None):
        self.genome = self._random_init(genome_len) if genome is None else genome
        self.fitness = 0
        self.index = np.arange(len(self.genome))

    @staticmethod
    def _random_init(genome_len):
        genome = np.arange(0, genome_len)
        np.random.shuffle(genome)
        return genome

    def mutate(self, mutation_prob):
        perform_mutation = np.random.rand(len(self.genome)) < mutation_prob

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
        crossover_point_1 = self._random_gene()
        crossover_point_2 = self._random_gene()

        if crossover_point_2 < crossover_point_1:
            crossover_point_1, crossover_point_2 = crossover_point_2, crossover_point_1

        first_parent_subset = self.genome[crossover_point_1: crossover_point_2]

        is_in = np.isin(other.genome, first_parent_subset)

        new_genome = self.genome.copy()
        new_genome[(self.index < crossover_point_1) |
                   (self.index >= crossover_point_2)] = other.genome[~is_in]
        return Individual(genome=new_genome)

    @staticmethod
    def _swap_genes(individual, first_half, second_half):
        individual.genome[:len(first_half)] = first_half
        individual.genome[:len(first_half)] = second_half


class Tournament:
    def __init__(self, tournament_size=2):
        self.tournament_size = tournament_size

    def select(self, population):
        tournament = np.random.choice(population, self.tournament_size)
        fitnesses = [ind.fitness for ind in tournament]
        idx = np.argmin(fitnesses)
        return tournament[idx]


