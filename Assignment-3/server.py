import sys

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from models.GameOfLifeModel import GameOfLifeModel
from utils.Config import Config


def agent_portrayal(agent):
    portrayal = {
        "Shape": "rect",
        "h": "0.9",
        "w": "0.9",
        "Color": "black" if agent.is_alive() else "white",
        "Filled": "true",
        "Layer": 0
    }
    return portrayal


config = Config(sys.argv[1])
width, height = config.get_grid_shape()
canvas_grid = CanvasGrid(agent_portrayal, grid_width=width, grid_height=height, canvas_height=height*10, canvas_width=width*10)
server = ModularServer(
    GameOfLifeModel,
    [canvas_grid],
    "Forest Model",
    {
        "grid_filename": config.grid_filename,
        "torus": config.torus,
        "alive_condition": config.alive_condition,
        "dead_condition": config.dead_condition,
        "alive_char": config.alive_char,
        "dead_char": config.dead_char,
        "max_iter": config.max_iter
    }
)
server.launch()
