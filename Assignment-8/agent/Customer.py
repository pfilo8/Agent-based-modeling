import numpy as np
import random

from mesa import Agent


class Customer(Agent):
    STATE_INNOVATOR = 'innovator'
    STATE_IMITATOR = 'imitator'

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = None
        self.iteration = None

    def step(self):
        if self.state is None:
            if self.model.p * (1-self.model.f_t) > random.random():
                self.state = self.STATE_INNOVATOR
                self.iteration = self.model.iteration
            elif self.model.q * (1-self.model.f_t) * self.model.f_t > random.random():
                self.state = self.STATE_IMITATOR
                self.iteration = self.model.iteration
