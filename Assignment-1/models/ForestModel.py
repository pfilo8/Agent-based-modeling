from mesa import Model
from mesa.space import Grid
from mesa.time import SimultaneousActivation

from agents.TreeAgent import TreeAgent


class ForestModel(Model):

    def __init__(self, grid_shape, p):
        self.grid = Grid(grid_shape[0], grid_shape[1], torus=False)
        self.schedule = SimultaneousActivation(self)
        self.running = True

        for a, x, y in self.grid.coord_iter():

            if self.random.random() < p:
                agent = TreeAgent((x, y), self)

                if x == 0:
                    agent.set_fire()
                    agent.advance()

                self.schedule.add(agent)
                self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
        self.running = self.is_running()

    def is_running(self):
        return any([agent.state == TreeAgent.STATE_FIRE for agent in self.schedule.agents])
