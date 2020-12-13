from collections import Counter

from mesa.space import Grid

from agents.CellAgent import CellAgent


class GridParser:

    def __init__(self, grid_filename, model=None, torus=True, alive_char=None, dead_char=None):
        self.parsed_grid = self.__parse_text(grid_filename)
        self.torus = torus
        self.model = model
        self.alive_char = alive_char
        self.dead_char = dead_char

    def get_shape(self):
        width, height = self.__get_shape(self.parsed_grid)
        return width, height

    def get_grid(self):
        width, height = self.get_shape()
        grid = Grid(width, height, self.torus)
        alive_char, dead_char = self.__get_alive_dead_char(self.parsed_grid, self.alive_char, self.dead_char)
        grid = self.__populate_grid(self.parsed_grid, grid, self.model, alive_char, dead_char)
        return grid

    @staticmethod
    def __parse_text(grid_filename):
        with open(grid_filename, 'r') as f:
            return f.read().split('\n')

    @staticmethod
    def __get_shape(parsed_grid):
        height = len(parsed_grid)
        width = len(parsed_grid[0])

        for line in parsed_grid:
            if len(line) != width:
                raise ValueError('Not equal length of rows.')
        return width, height

    @staticmethod
    def __get_alive_dead_char(parsed_grid, alive_char, dead_char):
        if alive_char is not None and dead_char is not None:
            return alive_char, dead_char
        return GridParser.__find_alive_dead(parsed_grid)

    @staticmethod
    def __find_alive_dead(parsed_grid):
        counter = Counter(''.join(parsed_grid))
        if len(counter) > 2:
            raise ValueError(f'More than two values in grid file.')
        dead_char = counter.most_common(2)[0][0]  # First record, char
        alive_char = counter.most_common(2)[1][0]  # Second record, char
        return alive_char, dead_char

    @staticmethod
    def __populate_grid(parsed_grid, grid, model, alive_char, dead_char):
        for x, row in enumerate(reversed(parsed_grid)):
            for y, el in enumerate(row):
                if el == alive_char:
                    agent = CellAgent((x, y), model, CellAgent.STATE_ALIVE)
                elif el == dead_char:
                    agent = CellAgent((x, y), model, CellAgent.STATE_DEAD)
                else:
                    raise ValueError('Parsing error.')
                grid.place_agent(agent, (y, x))
        return grid
