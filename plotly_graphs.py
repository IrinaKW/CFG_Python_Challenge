#%%

import plotly.express as px
import pandas as pd
import numpy as np

df=pd.read_csv('data/updated_sales_dataset.csv')
df

df_month= df[['Month','TotalSaleMonth','MonSpentCustMin', 'MonSpentCustMax', 'MonNumCustMin','MonNumCustMax']]
df_month=df_month.drop_duplicates()


dff=df_month[['Month','TotalSaleMonth']].sort_values('TotalSaleMonth')

dff

px.bar(dff, x='Month', y='TotalSaleMonth')



#%%
# Interactive representation of the highest spender by month
df_max_customer = data_file.loc[data_file.reset_index().groupby(['Month'])['TotalSpentCustomer'].idxmax()]
fig=px.sunburst(df_max_customer, 
            path=['Month','CustomerName','TotalSpentCustomer'])
fig.update_traces(hovertemplate='<b>Total: %{df_max_customer["TotalPurchasesCustomer"]} </b>')  # parent, or label, or id, or value
fig.show()


