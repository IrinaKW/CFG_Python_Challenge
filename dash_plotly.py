from dash import Dash, html
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data/updated_sales_dataset.csv')

# Initialize the app
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='GFC-Challenge Visual Representation'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10,
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
])


if __name__ == '__main__':
    app.run_server(debug=True)
