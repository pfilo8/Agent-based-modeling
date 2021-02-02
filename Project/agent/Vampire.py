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
        self.perform_hunt()
        shared_food = self.perform_food_sharing()
        self.perform_reproduction(shared_food)
        self.survival_time -= 12

    def get_root(self, root):
        return [agent for agent in self.model.schedule.agents if agent.root_id == root]

    def perform_hunt(self):
        if random.random() < self.model.hunt_probability:
            self.survival_time = 60
        else:
            self.survival_time -= 12

    def perform_food_sharing(self):
        if self.model.food_sharing:
            if self.survival_time <= 24:
                group = range(self.model.n_roots)
                prob = np.ones(self.model.n_roots)
                prob[self.root_id] = prob[self.root_id] * (self.model.n_roots - 1) * 9
                prob = prob/np.sum(prob)
                group_id = np.random.choice(group, p=prob)
                group_member = self.get_root(group_id)
                if len(group_member)>0:
                    other = random.choice(group_member)
                    return self.share_food(other)
        return False

    def perform_reproduction(self, shared_food):
        if self.model.reproduction and shared_food:
            if random.random() < self.model.reproduction_probability:
                id = max([agent.unique_id[1] for agent in self.get_root(self.root_id)]) + 1
                baby_vampire = self.model.vampire_type((self.root_id, id), self.model, random.choice(range(self.model.n_roots)))
                self.model.schedule.add(baby_vampire)

    def is_dead(self):
        return self.survival_time <= 0

    def share_food(self, other):
        raise NotImplementedError


class SimpleVampire(Vampire):
    def share_food(self, other):
        if other.survival_time >= 48:
            other.survival_time -= 6
            self.survival_time += 6
            return True
        return False


class SmartVampire(Vampire):
    STRATEGY_CHEATERS = 'Cheater'
    STRATEGY_FAIR = 'Fair'
    STRATEGY_MARTYRS = 'Martyrs'
    STRATEGY_GENEROUS = 'Generous'
    STRATEGY_PRUDENT = 'Prudent'
    STRATEGIES = [STRATEGY_CHEATERS, STRATEGY_FAIR, STRATEGY_GENEROUS, STRATEGY_MARTYRS, STRATEGY_PRUDENT]

    def __init__(self, id, model, root_id):
        super().__init__(id, model, root_id)
        self.motivation = np.random.choice(self.STRATEGIES, p=self.model.smart_vampire_strategies_prob)

    def share_food(self, other):
        if other.motivation == other.STRATEGY_CHEATERS:
            return False
        elif other.motivation == other.STRATEGY_MARTYRS:
            other.survival_time -= 12
            self.survival_time += 12
            return True
        elif other.motivation == other.STRATEGY_FAIR:
            if other.survival_time >= 48:
                other.survival_time -= 12
                self.survival_time += 12
                return True
            elif other.survival_time >= 24:
                other.survival_time -= 6
                self.survival_time += 6
                return True
        elif other.motivation == other.STRATEGY_GENEROUS:
            if other.survival_time >= 48:
                other.survival_time -= 24
                self.survival_time += 24
                return True
            elif other.survival_time >= 24:
                other.survival_time -= 12
                self.survival_time += 12
                return True
        elif other.motivation == other.STRATEGY_PRUDENT:
            if other.survival_time >= 48:
                other.survival_time -= 6
                self.survival_time += 6
                return True
        return False


class SmartDynamicVampire(Vampire):
    def __init__(self, id, model, root_id, motivation=None):
        super().__init__(id, model, root_id)
        self.motivation = np.random.randint(-4, 7) if not motivation else motivation

    def step(self):
        self.perform_hunt()
        shared_food = self.perform_food_sharing()
        self.motivation = max(min(self.motivation, self.model.max_motivation), self.model.min_motivation)
        self.perform_reproduction(shared_food)
        self.survival_time -= 12

    def share_food(self, other):
        if other.motivation < -2:  # Cheater
            self.motivation -= 2
            return False
        elif -2 <= other.motivation < 0:  # Prudent
            if other.survival_time >= 48:
                other.survival_time -= 6
                self.survival_time += 6
                self.motivation += 1
                return True
        elif 0 <= other.motivation <= 1:  # Fair
            if other.survival_time >= 48:
                other.survival_time -= 12
                self.survival_time += 12
                self.motivation += 1
                return True
            elif other.survival_time >= 24:
                other.survival_time -= 6
                self.survival_time += 6
                self.motivation += 1
                return True
        elif 1 < other.motivation <= 4:  # Generous
            if other.survival_time >= 48:
                other.survival_time -= 24
                self.survival_time += 24
                self.motivation += 1
                return True
            elif other.survival_time >= 24:
                other.survival_time -= 12
                self.survival_time += 12
                self.motivation += 1
                return True
        elif other.motivation > 4:  # Martyr
            other.survival_time -= 12
            self.survival_time += 12
            self.motivation += 1
            return True
        self.motivation -= 1
        return False

    def perform_reproduction(self, shared_food):
        if self.model.reproduction and shared_food:
            if random.random() < self.model.reproduction_probability:
                id = max([agent.unique_id[1] for agent in self.get_root(self.root_id)]) + 1
                baby_vampire = self.model.vampire_type((self.root_id, id), self.model, random.choice(range(self.model.n_roots)), -2)
                self.model.schedule.add(baby_vampire)
