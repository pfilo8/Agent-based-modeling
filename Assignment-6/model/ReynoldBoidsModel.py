import numpy as np

from mesa import Model
from mesa.space import ContinuousSpace
from mesa.time import SimultaneousActivation

from agent.Boid import Boid

class ReynoldBoidsModel(Model):
    def __init__(self, height: int, width: int, speed: float, vision: int, population: int = 100,
    separation_strength: float = 0.9, cohesion_strength: float = 0.9, alignment_strength: float = 0.9, max_steps: int = 1000,
    min_separation_distance: float = 2):
        super().__init__()
        self.speed = speed
        self.vision = vision
        self.separation_strength = separation_strength
        self.cohesion_strength = cohesion_strength
        self.alignment_strength = alignment_strength
        self.min_separation_distance = min_separation_distance

        self.schedule = SimultaneousActivation(self)
        self.grid = ContinuousSpace(height, width, torus=True)
        self.place_agents(population)

        self.iteration = 0
        self.max_steps = max_steps
        
    def place_agents(self, population):
        for _ in range(population):
            x = self.random.random() * self.grid.x_max
            y = self.random.random() * self.grid.y_max
            pos = (x, y)
            agent = Boid(pos, self)
            self.grid.place_agent(agent, pos)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()
        self.running = self.is_running()
        self.iteration += 1

    def is_running(self):
        return self.iteration < self.max_steps


