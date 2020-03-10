from Assignment_1.src.algorithms.genetic import GeneticAlgorithm
from Assignment_1.src.fitness import FitnessFunction
from Assignment_1.src.loading import DataLoader

path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_1/data/berlin11_modified.tsp'

loader = DataLoader()
cities = loader.load_cities(path)

config = {
    'population_size': 100,
    'crossover_probability': 0.7,
    'mutation_probability': 0.1,
    'tournament_size': 10
}

fitness_function = FitnessFunction(cities)
genetic = GeneticAlgorithm(cities, fitness_function, config)
genetic(1000)
