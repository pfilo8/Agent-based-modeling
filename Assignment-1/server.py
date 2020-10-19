from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from agents.TreeAgent import TreeAgent
from models.ForestModel import ForestModel

COLORS = {
    TreeAgent.STATE_GOOD: "green",
    TreeAgent.STATE_FIRE: "red",
    TreeAgent.STATE_BURNT: "black"
}


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": COLORS[agent.state],
        "Filled": "true",
        "Layer": 0,
        "r": 0.5
    }
    return portrayal


grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)
server = ModularServer(
    ForestModel,
    [grid],
    "Forest Model",
    {
        "grid_shape": (20, 20),
        "p": 0.5
    }
)
server.launch()
