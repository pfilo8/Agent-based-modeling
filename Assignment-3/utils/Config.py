import json

from .GridParser import GridParser


class Config:

    def __init__(self, filename):
        self.json = self.parse_json(filename)
        self.grid_filename = self.json['grid_filename']
        self.torus = self.json.get('torus', True)
        self.alive_condition = self.json.get('alive_condition', [2, 3])
        self.dead_condition = self.json.get('dead_condition', [3])
        self.alive_char = self.json.get('alive_char', '0')
        self.dead_char = self.json.get('dead_char', '.')

    @staticmethod
    def parse_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def get_grid_shape(self):
        return GridParser(self.grid_filename).get_shape()
