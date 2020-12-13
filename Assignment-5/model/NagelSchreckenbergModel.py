from mesa import Model
from mesa.space import SingleGrid
from mesa.time import BaseScheduler

from random import random

from agent.Car import Car

class CarModel(Model):

    def __init__(self, height, width, dawdle_prob, car_amount):
        super().__init__()
        self.height = height
        self.width = width
        self.dawdle_prob = dawdle_prob
        self.car_amount = car_amount

        self.schedule = BaseScheduler(self)
        self.grid = SingleGrid(height, width, torus=True)

        self.place_agents()

        self.running = True

    def place_agents(self):
        for i in range(self.car_amount):
            while True:
                try:
                    r = random()
                    agent = Car((int(r*100), 5), self, 10)
                    self.grid.position_agent(agent, int(r*100), 5)
                    self.schedule.add(agent)
                    break
                except Exception:
                    continue

    def step(self):
        self.schedule.step()