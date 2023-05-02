from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px



# Incorporate data
df = pd.read_csv('data/updated_sales_dataset.csv')

#create pivot tables
df_month= df[['Month','TotalSaleMonth','MonSpentCustMin', 'MonSpentCustMax', 'MonNumCustMin','MonNumCustMax']]
df_month=df_month.drop_duplicates()

df_cat= df[['Category','AvgPriceCategory','CatSpentCustMin', 'CatSpentCustMax', 'CatNumCustMin','CatNumCustMax']]
df_cat=df_month.drop_duplicates()

#df_total_cat=df.groupby('Category')['TotalPurchasesCustomer','TotalSpentCustomer'].sum()
#df_total_cat.reset_index().sort_values('TotalPurchasesCustomer', ascending=False)

df_max_customer = df.loc[df.reset_index().groupby(['Month'])['TotalSpentCustomer'].idxmax()]

# Initialize the app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div(className='row',  # Define the row element
        children=[
            # Define the left element
            html.Div(className='four columns div-user-controls',
            children = [
                html.H2('CFG Challenge: Product Sale Dashboard'),
                html.P('''Visualising with Plotly - Dash'''),
                html.Hr()
            ]), 
            #Define the middle element
            html.Div(className='eight columns div-for-charts bg-grey',
                children = [
                    html.H4('Interactive representation of the highest spender by month'),
                    dcc.Graph(config={'displayModeBar':False},
                        animate=True,
                        figure=px.sunburst(df_max_customer, path=['Month','CustomerName','TotalSpentCustomer'])
                    )
                ]),
            # Define the right element
            html.Div(className='eight columns div-for-charts bg-grey',
            children = [
                html.Hr(),
                html.H4('Monthly Spending '),
                dcc.Dropdown(options=['TotalSaleMonth','MonSpentCustMin', 'MonSpentCustMax', 'MonNumCustMin','MonNumCustMax'], 
                    value='TotalSaleMonth', id='dropdown-controls'),

                dcc.Graph(id='month graph'
                )
            ])  
    ])
])

# Add controls to build the interaction
@callback(
    Output(component_id='month graph', component_property='figure'),
    [Input(component_id='dropdown-controls', component_property='value')]
)
def month_graph(col_chosen):
    df=df_month[['Month',col_chosen]].sort_values(col_chosen)
    fig = px.bar(df, x='Month', y=col_chosen)
    return fig


# app = Dash(external_stylesheets=[dbc.themes.LUX])

# # App layout
# app.layout = html.Div([
    
#     html.Div(children='CFG Challenge Sales Data Visualisation App', style={'textAlign': 'center'}),
    
#     html.Hr(),
    
#     dcc.Dropdown(options=['MonSpentCustMin', 'MonSpentCustMax', 'MonNumCustMix','MonNumCustMax'], value='MonSpentCustMin', id='dropdown-controls'),

#     dash_table.DataTable(data=df.to_dict('records'), page_size=10),

#     html.Div(children=[
#         dcc.Graph(figure=px.histogram(df_month.sort_values('MonSpentCustMax'), x='Month', y='MonSpentCustMax'), id='graph-max', style={'display': 'inline-block'}),
#         dcc.Graph(figure=px.histogram(df_month.sort_values('MonSpentCustMin'), x='Month', y='MonSpentCustMin'), id='graph-min', style={'display': 'inline-block'})
#     ]),

#     html.Div(children='Total purchase per customer per Category', style={'textAlign': 'center'})
#     #dcc.Graph(figure={}, id='controls-and-graph')
# ])




if __name__ == '__main__':
    app.run_server(debug=True)
