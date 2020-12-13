from mesa import Agent
from random import random

class Car(Agent):

    def __init__(self, pos, model, max_speed):
        super().__init__(pos, model)
        self.model = model
        self.pos = pos
        self.max_speed = max_speed
        self.speed = 1

    def step(self):
        if self.speed < self.max_speed:
            self.speed += 1

        tmpX = self.pos[0] + 1
        while True:
            if not self.model.grid.is_cell_empty(self.model.grid.torus_adj((tmpX, self.pos[1]))):
                break
            tmpX += 1
        if tmpX - self.pos[0] < self.speed:
            self.speed = tmpX - self.pos[0]

        if random() < self.model.dawdle_prob:
            self.speed -= 1
        self.move()

    def move(self):
        if self.model.grid.is_cell_empty(self.model.grid.torus_adj((self.pos[0]+self.speed, self.pos[1]))):
            self.model.grid.move_agent(self, self.model.grid.torus_adj((self.pos[0]+self.speed, self.pos[1])))