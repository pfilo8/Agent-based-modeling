import numpy as np


class HoshenKopelman:

    def __init__(self, grid):
        self.grid = grid
        self.label = np.zeros(shape=self.grid.shape)

    def search(self):
        largest_label = 0

        for x in range(self.grid.shape[0]):
            for y in range(self.grid.shape[1]):
                if self.grid[x, y] == 1:
                    left = self.__get_left(x, y)
                    above = self.__get_right(x, y)

                    if left == 0 and above == 0:
                        largest_label += 1
                        self.label[x, y] = largest_label
                    elif left != 0 and above == 0:
                        self.label[x, y] = self.label[x - 1, y]
                    elif left == 0 and above != 0:
                        self.label[x, y] = self.label[x, y - 1]
                    else:
                        self.__union(x, y)
                        self.label[x, y] = self.label[x, y - 1]
        return self.label

    def __get_left(self, x, y):
        return self.grid[x - 1, y] if x - 1 >= 0 else 0

    def __get_right(self, x, y):
        return self.grid[x, y - 1] if y - 1 >= 0 else 0

    def __union(self, x, y):
        above = self.label[x, y - 1]
        left = self.label[x - 1, y]
        self.label = np.where(self.label == above, left, self.label)
