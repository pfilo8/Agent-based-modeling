from functools import partial

import pandas as pd
import numpy as np

from config.PopulationConfiguration import PopulationConfiguration
from model.SchellingModel import SchellingModel

height, width = 100, 100
BaselineSchelingModel = partial(SchellingModel, height=height, width=width)


def calculate_happiness(agent, model):
    neighbour_color = [neighbour.color == agent.color for neighbour in model.grid.iter_neighbors(agent.pos, moore=True)]
    return np.mean(neighbour_color) if len(neighbour_color) > 0 else int(agent.lonely_happy)


def calculate_segregation(model):
    return np.mean([calculate_happiness(agent, model) for agent in model.schedule.agents])


def run_experiment_iterations():
    ns = []
    its = []

    for n in range(250, 4050, 50):
        print(f'Iterations experiment. n = {n}')
        populations = [
            PopulationConfiguration("red", n, 0.5),
            PopulationConfiguration("blue", n, 0.5)
        ]

        model = BaselineSchelingModel(populations=populations)
        model.run_model()
        ns.append(n)
        its.append(model.iteration)

    pd.DataFrame({
        'n': ns,
        'iterations': its
    }).to_csv('outputs/experiment_iterations.csv', index=False)


def run_experiment_segregation_j():
    js = []
    segs = []

    for j in np.arange(0.1, 0.95, 0.05):
        print(f'Segregations j experiment. j = {j}')
        populations = [
            PopulationConfiguration("red", 4000, j),
            PopulationConfiguration("blue", 4000, j)
        ]

        model = BaselineSchelingModel(populations=populations)
        model.run_model()
        js.append(j)
        segs.append(calculate_segregation(model))

    pd.DataFrame({
        'j': js,
        'segregations': segs
    }).to_csv('outputs/experiment_segregations_j.csv', index=False)


def run_experiment_segregation_radius():
    rs = []
    segs = []

    for r in range(1, 6):
        print(f'Segregations r experiment. r = {r}')
        populations = [
            PopulationConfiguration("red", 4000, 0.5),
            PopulationConfiguration("blue", 4000, 0.5)
        ]

        model = BaselineSchelingModel(populations=populations, neighborhood_radius=r)
        model.run_model()
        rs.append(r)
        segs.append(calculate_segregation(model))

    pd.DataFrame({
        'j': rs,
        'segregations': segs
    }).to_csv('outputs/experiment_segregations_r.csv', index=False)


if __name__ == '__main__':
    run_experiment_iterations()
    run_experiment_segregation_j()
    run_experiment_segregation_radius()
