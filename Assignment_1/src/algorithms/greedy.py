from numpy.linalg import norm


class GreedyAlgorithm:
    def __init__(self, cities):
        self.cities = cities

    def __call__(self, start_city):
        cities_to_visit = list(range(len(self.cities)))
        cities_to_visit.remove(start_city)

        current_city = start_city
        genome = [current_city]
        while cities_to_visit:
            distances = {
                c: norm(self.cities[current_city] - self.cities[c]) for c in cities_to_visit
            }
            current_city = min(distances, key=distances.get)
            cities_to_visit.remove(current_city)
            genome.append(current_city)

        return genome
