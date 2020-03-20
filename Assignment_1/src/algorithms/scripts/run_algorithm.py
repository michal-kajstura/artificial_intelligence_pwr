from Assignment_1.src.algorithms.genetic import GeneticAlgorithm
from Assignment_1.src.logging import Logger
from Assignment_1.src.runner import Runner

path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_1/data/fl417.tsp'

config = {
    'population_size': 1000,
    'generations': 30,
    'crossover_probability': 0.0,
    'mutation_probability': 0.001,
    'tournament_size': 50,
    'greedy_init_percent': 0.1,
}

genetic = GeneticAlgorithm(config)
runner = Runner(path, Logger('b'))

route = runner.run(genetic)
print(route)

