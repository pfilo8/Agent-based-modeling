# Agent-based Bass Model

In this assignment list we've prepared situation agent-base version of Bass Diffusion Model. 

## Approach

* Initialize n agents with null state. Define f(0) = 0.
* In each step t:
    * Check if agent has null state. 
    * If yes check if agent is innovator or if agent is imitator.
    * Update f(t).

In the each step probability of agent being innovator was equal:

p * (1 - f(t))

and probability of being imitator:

q * f(t) * (1 - f(t))

Which is equivalent to differential definiton of the model.

## Results

Analysis of the model was performed in `simulation.ipynb` notebook.
Resulting plots can be found in the `results` directory. Based on our generated plots 
and especially its shapes we can conclude that our model is a good approximation of the original one.
