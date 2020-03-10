from Assignment_1.src.algorithms.genetic import GeneticAlgorithm
from Assignment_1.src.runner import Runner

path = '/home/michal/studia/SI/artificial_intelligence_pwr/Assignment_1/data/berlin11_modified.tsp'

config = {
    'population_size': 100,
    'generations': 100,
    'crossover_probability': 0.7,
    'mutation_probability': 0.1,
    'tournament_size': 10
}

genetic = GeneticAlgorithm(config)
runner = Runner(path, 'berlin_11')

route = runner.run(genetic)
print(route)

