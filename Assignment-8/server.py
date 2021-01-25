from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from agent.Customer import Customer
from model.BassModel import BassModel


def agent_portrayal(agent):
    color_mapping = {
        None: "black",
        Customer.STATE_IMITATOR: "red",
        Customer.STATE_INNOVATOR: "green"
    }
    portrayal = {
        "Shape": "circle",
        "Color": color_mapping[agent.state],
        "Filled": "true",
        "Layer": 0,
        "r": 1
    }
    return portrayal


grid = CanvasGrid(agent_portrayal, 50, 1, 500, 50)
server = ModularServer(
    BassModel,
    [grid],
    "Bass Model",
    {
        "p": 0.01,
        "q": 0.3,
        "n": 50
    }
)
server.launch(port=8220)
