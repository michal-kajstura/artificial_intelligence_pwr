import numpy as np


class DataLoader:

    def __init__(self, header_size=6, eof_size=2):
        self.header_size = header_size
        self.eof_size = eof_size

    def load_cities(self, path):
        with open(path, 'r') as file:
            raw_data = file.readlines()

        content = raw_data[self.header_size: -self.eof_size]
        content = [self._process_line(l) for l in content]
        content = np.array(content)

        return content

    @staticmethod
    def _process_line(line):
        _, lat, lon = line.split()
        return float(lat), float(lon)