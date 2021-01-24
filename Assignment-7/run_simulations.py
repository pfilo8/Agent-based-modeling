import logging
import multiprocessing as mp
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import networkx as nx

from simulations.qvoter_on_graph import qvoter_model_on_graph

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

PATH_BASEDIR = Path('results')

P = np.arange(0, 1.05, 0.05)
Q = [4] 
F = [0.2, 0.3, 0.4, 0.5]
N_STEPS = 100
GRAPHS = {
    "complete": {
        "generator": nx.complete_graph,
        "args": {
            "n": 100
        }
    }
}


def calculate(p, q, f, graph):
    logging.info(f"Current graph: {graph}, current p: {p}")

    current_path = Path(PATH_BASEDIR).joinpath(f"{graph}").joinpath(f"q-{q}").joinpath(f"p-{p}").joinpath(f"f-{f}")
    current_path.mkdir(parents=True, exist_ok=True)

    for i in range(N_STEPS):
        generator = GRAPHS[graph]['generator']
        args = GRAPHS[graph]['args']

        g = generator(**args)
        results = qvoter_model_on_graph(g, p, q, f)
        results = pd.DataFrame(results)
        results_path = current_path.joinpath(f'{i}.csv')
        results.to_csv(results_path, index=False)


PATH_BASEDIR.mkdir(parents=True, exist_ok=True)

pool = mp.Pool(processes=8)

for p, q, f, graph in product(P, Q, F, GRAPHS):
    pool.apply_async(calculate, args=(p, q, f, graph))

pool.close()
pool.join()
