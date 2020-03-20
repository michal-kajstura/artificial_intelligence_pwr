import numpy as np

from Assignment_1.src.algorithms.greedy import GreedyAlgorithm
from Assignment_1.src.algorithms.individual import Individual
from Assignment_1.src.algorithms.operators import ordered_crossover, tournament, reverse_mutation
from Assignment_1.src.fitness import FitnessFunction


class GeneticAlgorithm:
    def __init__(self, config, mutation_fcn=reverse_mutation,
                 crossover_fcn=ordered_crossover,
                 imp_th=40):
        self.config = config
        self.selector = lambda t: tournament(t, config['tournament_size'])
        self.mutation_prob = config['mutation_probability']
        self.best_ever = None
        self.crossover = crossover_fcn
        self.mutation = mutation_fcn
        self.population = []
        self.generations_without_improvement = 0
        self.imp_th = imp_th

    def __call__(self, cities, **kwargs):
        self.fitness_function = FitnessFunction(cities)
        pop_size = self.config['population_size']
        self.population = self._create_population(len(cities), pop_size)
        if self.config.get('greedy_init_percent', 0) > 0:
            self._add_greedy(cities, self.config['greedy_init_percent'])

        for _ in range(self.config['generations']):
            self.population = self._build_new_population()

            if 'logger' in kwargs.keys():
                fitnesses = [ind.fitness for ind in self.population]
                kwargs['logger'].log({
                    'best': min(fitnesses),
                    'worst': max(fitnesses),
                    'average': sum(fitnesses) / len(fitnesses)
                }, self.best_ever)


        return self.best_ever.genome

    def _create_population(self, genome_len, size):
        population = np.empty(self.config['population_size'], dtype=object)
        for i in range(size):
            individual = Individual(genome_len=genome_len)
            individual.fitness = self.fitness_function(individual.genome)
            population[i] = individual
        return population

    def _add_greedy(self, cities, percent):
        greedy = GreedyAlgorithm()
        greedy_individuals = [Individual(genome=g) for g in greedy(cities)]
        for g in greedy_individuals:
            g.fitness = self.fitness_function(g.genome)
        greedy_num = min(len(greedy_individuals), percent * len(greedy_individuals))
        for i, g in enumerate(sorted(greedy_individuals, key=lambda g: g.fitness)):
            if i > greedy_num:
                break
            self.population[i] = g



    def _build_new_population(self):
        new_population = np.empty(self.config['population_size'], dtype=object)
        new_individuals_num = 0
        while new_individuals_num < self.config['population_size']:
            first_individual = self.selector(self.population)
            second_individual = self.selector(self.population)

            if self._random(self.config['crossover_probability']):
                new_individual = self.crossover(first_individual, second_individual)
            else:
                new_individual = first_individual.copy()

            self._mutate(new_individual)

            new_individual.fitness = self.fitness_function(new_individual.genome)
            new_population[new_individuals_num] = new_individual

            if self.best_ever is None or new_individual.fitness < self.best_ever.fitness:
                self.best_ever = new_individual.copy()

            new_individuals_num += 1

        return new_population

    @staticmethod
    def _random(probability):
        return np.random.rand() < probability

    def _mutate(self, individual):
        if np.random.rand() < self.mutation_prob:
            self.mutation(individual)
