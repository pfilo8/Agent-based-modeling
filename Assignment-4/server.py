from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from config.PopulationConfiguration import PopulationConfiguration
from model.SchellingModel import SchellingModel


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": agent.color,
        "Filled": "true",
        "Layer": 0,
        "r": 0.5
    }
    return portrayal


height, width = 100, 100
populations = [
    PopulationConfiguration("red", 2000, 0.5),
    PopulationConfiguration("blue", 2000, 0.5),
    PopulationConfiguration("green", 2000, 0.5)
]
neighborhood_radius = 2

grid = CanvasGrid(agent_portrayal, height, width, 500, 500)
server = ModularServer(
    SchellingModel,
    [grid],
    "Schelling Model",
    {
        "height": height,
        "width": width,
        "populations": populations,
        "neighborhood_radius": neighborhood_radius
    }
)
server.launch()
