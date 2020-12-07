from config.PopulationConfiguration import PopulationConfiguration
from model.SchellingModel import SchellingModel

height, width = 100, 100

populations = [
    PopulationConfiguration("red", 4000, 0.5),
    PopulationConfiguration("blue", 4000, 0.5)
]

model = SchellingModel(height, width, populations)
model.step()
