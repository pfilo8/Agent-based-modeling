from functools import partial

import numpy as np
from mesa.batchrunner import BatchRunner

from model.NagelSchreckenbergModel import NagelSchreckenbergModel

model = partial(NagelSchreckenbergModel, line_length=100, max_speed=5)

params_variables = {
    "randomization_prob": [0.2, 0.5, 0.7],
    "car_density": np.arange(0.1, 1.0, 0.1)
}

batch_runner = BatchRunner(
    model,
    variable_parameters=params_variables,
    iterations=50
)

batch_runner.run_all()
results = batch_runner.get_model_vars_dataframe()
results.to_csv('output/simulation_results.csv', index=False)
