from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from agent.Vampire import SimpleVampire
from utils.statistics import compute_vampires


class VampireModel(Model):
    def __init__(self, n_roots=10, root_size=15, hunt_probability=0.93, food_sharing=False, reproduction=False,
                 reproduction_probability=0.1, vampire_type=SimpleVampire, smart_vampire_strategies_prob=None,
                 min_motivation=-999, max_motivation=999, max_iteration=1000):

        self.hunt_probability = hunt_probability
        self.food_sharing = food_sharing
        self.reproduction = reproduction
        self.reproduction_probability = reproduction_probability
        self.vampire_type = vampire_type
        self.smart_vampire_strategies_prob = smart_vampire_strategies_prob
        self.min_motivation = min_motivation
        self.max_motivation = max_motivation

        self.schedule = RandomActivation(self)
        self.running = True
        self.iteration = 0
        self.max_iteration = max_iteration

        self.init_agents(n_roots, root_size)
        self.datacollector = DataCollector(
            model_reporters={"Bats": compute_vampires},
            agent_reporters={"Motivation": lambda a: a.motivation if hasattr(a, 'motivation') else None}
        )

    def init_agents(self, n_roots, root_size):
        for root_id in range(n_roots):
            for i in range(root_size):
                agent = self.vampire_type((root_id, i), self, root_id)
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
