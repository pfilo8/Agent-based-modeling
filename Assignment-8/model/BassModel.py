import numpy as np

from mesa import Model
from mesa.space import Grid
from mesa.time import SimultaneousActivation

from agent.Customer import Customer


class BassModel(Model):
    LINE_HEIGHT = 1
    LINE_POS = 0

    def __init__(self, p: float, q: float, n: int, max_iteration: int = 1000):
        super().__init__()
        self.p = p
        self.q = q

        self.grid = Grid(n, self.LINE_HEIGHT, torus=True)
        self.schedule = SimultaneousActivation(self)
        self.init_agents(n)

        self.f_t = self.calculate_f_t()

        self.iteration = 0
        self.max_iteration = max_iteration

    def init_agents(self, n):
        for i in range(n):
            agent = Customer(i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (i, self.LINE_POS))

    def calculate_f_t(self):
        return np.mean([1 if agent.state else 0 for agent in self.schedule.agents])

    def step(self):
        self.schedule.step()
        self.running = self.is_running()
        self.iteration += 1
        self.f_t = self.calculate_f_t()

    def is_running(self):
        return self.iteration < self.max_iteration
