import numpy as np
from statistics import mean


def choosing_distribution(distribution, type):
    size = 10
    if type == 'color':
        loc = 3
        scale = 2
        low = 0
        high = 5
    elif type == 'rotation':
        loc = 187
        scale = 170
        low = 15
        high = 360
    elif type == 'background':
        loc = 5
        scale = 4
        low = 1
        high = 10
    elif type == 'size':
        loc = 8
        scale = 6
        low = 2
        high = 15

    if distribution == 'normal':
        distribution_array = np.random.normal(loc, scale, size)
    elif distribution == 'exponential':
        distribution_array = np.random.exponential(scale, size)
    elif distribution == 'uniform':
        distribution_array = np.random.uniform(low, high, size=1)

    distribution_parameter = mean(distribution_array)
    print(round(distribution_parameter))


choosing_distribution('normal', 'rotation')
