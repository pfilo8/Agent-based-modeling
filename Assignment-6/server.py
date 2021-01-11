from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from canvas.SimpleContinuousModule import SimpleCanvas

from model.ReynoldBoidsModel import ReynoldBoidsModel


def boid_draw(agent):
    return {"Shape": "circle", "r": 2, "Filled": "true", "Color": "Red"}


boid_canvas = SimpleCanvas(boid_draw, 500, 500)
model_params = {
    "height": 100, 
        "width": 50, 
        "speed": 3, 
        "vision": 10, 
        "separation_strength": 0.02,
        "cohesion_strength": 0.02, 
        "alignment_strength": 0.4
}

server = ModularServer(ReynoldBoidsModel, [boid_canvas], "Boids", model_params)
server.launch()
