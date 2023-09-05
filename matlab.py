import random
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, dimension, steps):
        self.dimension = dimension
        self.steps = steps
        self.cordinet_system = [[0 for step in range(self.steps)] for dim in range(self.dimension)]

    def walk(self):
        for step in range(self.steps):
            random_dim = random.randint(1, self.dimension - 1)
            for dim in range(self.dimension):
                spec_dim = self.cordinet_system[dim]
                spec_dim[step] = spec_dim[step - 1]
                if dim == random_dim:
                    spec_dim[step] = spec_dim[step - 1] + move_random()

    def move_random(self):
        tossing_coin = random.random()
        return 1 if tossing_coin > 0.5 else -1

    def display(self):
        if self.dimension == 1:
            plt.plat([step for step in range(self.steps)], self.cordinet_system[0])
        elif self.dimension == 2:
            pass
        elif self.dimension == 3:
            pass
        else:
            pass


tes = RandomWalk(1, 10)
