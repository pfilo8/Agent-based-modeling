from mesa import Agent


class TreeAgent(Agent):
    STATE_GOOD = 'Good'
    STATE_FIRE = 'Fire'
    STATE_BURNT = 'Burnt'

    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.pos = pos
        self.state = self.STATE_GOOD
        self.state_future = None

    def is_good(self):
        return self.state == self.STATE_GOOD

    def is_on_fire(self):
        return self.state == self.STATE_FIRE

    def set_fire(self):
        self.state_future = self.STATE_FIRE

    def set_burnt(self):
        self.state_future = self.STATE_BURNT

    def step(self):
        if self.is_on_fire():
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.is_good():
                    neighbor.set_fire()
            self.set_burnt()

    def advance(self):
        if self.state_future:
            self.state = self.state_future
            self.state_future = None
