from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model.NagelSchreckenbergModel import NagelSchreckenbergModel


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": "black",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5
    }
    return portrayal


grid = CanvasGrid(agent_portrayal, 1, 100, 50, 500)
server = ModularServer(
    NagelSchreckenbergModel,
    [grid],
    "Nagel Schreckenberg Model",
    {
        "line_length": 100,
        "randomization_prob": 0.5,
        "car_density": 0.4,
        "max_speed": 7
    }
)
server.launch(port=8220)
