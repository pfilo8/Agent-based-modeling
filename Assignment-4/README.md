# Schelling Model

In this lab assignment we've implemented Schelling Model.

### Baseline model

The baseline model have following parameters:
* Square lattice grid with L = 100
* Number of Citizens is equal N = 8000, where we have 2 classes (red and blue) and Nb = Nr
* Happiness threshold is equal to jr = jb = 0.5
* Number of neighbours for all agents is equal mr = mb = 8 (radius of neighbours equal to 1)
* Periodic boundary condition
* Stop conditions: nobody wants to move, max limit of iterations equal to 1000
* Lonely agents are happy

### Results

We've prepared following results:
* GIF of baseline model
* GIF of baseline model with jr = 0.75 and jb = 0.375
* GIF of baseline model with mr = mb = 80 (radius = 3)
* GIF of model with 3 classes of neighbours - 2000 per each class, rest as baseline model (additional)
* Plot N vs. number of iterations till end of the simulation (250, 4000, 50)
* Plot segregation vs. jr = jb (0.1, 0.9, 0.05)
* Plot segregation vs. nb of layers (k = 1, 2, 3, 4, 5)

They can be found in `results` directory.

### Implementation details
Our implementations was thought to be as generic as possible. 
We would like to mentions a few options which are possible but wasn't simulated due to limited computational resources.

* It's possible to add as many citizens classes as user wishes
* Each citizen class may have different happiness threshold 
* In each model instance user can define any rectangular grid size, neighbour radius, flag if lonely agent is happy and max iterations
