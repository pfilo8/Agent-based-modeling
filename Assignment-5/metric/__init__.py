import numpy as np


def calculate_average_speed(agents):
    return np.mean([agent.speed for agent in agents])
