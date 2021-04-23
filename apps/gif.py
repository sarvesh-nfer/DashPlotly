import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta
#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________code for Dash_______________________________________________________________________________________________________



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#44bd32'
}


#tab style
tabs_styles = {
    'height': '70px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '25px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '10px'
}
##tab style ends here


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

parse=pd.read_csv('apps/parse_bb.csv')
parse[['scanner_name','slide_id','1','2']]=parse["slide_name"].str.split("_",expand=True)
parse=parse.drop(['1','2'],axis=1)
m1=parse[parse['scanner_name']=='H01CBA02P']
m2=parse[parse['scanner_name']=='H01CBA03P']
m3=parse[parse['scanner_name']=='H01CBA01P']
m4=parse[parse['scanner_name']=='H01CBA05P']

category1 = []
for opt in m1['date'].unique():
    category1.append({'label' : opt, 'value' : opt})

category2 = []
for opt in m2['date'].unique():
    category2.append({'label' : opt, 'value' : opt})

category3 = []
for opt in m3['date'].unique():
    category3.append({'label' : opt, 'value' : opt})

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Scanner Health',style=tab_style, selected_style=tab_selected_style, children=[
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            #html.Img(src=app.get_asset_url('/spec2.png'),style={'maxWidth': '100%','maxHeight': '100%','marginLeft': 'auto','marginRight': 'auto'}),
            html.Br(),
            html.Br(),
            html.H1(children='Acquisition',style={
            'textAlign': 'center',
            'color': colors['text']}),
            html.H1(children='\t\t- Last updated for :'+str(date.today()- timedelta(days = 1)),style={
            'textAlign': 'center',
            'color': colors['text']})

        ]),
        dcc.Tab(label='Station 1',style=tab_style, selected_style=tab_selected_style, children=[
        html.Br(),
            html.H1(children='Table for grids'),
            html.Div([
                html.Label("Choose date"),
                dcc.Dropdown(id = 't1', options = category1, value = np.sort(m1['date'].unique())[-1]),
                dcc.Graph(id='grapht1'),
                ],
                 style = {'width': '50%', 'display': 'inline-block'}),
        ]),
        dcc.Tab(label='Station 2',style=tab_style, selected_style=tab_selected_style, children=[
        html.Br(),
            html.H1(children='Table for grids'),
            html.Div([
                html.Label("Choose date"),
                dcc.Dropdown(id = 't2', options = category2, value = np.sort(m2['date'].unique())[-1]),
                dcc.Graph(id='grapht2'),
                ],
                 style = {'width': '50%', 'display': 'inline-block'}),
        ]),
        dcc.Tab(label='Station 3',style=tab_style, selected_style=tab_selected_style, children=[
        html.Br(),
            html.H1(children='Table for grids'),
            html.Div([
                html.Label("Choose date"),
                dcc.Dropdown(id = 't3', options = category3, value = np.sort(m3['date'].unique())[-1]),
                dcc.Graph(id='grapht3'),
                ],
                 style = {'width': '50%', 'display': 'inline-block'}),
        ])
    ])
])
'''
if __name__ == '__main__':
    app.run_server(debug=True,port=8700)
'''
