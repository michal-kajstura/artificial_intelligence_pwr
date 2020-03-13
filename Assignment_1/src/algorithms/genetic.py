import numpy as np

from Assignment_1.src.fitness import FitnessFunction


class GeneticAlgorithm:
    def __init__(self, config):
        self.config = config
        self.selector = Tournament(config['tournament_size'])
        self.best_ever = None

    def __call__(self, cities, **kwargs):
        self.fitness_function = FitnessFunction(cities)
        self._create_population(len(cities))
        self._evaluate_population()
        for _ in range(self.config['generations']):
            self.population = self._build_new_population()

            if 'logger' in kwargs.keys():
                fitnesses = [ind.fitness for ind in self.population]
                kwargs['logger'].log({
                    'best': min(fitnesses),
                    'worst': max(fitnesses),
                    'average': sum(fitnesses) / len(fitnesses)
                })

        return self.best_ever.genome

    def _create_population(self, genome_len):
        self.population = [Individual(genome_len=genome_len)
                           for _ in range(self.config['population_size'])]

    def _evaluate_population(self):
        for individual in self.population:
            individual.fitness = self.fitness_function(individual.genome)

    def _build_new_population(self):
        new_population = []
        while len(new_population) < len(self.population):
            first_individual = self.selector.select(self.population)
            second_individual = self.selector.select(self.population)

            if self._random(self.config['crossover_probability']):
                new_individual = first_individual.crossover(second_individual)
            else:
                new_individual = first_individual.copy()

            new_individual.mutate(self.config['mutation_probability'])

            new_individual.fitness = self.fitness_function(new_individual.genome)
            new_population.append(new_individual)

            if self.best_ever is None or new_individual.fitness > self.best_ever.fitness:
                self.best_ever = new_individual

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
        for mut in range(len(self.genome)):
            if np.random.rand() < mutation_prob:
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

    def copy(self):
        return Individual(genome=self.genome.copy())


class Tournament:
    def __init__(self, tournament_size=2):
        self.tournament_size = tournament_size

    def select(self, population):
        tournament = np.random.choice(population, self.tournament_size, replace=False)
        fitnesses = [ind.fitness for ind in tournament]
        idx = np.argmin(fitnesses)
        return tournament[idx]


