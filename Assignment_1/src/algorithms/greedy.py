import numpy as np
from numpy.linalg import norm

from Assignment_1.src.fitness import FitnessFunction


class GreedyAlgorithm:
    def __call__(self, cities, **kwargs):
        fitness_function = FitnessFunction(cities)
        best_route = None
        best_fitness = np.inf

        for city in range(len(cities)):
            route = self._compute_route(cities, city)
            fitness = fitness_function(route)
            if fitness < best_fitness:
                best_fitness = fitness
                best_route = route

        return best_route

    @staticmethod
    def _compute_route(cities, start_city):
        cities_to_visit = list(range(len(cities)))
        cities_to_visit.remove(start_city)

        current_city = start_city
        route = [current_city]
        while cities_to_visit:
            distances = {
                c: norm(cities[current_city] - cities[c]) for c in cities_to_visit
            }
            current_city = min(distances, key=distances.get)
            cities_to_visit.remove(current_city)
            route.append(current_city)

        return route
