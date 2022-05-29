import numpy as np
from statistics import mean


def choosing_distribution(distribution):
    if distribution == 'normal':
        distribution_array = np.random.normal(loc=3, scale=2, size=10)
    elif distribution == 'exponential':
        distribution_array = np.random.exponential(scale=2, size=10)
    elif distribution == 'uniform':
        distribution_array = np.random.uniform(low=1, high=5, size=1)

    distribution_parameter = mean(distribution_array)
    return round(distribution_parameter)
