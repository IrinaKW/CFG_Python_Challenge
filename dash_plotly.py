from dash import Dash, html
import pandas as pd

# Incorporate data
df = pd.read_csv('https://data/updated_.csv')

# Initialize the app
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Visual Representation')
])


if __name__ == '__main__':
    app.run_server(debug=True)
