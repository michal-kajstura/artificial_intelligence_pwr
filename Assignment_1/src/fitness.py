from numpy.linalg import norm


class FitnessFunction:
    def __init__(self, cities):
        self.cities = cities

    def __call__(self, genome):
        sorted_cities = self.cities[genome]
        s1 = sorted_cities[1:]
        s2 = sorted_cities[:-1]
        distance = norm(s1 - s2, axis=1).sum()
        distance += norm(sorted_cities[-1] - sorted_cities[0])
        return distance
