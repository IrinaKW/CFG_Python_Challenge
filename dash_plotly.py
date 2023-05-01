from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data/updated_sales_dataset.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Hr(),
    dcc.Dropdown(options=['TotalSale', 'lifeExp', 'gdpPercap'], value='lifeExp', id='dropdown-controls'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='dropdown-controls', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='Month', y=col_chosen, histfunc='avg')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
