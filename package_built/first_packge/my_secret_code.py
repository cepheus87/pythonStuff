import numpy as np


class SecretCode:

    def __init__(self):
        self.array = np.array([5])

    def show(self):
        print(f'My secret {type(self.array)}, {self.array}')
