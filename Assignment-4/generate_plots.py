import pandas as pd
import plotly.express as px


def generate_plot_experiment_radius():
    df = pd.read_csv('outputs/experiment_segregations_r.csv')
    px.bar(
        df,
        x='j',
        y='segregations',
        labels={
            'j': 'Neighbour radius',
            'segregations': 'Segregation coefficient'
        }
    ).write_html('results/experiment-radius.html')


def generate_plot_experiment_j():
    df = pd.read_csv('outputs/experiment_segregations_j.csv')
    px.bar(
        df,
        x='j',
        y='segregations',
        labels={
            'j': 'Neighbour radius',
            'segregations': 'Segregation coefficient'
        }
    ).write_html('results/experiment-j.html')


def generate_plot_experiment_iterations():
    df = pd.read_csv('outputs/experiment_iterations.csv')
    px.bar(
        df,
        x='n',
        y='iterations',
        labels={
            'n': 'Number of citizens',
            'iterations': 'Iterations to converge'
        }
    ).write_html('results/experiment-iterations.html')


if __name__ == '__main__':
    generate_plot_experiment_iterations()
    generate_plot_experiment_j()
    generate_plot_experiment_radius()
