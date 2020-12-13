from typing import List

from mesa import Model
from mesa.time import SimultaneousActivation

from utils.GridParser import GridParser


class GameOfLifeModel(Model):

    def __init__(self, grid_filename: str, torus: bool, alive_condition: List, dead_condition: List, alive_char: str,
                 dead_char: str, max_iter: int = 150):
        self.grid = self.get_grid(grid_filename, torus, alive_char, dead_char)
        self.schedule = self.get_schedule()
        self.running = True
        self.alive_condition = alive_condition
        self.dead_condition = dead_condition
        self.max_iter = max_iter
        self.iteration = 1

    def step(self):
        self.schedule.step()
        self.iteration += 1
        self.running = self.is_running()

    def is_running(self):
        first_condition = not all([agent.is_dead() for agent in self.schedule.agents])  # All dead cells
        second_condition = self.iteration < self.max_iter
        return first_condition and second_condition

    def get_grid(self, grid_filename, torus, alive_char, dead_char):
        return GridParser(grid_filename, self, torus, alive_char, dead_char).get_grid()

    def get_schedule(self):
        schedule = SimultaneousActivation(self)
        for a, x, y in self.grid.coord_iter():
            schedule.add(a)
        return schedule
