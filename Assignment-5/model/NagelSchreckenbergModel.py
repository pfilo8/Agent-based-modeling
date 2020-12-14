from mesa import Model
from mesa.space import Grid
from mesa.time import SimultaneousActivation

from agent.Car import Car
from metric import calculate_average_speed


class NagelSchreckenbergModel(Model):
    LINE_HEIGHT = 1
    LINE_POS = 0

    def __init__(self, line_length, randomization_prob, car_density, max_speed, max_steps=100):
        super().__init__()
        self.line_length = line_length
        self.randomization_prob = randomization_prob
        self.car_amount = int(line_length * car_density)
        self.max_speed = max_speed

        self.schedule = SimultaneousActivation(self)
        self.grid = Grid(self.LINE_HEIGHT, line_length, torus=True)
        self.place_agents()

        self.max_steps = max_steps
        self.iteration = 0
        self.running = True

        self.custom_data_collector = []

    def place_agents(self):
        for i in range(self.car_amount):
            pos = self.grid.find_empty()
            agent = Car(pos, self, self.max_speed)
            self.grid.place_agent(agent, pos)
            self.schedule.add(agent)

    def step(self):
        self.custom_data_collector.append(calculate_average_speed(self.schedule.agents))
        self.schedule.step()
        self.running = self.is_running()
        self.iteration += 1

    def is_running(self):
        return self.iteration < self.max_steps
