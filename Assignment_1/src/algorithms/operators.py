import numpy as np

from Assignment_1.src.algorithms.genetic import Individual


def swap_mutation(individual):
    genome = individual.genome
    first_swap_position, second_swap_position = _get_random_points(len(genome))
    temp = genome[first_swap_position]
    genome[first_swap_position] = genome[second_swap_position]
    genome[second_swap_position] = temp


def reverse_mutation(individual):
    genome = individual.genome
    first_swap_position, second_swap_position = _get_random_points(len(genome))
    genome[first_swap_position: second_swap_position] = np.flip(genome[first_swap_position:
                                                                       second_swap_position])


def ordered_crossover(first_individual, second_individual):
    genome_length = len(first_individual.genome)
    crossover_point_1, crossover_point_2 = _get_random_points(genome_length)
    first_parent_subset = first_individual.genome[crossover_point_1: crossover_point_2]

    is_in_first_parent = np.isin(second_individual.genome, first_parent_subset)

    index = np.arange(genome_length)
    new_genome = first_individual.genome.copy()
    new_genome[(index < crossover_point_1) |
               (index >= crossover_point_2)] = second_individual.genome[~is_in_first_parent]
    return Individual(genome=new_genome)



def tournament(population, tournament_size):
    tournament = population[np.random.randint(0, len(population), tournament_size)]
    idx = np.argmin([ind.fitness for ind in tournament])
    return tournament[idx]


def _get_random_points(genome_length):
    crossover_point_1 = np.random.randint(0, genome_length)
    crossover_point_2 = np.random.randint(0, genome_length)

    if crossover_point_2 < crossover_point_1:
        crossover_point_1, crossover_point_2 = crossover_point_2, crossover_point_1
    return crossover_point_1, crossover_point_2


def roulette(population):
    fitnesses = np.array([ind.fitness for ind in population])
    fitnesses = fitnesses.max() - fitnesses
    probabilities = fitnesses / fitnesses.sum()
    idx = np.random.choice(np.arange(len(population)), p=probabilities)
    return population[idx]