import random

from mesa import Agent


class Car(Agent):

    def __init__(self, pos, model, max_speed):
        super().__init__(pos, model)
        self.model = model
        self.pos = pos
        self.max_speed = max_speed
        self.speed = 1

    def step(self):
        self._accelerate()
        self._slow_down()
        self._randomization()

    def _accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 1

    def _slow_down(self):
        for i in range(1, self.speed + 1):
            theoretical_neighbour_pos = (self.model.LINE_POS, self.pos[1] + i)
            real_neighbour_pos = self.model.grid.torus_adj(theoretical_neighbour_pos)
            if not self.model.grid.is_cell_empty(real_neighbour_pos):
                # The next position is not empty
                self.speed = i - 1

    def _randomization(self):
        if self.speed >= 1:
            if random.random() < self.model.randomization_prob:
                self.speed -= 1

    def advance(self) -> None:
        new_pos = (self.model.LINE_POS, self.pos[1] + self.speed)
        self.model.grid.move_agent(self, new_pos)
