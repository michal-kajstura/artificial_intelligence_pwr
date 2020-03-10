from numpy.linalg import norm
from scipy.spatial import distance_matrix


class FitnessFunction:
    def __init__(self, cities):
        self.distance_matrix = distance_matrix(cities, cities)

    def __call__(self, genome):
        route_length = self.distance_matrix[genome[:-1], genome[1:]].sum()
        route_length += self.distance_matrix[genome[0], genome[-1]]
        return route_length
