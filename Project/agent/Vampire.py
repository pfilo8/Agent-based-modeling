import random
import numpy as np

from mesa import Agent

# [STRATEGY_CHEATERS, STRATEGY_FAIR, STRATEGY_GENEROUS, STRATEGY_MARTYRS, STRATEGY_PRUDENT]
SMART_VAMPIRE_STRATEGIES_PROB = [0.25, 0.25, 0.125, 0.25, 0.125]


class Vampire(Agent):
    def __init__(self, id, model, root_id):
        super().__init__(id, model)
        self.root_id = root_id
        self.survival_time = 60

    def step(self):
        self.hunt()
        if self.model.food_sharing:
            if self.survival_time <= 12:
                other = random.choice(self.get_family())
                self.share_food(other)
        self.survival_time -= 12

    def get_family(self):
        return [agent for agent in self.model.schedule.agents if agent.root_id == self.root_id]

    def hunt(self):
        if random.random() < self.model.hunt_probability:
            self.survival_time = 60
        else:
            self.survival_time -= 12

    def is_dead(self):
        return self.survival_time <= 0

    def share_food(self, other):
        raise NotImplementedError


class SimpleVampire(Vampire):
    def share_food(self, other):
        if other.survival_time >= 48:
            other.survival_time -= 6
            self.survival_time += 6


class SmartVampire(Vampire):
    STRATEGY_CHEATERS = 'C'
    STRATEGY_FAIR = 'F'
    STRATEGY_MARTYRS = 'M'
    STRATEGY_GENEROUS = 'G'
    STRATEGY_PRUDENT = 'P'
    STRATEGIES = [STRATEGY_CHEATERS, STRATEGY_FAIR, STRATEGY_GENEROUS, STRATEGY_MARTYRS, STRATEGY_PRUDENT]

    def __init__(self, id, model, root_id):
        super().__init__(id, model, root_id)
        self.motivation = np.random.choice(self.STRATEGIES, p=self.model.smart_vampire_strategies_prob)

    def share_food(self, other):
        if other.motivation == other.STRATEGY_CHEATERS:
            pass
        elif other.motivation == other.STRATEGY_MARTYRS:
            other.survival_time -= 12
            self.survival_time += 12
        elif other.motivation == other.STRATEGY_FAIR:
            if other.survival_time >= 48:
                other.survival_time -= 12
                self.survival_time += 12
            elif other.survival_time >= 24:
                other.survival_time -= 6
                self.survival_time += 6
        elif other.motivation == other.STRATEGY_GENEROUS:
            if other.survival_time >= 48:
                other.survival_time -= 24
                self.survival_time += 24
            elif other.survival_time >= 24:
                other.survival_time -= 12
                self.survival_time += 12
        elif other.motivation == other.STRATEGY_PRUDENT:
            if other.survival_time >= 48:
                other.survival_time -= 6
                self.survival_time += 6


class SmartDynamicVampire(Vampire):
    def __init__(self, id, model, root_id):
        super().__init__(id, model, root_id)
        self.motivation = np.random.randint(-3, 4)

    def share_food(self, other):
        if other.motivation < -2:  # Cheater
            self.motivation -= 1
        elif -2 <= other.motivation < 0:  # Prudent
            if other.survival_time >= 48:
                other.survival_time -= 6
                self.survival_time += 6
                self.motivation += 1
            self.motivation -= 1
        elif 0 <= other.motivation <= 1:  # Fair
            if other.survival_time >= 48:
                other.survival_time -= 12
                self.survival_time += 12
                self.motivation += 1
            elif other.survival_time >= 24:
                other.survival_time -= 6
                self.survival_time += 6
                self.motivation += 1
            self.motivation -= 1
        elif 1 < other.motivation <= 4:  # Generous
            if other.survival_time >= 48:
                other.survival_time -= 24
                self.survival_time += 24
                self.motivation += 1
            elif other.survival_time >= 24:
                other.survival_time -= 12
                self.survival_time += 12
                self.motivation += 1
            other.motivation -= 1
        elif other.motivation > 4:  # Martyr
            other.survival_time -= 12
            self.survival_time += 12
            self.motivation += 1
