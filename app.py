import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly.express as px



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

trends_sim = pd.read_csv('/Users/calumwalker/github/CovidDashboard/total_cases_by_la_20201201.csv')
trends_agesex = pd.read_csv('/Users/calumwalker/github/CovidDashboard/trend_agesex_20201201.csv', parse_dates=['Date'], index_col=0)
total_cases = pd.read_csv('/Users/calumwalker/github/CovidDashboard/total_cases_by_la_20201201.csv')



del trends_agesex['Sex']
del trends_agesex['SexQF']
del trends_agesex['AgeGroupQF']
del trends_agesex['CumulativePositive']
del trends_agesex['CrudeRatePositive']
del trends_agesex['DailyDeaths']
del trends_agesex['CumulativeDeaths']
del trends_agesex['CrudeRateDeaths']
del trends_agesex['CumulativeNegative']
del trends_agesex['CrudeRateNegative']
del trends_agesex['Country']
import plotly.graph_objects as go
df_15_to_19 = trends_agesex[trends_agesex['AgeGroup']=='15 to 19']
df_20_to_24 = trends_agesex[trends_agesex['AgeGroup']=='20 to 24']
df_25_to_44 = trends_agesex[trends_agesex['AgeGroup']=='25 to 44']
df_45_to_64 = trends_agesex[trends_agesex['AgeGroup']=='45 to 64']
df_65_to_74 = trends_agesex[trends_agesex['AgeGroup']=='65 to 74']
df_75_to_84 = trends_agesex[trends_agesex['AgeGroup']=='75 to 84']
df_85plus = trends_agesex[trends_agesex['AgeGroup']=='85plus']


df_15_to_19 = df_15_to_19.groupby(['Date']).sum()
df_20_to_24 = df_20_to_24.groupby(['Date']).sum()
df_25_to_44 = df_25_to_44.groupby(['Date']).sum()
df_45_to_64 = df_45_to_64.groupby(['Date']).sum()
df_65_to_74 = df_65_to_74.groupby(['Date']).sum()
df_75_to_84 = df_75_to_84.groupby(['Date']).sum()
df_85plus = df_85plus.groupby(['Date']).sum()

df_15_to_19.columns = ['15 to 19']
df_20_to_24.columns = ['20 to 24']
df_25_to_44.columns = ['25 to 44']
df_45_to_64.columns = ['45 to 64']
df_65_to_74.columns = ['65 to 74']
df_75_to_84.columns = ['75 to 84']
df_85plus.columns = ['85+']

from functools import reduce

data_frames = [df_15_to_19, df_20_to_24, df_25_to_44, df_45_to_64, df_65_to_74, df_75_to_84, df_85plus]


df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'],
                                            how='outer'), data_frames)


fig = px.line(df_merged, x=df_merged.index, y=["15 to 19", "20 to 24", "25 to 44", "45 to 64", "65 to 74", "75 to 84", "85+"])



app.layout = html.Div(children=[
    html.H1(children='Scotland COVID Dashboard'),

    html.Div(children='''
        From the Governments Website
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
