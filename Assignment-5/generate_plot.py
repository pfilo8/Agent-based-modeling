import pandas as pd
import plotly.express as px

df = pd.read_csv('outputs/simulation_results.csv')

results = df.groupby(['randomization_prob', 'car_density'])['average_speed'].mean().reset_index()

fig = px.line(
    data_frame=results,
    x='car_density',
    y='average_speed',
    color='randomization_prob',
    labels={
        'car_density': "Car density",
        'average_speed': "Average speed",
        'randomization_prob': "Randomization probability"
    }
)

fig.write_html('results/average-speed-plot.html')
