from mesa import Agent


class Citizen(Agent):

    def __init__(self, pos, model, color, neighborhood_radius=1, happiness_threshold=0.5, lonely_happy=True):
        super().__init__(pos, model)
        self.color = color
        self.neighborhood_radius = neighborhood_radius 
        self.happiness_threshold = happiness_threshold
        self.lonely_happy = lonely_happy

    def is_happy(self):
        neighbours = [el for el in self.model.grid.iter_neighbors(self.pos, moore=True)]
        if len(neighbours) == 0:
            return self.lonely_happy
        else:
            same_color = [el for el in neighbours if el.color == self.color]
            return (len(same_color) / len(neighbours)) > self.happiness_threshold

    def step(self):
        if not self.is_happy():
            new_pos = self.model.grid.find_empty()
            self.model.grid.move_agent(self, new_pos)
