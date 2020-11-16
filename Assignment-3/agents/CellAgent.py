from mesa import Agent


class CellAgent(Agent):
    STATE_DEAD = 'Dead'
    STATE_ALIVE = 'Alive'

    def __init__(self, pos, model, state):
        super().__init__(pos, model)
        self.pos = pos
        self.state = state
        self.state_future = None

    def is_dead(self):
        return self.state == CellAgent.STATE_DEAD

    def is_alive(self):
        return self.state == CellAgent.STATE_ALIVE

    def set_dead(self):
        self.state_future = CellAgent.STATE_DEAD

    def set_alive(self):
        self.state_future = CellAgent.STATE_ALIVE

    def step(self):
        number_of_alive_neighbor = self.__get_number_of_alive_neighbors()
        if self.is_alive():
            if number_of_alive_neighbor < min(self.model.alive_condition):  # Underpopulation
                self.set_dead()
            elif number_of_alive_neighbor > max(self.model.alive_condition):  # Overpopulation
                self.set_dead()
        elif self.is_dead():
            if number_of_alive_neighbor in self.model.dead_condition:  # Reproduction
                self.set_alive()

    def __get_number_of_alive_neighbors(self):
        return sum([1 for neighbor in self.model.grid.neighbor_iter(self.pos) if neighbor.is_alive()])

    def advance(self) -> None:
        if self.state_future:
            self.state = self.state_future
            self.state_future = None
