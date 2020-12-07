from typing import List

from mesa import Model
from mesa.space import Grid
from mesa.time import RandomActivation

from agent.Citizen import Citizen
from config.PopulationConfiguration import PopulationConfiguration


class SchellingModel(Model):

    def __init__(self, width: int, height: int, populations: List[PopulationConfiguration],
                 neighborhood_radius: int = 1, lonely_happy: bool = True, max_iter: int = 1000):
        self.grid = Grid(width=width, height=height, torus=True)
        self.schedule = RandomActivation(self)

        self.iteration = 0
        self.running = True
        self.max_iter = max_iter

        for population in populations:
            for _ in range(population.n):
                pos = self.grid.find_empty()
                agent = Citizen(pos=pos, model=self, color=population.color, happiness_threshold=population.j,
                                neighborhood_radius=neighborhood_radius, lonely_happy=lonely_happy)
                self.grid.place_agent(agent, pos)
                self.schedule.add(agent)

    def step(self):
        self.schedule.step()
        self.iteration += 1
        self.running = self.is_running()

    def is_running(self):
        return not self.__is_all_happy() and not self.__is_max_iter_exceeded()

    def __is_all_happy(self):
        return all([agent.is_happy() for agent in self.schedule.agents])

    def __is_max_iter_exceeded(self):
        return self.iteration > self.max_iter
