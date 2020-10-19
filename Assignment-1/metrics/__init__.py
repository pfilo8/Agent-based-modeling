import numpy as np

from agents.TreeAgent import TreeAgent

from src.HoshenKopelman import HoshenKopelman


def compute_is_burnt(model):
    return int(any([agent.state == TreeAgent.STATE_BURNT for agent in model.grid.grid[-1] if agent is not None]))


def compute_max_cluster_size(model):
    grid = prepare_grid(model.grid.grid)
    hk = HoshenKopelman(grid)
    label = hk.search()
    labels, counts = np.unique(label, return_counts=True)
    clusters = dict(zip(labels, counts))
    clusters.pop(0, None)  # Delete non-burnt tree cluster
    return max(clusters.values(), default=0)


def prepare_grid(grid):
    grid_translated = []
    for row in grid:

        row_translated = []
        for el in row:
            if isinstance(el, TreeAgent):
                if el.state == TreeAgent.STATE_BURNT:
                    row_translated.append(1)
                else:
                    row_translated.append(0)
            else:
                row_translated.append(0)
        grid_translated.append(row_translated)

    return np.array(grid_translated)
