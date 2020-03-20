import numpy as np
from scipy.spatial import distance_matrix


class GreedyAlgorithm:
    def __call__(self, cities, **kwargs):
        distance_matrix_ = distance_matrix(cities, cities)
        return [self.compute_route(city, distance_matrix_) for city in range(len(cities))]

    @staticmethod
    def compute_route(start_city, distance_matrix):
        distance_matrix = np.ma.array(distance_matrix.copy(),
                                      mask=np.zeros_like(distance_matrix))
        route = np.empty(distance_matrix.shape[0], dtype=np.uint32)
        visited_city = start_city

        visited_num = 0
        while visited_num < len(route):
            distance_matrix.mask[:, visited_city] = 1
            min_index = np.argmin(distance_matrix[visited_city])
            route[visited_num] = visited_city
            visited_num += 1
            visited_city = min_index

        return route
