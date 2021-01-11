import numpy as np

from mesa import Agent

class Boid(Agent):
        def __init__(self, pos, model):
            super().__init__(pos, model)
            self.pos = np.array(pos)
            self.model = model
            self.heading = np.random.random(2)
            self.heading /= np.linalg.norm(self.heading)
        
        def cohere(self, neighbors):
            cohere = np.zeros(2)
            for neighbor in neighbors:
                cohere += self.model.grid.get_heading(self.pos, neighbor.pos)
            cohere /= len(neighbors)
            return cohere

        def separate(self, neighbors):
            me = self.pos
            them = (n.pos for n in neighbors)
            separation_vector = np.zeros(2)
            for other in them:
                if self.model.grid.get_distance(me, other) < self.model.min_separation_distance:
                    separation_vector -= self.model.grid.get_heading(me, other)
            return separation_vector

        def alignment(self, neighbors):
            alignment_vec = np.zeros(2)
            for neighbor in neighbors:
                alignment_vec += neighbor.heading
            alignment_vec /= len(neighbors)
            return alignment_vec

        def get_neighbors(self):
            neighbors = self.model.grid.get_neighbors(self.pos, self.model.vision, False)
            return neighbors

        def step(self):
            neighbors = self.get_neighbors()

            if len(neighbors) > 0:
                cohere_vec = self.cohere(neighbors)
                separate_vec = self.separate(neighbors)
                alignment_vec = self.alignment(neighbors)

                self.heading += (cohere_vec * self.model.separation_strength
                + separate_vec * self.model.cohesion_strength
                + alignment_vec * self.model.alignment_strength) 
                self.heading /= np.linalg.norm(self.heading)

        def advance(self):
            new_pos = np.array(self.pos) + self.heading * self.model.speed
            new_x, new_y = new_pos
            self.model.grid.move_agent(self, (new_x, new_y))
