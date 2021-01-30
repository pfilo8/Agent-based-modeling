import numpy as np

from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from agent.Vampire import SimpleVampire
from utils.statistics import compute_vampires

class VampireModel(Model):
    def __init__(self, n_roots = 10, root_size = 15, hunt_probability = 0.93, food_sharing = False, 
                vampire_type = SimpleVampire, max_iteration = 1000):

        self.hunt_probability = hunt_probability
        self.food_sharing = food_sharing
        self.schedule = RandomActivation(self)

        self.running = True
        self.iteration = 0
        self.max_iteration = max_iteration

        self.init_agents(n_roots, root_size, vampire_type)

        self.datacollector = DataCollector(model_reporters={"Bats": compute_vampires})


    def init_agents(self, n_roots, root_size, vampire_type):
        for root_id in range(n_roots):
            for i in range(root_size):
                agent = vampire_type((root_id, i), self, root_id)
                self.schedule.add(agent)

    def remove_dead_agents(self):
        [self.schedule.remove(agent) for agent in self.schedule.agents if agent.is_dead()] 


    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.remove_dead_agents()

        self.running = self.is_running()
        self.iteration += 1
        
    def is_running(self):
        return (self.iteration < self.max_iteration) and (compute_vampires(self) > 0)

                


