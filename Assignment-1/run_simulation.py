from datetime import datetime

import numpy as np
from mesa.batchrunner import BatchRunner

from models.ForestModel import ForestModel
from metrics import compute_is_burnt, compute_max_cluster_size

params_variable = {
    "p": np.arange(0, 1.02, 0.02),
    "grid_shape": [(20, 20), (50, 50), (100, 100)]
}

batch_runner = BatchRunner(
    ForestModel,
    variable_parameters=params_variable,
    iterations=50,
    model_reporters={
        "Burnt": compute_is_burnt,
        "Max cluster size": compute_max_cluster_size
    }
)

batch_runner.run_all()
results = batch_runner.get_model_vars_dataframe()
results.to_csv('output/simulation_results.csv', index=False)
