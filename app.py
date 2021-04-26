import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
from datetime import timedelta
# must add this line in order for the app to be deployed successfully on Heroku
from index import server
from index import app
# import all pages in the app
from apps import health,daily,home,gif
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("daily", href="/daily"),
        dbc.DropdownMenuItem("health", href="/health"),
        dbc.DropdownMenuItem("Acquisition", href="/gif"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/spec3.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Report DASH", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/daily':
        return daily.app.layout
    elif pathname == '/health':
        return health.app.layout
    elif pathname == '/gif':
        return gif.app.layout
    else:
        return home.app.layout

#___________________________________________________________________________________ ANGLE offset plots____________________________________________________________________________________________
today = date.today()
yesterday = today - timedelta(days = 1)
today=str(today)
yesterday=str(yesterday)
#___________________________________________________________________________________ ANGLE offset plots____________________________________________________________________________________________
offset=pd.read_csv("apps/angleoffset.csv")
offset=offset.dropna(subset=['load_identifier'])
offset['date'] = pd.to_datetime(offset['time_stamp']).dt.date
offset['date2']=offset['time_stamp']
offset['date'] = pd.to_datetime(offset['date'])

offset['row_col']=offset['row_index'].map(str)+','+offset['col_index'].map(str)

o1_2=offset[offset['scanner_name']=='H01CBA05P']
o2_2=offset[offset['scanner_name']=='H01CBA02P']
o3_2=offset[offset['scanner_name']=='H01CBA06P']
o4_2=offset[offset['scanner_name']=='H01CBA03P']
o1_3=offset[offset['scanner_name']=='S1']

@app.callback(Output('graphx1', 'figure'),
              [Input('x1', 'value')])
def figure_x1(input_1):
    # filter the data

    x1 = o1_2[o1_2['date']==input_1]
    sar=np.sort(x1['load_identifier'])[-1]
    x1=o1_2[o1_2['load_identifier']==sar]
    # Create a plotly figure
    figo1 = px.scatter(x1, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=2000)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-3800, 2800])
    return figo1

@app.callback(Output('graphx11', 'figure'),
              [Input('x11', 'value')])
def figure_x11(input_1):
    # filter the data
    x11 = o1_2[o1_2['date']==input_1]
    sar=np.sort(x11['load_identifier'])[-1]
    x11=o1_2[o1_2['load_identifier']==sar]
    # Create a plotly figure
    figo11 = px.scatter(x11, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo11.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo11.add_vrect(x0=-2500, x1=2000)
    figo11.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo11.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo11.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo11.update_xaxes(range=[-3800, 2800])
    return figo11

@app.callback(Output('graphx2', 'figure'),
              [Input('x2', 'value')])
def figure_x2(input_1):
    # filter the data

    x2 = o2_2[o2_2['date']==input_1]
    sar=np.sort(x2['load_identifier'])[-1]
    x2=o2_2[o2_2['load_identifier']==sar]
    # Create a plotly figure
    figo2 = px.scatter(x2, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo2.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo2.add_vrect(x0=-2500, x1=2000)
    figo2.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo2.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo2.update_xaxes(range=[-3800, 2800])
    return figo2

@app.callback(Output('graphx22', 'figure'),
              [Input('x22', 'value')])
def figure_x22(input_1):
    # filter the data

    x22 = o2_2[o2_2['date']==input_1]
    sar=np.sort(x22['load_identifier'])[-1]
    x22=o2_2[o2_2['load_identifier']==sar]
    # Create a plotly figure
    figo22 = px.scatter(x22, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo22.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo22.add_vrect(x0=-2500, x1=2000)
    figo22.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo22.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo22.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo22.update_xaxes(range=[-3800, 2800])
    return figo22

@app.callback(Output('graphx3', 'figure'),
              [Input('x3', 'value')])
def figure_x3(input_1):
    # filter the data

    x3 = o3_2[o3_2['date']==input_1]
    sar=np.sort(x3['load_identifier'])[-1]
    x3=o3_2[o3_2['load_identifier']==sar]
    # Create a plotly figure
    figo3 = px.scatter(x3, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo3.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo3.add_vrect(x0=-2500, x1=2000)
    figo3.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo3.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo3.update_xaxes(range=[-3800, 2800])
    return figo3

@app.callback(Output('graphx33', 'figure'),
              [Input('x33', 'value')])
def figure_x33(input_1):
    # filter the data

    x33 = o3_2[o3_2['date']==input_1]
    sar=np.sort(x33['load_identifier'])[-1]
    x33=o3_2[o3_2['load_identifier']==sar]
    # Create a plotly figure
    figo33 = px.scatter(x33, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo33.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo33.add_vrect(x0=-2500, x1=2000)
    figo33.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo33.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo33.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo33.update_xaxes(range=[-3800, 2800])
    return figo33

@app.callback(Output('graphx4', 'figure'),
              [Input('x4', 'value')])
def figure_x4(input_1):
    # filter the data

    x4 = o4_2[o4_2['date']==input_1]
    sar=np.sort(x4['load_identifier'])[-1]
    x3=o4_2[o4_2['load_identifier']==sar]
    # Create a plotly figure
    figo4 = px.scatter(x4, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo4.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo4.add_vrect(x0=-2500, x1=2000)
    figo4.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo4.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo4.update_xaxes(range=[-3800, 2800])
    return figo4

@app.callback(Output('graphx44', 'figure'),
              [Input('x44', 'value')])
def figure_x44(input_1):
    # filter the data

    x44 = o4_2[o4_2['date']==input_1]
    sar=np.sort(x44['load_identifier'])[-1]
    x44=o4_2[o4_2['load_identifier']==sar]
    # Create a plotly figure
    figo44 = px.scatter(x44, y="row_col", x="offset_pos_x_um",hover_data=["offset_pos_x_um", "row_col","slide_name"],
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "row_col": "Row_column_Index",
                     },)
    figo44.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo44.add_vrect(x0=-2500, x1=2000)
    figo44.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo44.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo44.update_layout(width=900,height=1200,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo44.update_xaxes(range=[-3800, 2800])
    return figo44

@app.callback(Output('graphy1', 'figure'),
              [Input('y1', 'value')])
def figure_y1(input_1):
    # filter the data
    y1 = o1_2[o1_2['date']==input_1]
    sar=np.sort(y1['load_identifier'])[-1]
    y1=o1_2[o1_2['load_identifier']==sar]
    
    figy1 = px.scatter(y1, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy1.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy1.add_hrect(y0=0, y1=5000)
    figy1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy1.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figy1.update_layout(hovermode="y")
    figy1.update_yaxes(range=[-500, 6000])
    return figy1

@app.callback(Output('graphy11', 'figure'),
              [Input('y11', 'value')])
def figure_y11(input_1):
    # filter the data
    y11 = o1_2[o1_2['date']==input_1]
    sar=np.sort(y11['load_identifier'])[-1]
    y11=o1_2[o1_2['load_identifier']==sar]
    
    figy11 = px.scatter(y11, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy11.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy11.add_hrect(y0=0, y1=5000)
    figy11.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy11.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy11.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figo11.update_layout(hovermode="y")
    figy11.update_yaxes(range=[-500, 6000])
    return figy11

@app.callback(Output('graphy3', 'figure'),
              [Input('y3', 'value')])
def figure_y3(input_1):
    # filter the data
    y3 = o3_2[o3_2['date']==input_1]
    sar=np.sort(y3['load_identifier'])[-1]
    y3=o3_2[o3_2['load_identifier']==sar]
    
    figy3 = px.scatter(y3, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy3.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy3.add_hrect(y0=0, y1=5000)
    figy3.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy3.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figy1.update_layout(hovermode="y")
    figy3.update_yaxes(range=[-500, 6000])
    return figy3

@app.callback(Output('graphy33', 'figure'),
              [Input('y33', 'value')])
def figure_y33(input_1):
    # filter the data
    y33 = o3_2[o3_2['date']==input_1]
    sar=np.sort(y33['load_identifier'])[-1]
    y33=o3_2[o3_2['load_identifier']==sar]
    
    figy33 = px.scatter(y33, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy33.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy33.add_hrect(y0=0, y1=5000)
    figy33.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy33.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy33.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figo33.update_layout(hovermode="y")
    figy33.update_yaxes(range=[-500, 6000])
    return figy33

@app.callback(Output('graphy2', 'figure'),
              [Input('y2', 'value')])
def figure_y2(input_1):
    # filter the data
    y2 = o2_2[o2_2['date']==input_1]
    sar=np.sort(y2['load_identifier'])[-1]
    y2=o2_2[o2_2['load_identifier']==sar]
    
    figy2 = px.scatter(y2, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy2.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy2.add_hrect(y0=0, y1=5000)
    figy2.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy2.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figy1.update_layout(hovermode="y")
    figy2.update_yaxes(range=[-500, 6000])
    return figy2

@app.callback(Output('graphy22', 'figure'),
              [Input('y22', 'value')])
def figure_y22(input_1):
    # filter the data
    y22 = o2_2[o2_2['date']==input_1]
    sar=np.sort(y22['load_identifier'])[-1]
    y22=o2_2[o2_2['load_identifier']==sar]
    
    figy22 = px.scatter(y22, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy22.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy22.add_hrect(y0=0, y1=5000)
    figy22.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy22.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy22.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figo11.update_layout(hovermode="y")
    figy22.update_yaxes(range=[-500, 6000])
    return figy22
    
@app.callback(Output('graphy4', 'figure'),
              [Input('y4', 'value')])
def figure_y4(input_1):
    # filter the data
    y4 = o4_2[o4_2['date']==input_1]
    sar=np.sort(y4['load_identifier'])[-1]
    y4=o4_2[o4_2['load_identifier']==sar]
    
    figy4 = px.scatter(y4, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy4.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy4.add_hrect(y0=0, y1=5000)
    figy4.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy4.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figy4.update_layout(hovermode="y")
    figy4.update_yaxes(range=[-500, 6000])
    return figy4

@app.callback(Output('graphy44', 'figure'),
              [Input('y44', 'value')])
def figure_y44(input_1):
    # filter the data
    y44 = o4_2[o4_2['date']==input_1]
    sar=np.sort(y44['load_identifier'])[-1]
    y44=o4_2[o4_2['load_identifier']==sar]
    
    figy44 = px.scatter(y44, x="row_col", y="offset_pos_y_um",hover_data=["offset_pos_y_um", "row_col","slide_name"],
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "row_col": "Row_column_Index",
                 },)
    figy44.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figy44.add_hrect(y0=0, y1=5000)
    figy44.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy44.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy44.update_layout(width=1000,height=500,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figy44.update_layout(hovermode="y")
    figy44.update_yaxes(range=[-500, 6000])
    return figy44
#__________________________________________________________________________________________ CURRENT PLOT __________________________________________________________________________________________
current=pd.read_csv("apps/current.csv")
#current['date2'] = pd.to_datetime(offset['time_stamp']).dt.date
S1_2=current[current['scanner_name']=='H01CBA05P']
S2_2=current[current['scanner_name']=='H01CBA02P']
S3_2=current[current['scanner_name']=='H01CBA06P']
S4_2=current[current['scanner_name']=='H01CBA03P']
S1_3=current[current['scanner_name']=='S1']

@app.callback(Output('graphc1', 'figure'),
              [Input('c1', 'value')])
def figure_c1(input_1):
    c1=S1_2[S1_2['date']==input_1]
    sar=np.sort(c1['load_identifier'])[-1]
    c1=S1_2[S1_2['load_identifier']==sar]
    figc1 = px.scatter(c1, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col","load_identifier","date"],
                 labels={"first_initial_current": "Current Reading (A)",
                         "row_col": "Row_column_index",
                        })
    figc1.add_scatter(x=c1['row_col'], y=c1['first_final_current'],mode="markers+lines",name="final_current",
                    text=c1['first_final_current'],hoverinfo='text',)
    figc1.add_scatter(x=c1['row_col'], y=c1['first_current_diff'],mode="markers+lines",name="Difference_current",
                    text=c1['first_current_diff'],hoverinfo='text',)
    figc1.update_traces(mode="markers+lines",showlegend=True,
    name='initial_current',marker=dict(size=5,line=dict(width=1,color='DarkSlateGrey')),
    selector=dict(mode='markers'))
    figc1.update_layout(
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    figc1.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figc1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figc1.update_layout(hovermode="x")
    return figc1

@app.callback(Output('graphc2', 'figure'),
              [Input('c2', 'value')])
def figure_c2(input_1):
    c2=S2_2[S2_2['date']==input_1]
    sar=np.sort(c2['load_identifier'])[-1]
    c2=S2_2[S2_2['load_identifier']==sar]
    figc2 = px.scatter(c2, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col","load_identifier","date"],
                 labels={"first_initial_current": "Current Reading (A)",
                         "row_col": "Row_column_index",
                        })
    figc2.add_scatter(x=c2['row_col'], y=c2['first_final_current'],mode="markers+lines",name="final_current",
                    text=c2['first_final_current'],hoverinfo='text',)
    figc2.add_scatter(x=c2['row_col'], y=c2['first_current_diff'],mode="markers+lines",name="Difference_current",
                    text=c2['first_current_diff'],hoverinfo='text',)
    figc2.update_traces(mode="markers+lines",showlegend=True,
    name='initial_current',marker=dict(size=5,line=dict(width=1,color='DarkSlateGrey')),
    selector=dict(mode='markers'))
    figc2.update_layout(
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    figc2.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figc2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figc2.update_layout(hovermode="x")
    return figc2

@app.callback(Output('graphc3', 'figure'),
              [Input('c3', 'value')])
def figure_c3(input_1):
    c3=S3_2[S3_2['date']==input_1]
    sar=np.sort(c3['load_identifier'])[-1]
    c3=S3_2[S3_2['load_identifier']==sar]
    figc3 = px.scatter(c3, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col","load_identifier","date"],
                 labels={"first_initial_current": "Current Reading (A)",
                         "row_col": "Row_column_index",
                        })
    figc3.add_scatter(x=c3['row_col'], y=c3['first_final_current'],mode="markers+lines",name="final_current",
                    text=c3['first_final_current'],hoverinfo='text',)
    figc3.add_scatter(x=c3['row_col'], y=c3['first_current_diff'],mode="markers+lines",name="Difference_current",
                    text=c3['first_current_diff'],hoverinfo='text',)
    figc3.update_traces(mode="markers+lines",showlegend=True,
    name='initial_current',marker=dict(size=5,line=dict(width=1,color='DarkSlateGrey')),
    selector=dict(mode='markers'))
    figc3.update_layout(
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    figc3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figc3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figc3.update_layout(hovermode="x")
    return figc3
@app.callback(Output('graphc4', 'figure'),
              [Input('c4', 'value')])
def figure_c4(input_1):
    c4=S4_2[S4_2['date']==input_1]
    sar=np.sort(c4['load_identifier'])[-1]
    c4=S4_2[S4_2['load_identifier']==sar]
    figc4 = px.scatter(c4, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col","load_identifier","date"],
                 labels={"first_initial_current": "Current Reading (A)",
                         "row_col": "Row_column_index",
                        })
    figc4.add_scatter(x=c4['row_col'], y=c4['first_final_current'],mode="markers+lines",name="final_current",
                    text=c4['first_final_current'],hoverinfo='text',)
    figc4.add_scatter(x=c4['row_col'], y=c4['first_current_diff'],mode="markers+lines",name="Difference_current",
                    text=c4['first_current_diff'],hoverinfo='text',)
    figc4.update_traces(mode="markers+lines",showlegend=True,
    name='initial_current',marker=dict(size=5,line=dict(width=1,color='DarkSlateGrey')),
    selector=dict(mode='markers'))
    figc4.update_layout(
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    figc4.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figc4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figc4.update_layout(hovermode="x")
    return figc4
#__________________________________________________________________________________________ angle PLOT __________________________________________________________________________________________
angle=pd.read_csv("apps/angleoffset.csv")
angle=angle.dropna(subset=['load_identifier'])
angle['date'] = pd.to_datetime(angle['time_stamp']).dt.date
angle['date2']=angle['date']
angle['date'] = pd.to_datetime(angle['date'])
a1_2=angle[angle['scanner_name']=='H01CBA05P']
a2_2=angle[angle['scanner_name']=='H01CBA02P']
a3_2=angle[angle['scanner_name']=='H01CBA06P']
a4_2=angle[angle['scanner_name']=='H01CBA03P']
a1_3=angle[angle['scanner_name']=='S1']

@app.callback(Output('grapha1', 'figure'),
              [Input('a1', 'value')])
def figure_a1(input_1):
    a1=a1_2[a1_2['date']==input_1]
    sar=np.sort(a1['load_identifier'])[-1]
    a1=a1_2[a1_2['load_identifier']==sar]
    # Create figure with secondary y-axis
    figa1 = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    figa1.add_trace(
        go.Scatter(x=a1['row_col'], y=a1['permissible_angle'], name="permissible_angle",mode = 'lines+markers',
                text=a1['slide_name'],hoverinfo='text',)
    )
    figa1.add_trace(
        go.Scatter(x=a1['row_col'], y=a1['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
        secondary_y=False,
    )
    figa1.add_trace(
        go.Scatter(x=a1['row_col'], y=a1['slide_height_mm'], name="Slide_height (mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    figa1.update_layout(width=1400,height=800,
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    # Set x-axis title
    figa1.update_xaxes(title_text="Row_Column_Index")
    # Set y-axes titles
    figa1.update_yaxes(title_text="<b>secondary</b> Slide_height(mm) ", secondary_y=True)
    figa1.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
    figa1.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figa1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figa1.update_layout(hovermode="x unified")
    return figa1

@app.callback(Output('grapha2', 'figure'),
              [Input('a2', 'value')])
def figure_a2(input_1):
    a2=a2_2[a2_2['date']==input_1]
    sar=np.sort(a2['load_identifier'])[-1]
    a2=a2_2[a2_2['load_identifier']==sar]
    # Create figure with secondary y-axis
    figa2 = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    figa2.add_trace(
        go.Scatter(x=a2['row_col'], y=a2['permissible_angle'], name="permissible_angle",mode = 'lines+markers',
                text=a2['slide_name'],hoverinfo='text',)
    )
    figa2.add_trace(
        go.Scatter(x=a2['row_col'], y=a2['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
        secondary_y=False,
    )
    figa2.add_trace(
        go.Scatter(x=a2['row_col'], y=a2['slide_height_mm'], name="Slide_height (mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    figa2.update_layout(width=1400,height=800,
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    # Set x-axis title
    figa2.update_xaxes(title_text="Row_Column_Index")
    # Set y-axes titles
    figa2.update_yaxes(title_text="<b>secondary</b> Slide_height(mm) ", secondary_y=True)
    figa2.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
    figa2.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figa2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figa2.update_layout(hovermode="x unified")
    return figa2

@app.callback(Output('grapha3', 'figure'),
              [Input('a3', 'value')])
def figure_a3(input_1):
    a3=a3_2[a3_2['date']==input_1]
    sar=np.sort(a3['load_identifier'])[-1]
    a3=a3_2[a3_2['load_identifier']==sar]
    # Create figure with secondary y-axis
    figa3 = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    figa3.add_trace(
        go.Scatter(x=a3['row_col'], y=a3['permissible_angle'], name="permissible_angle",mode = 'lines+markers',
                text=a3['slide_name'],hoverinfo='text',)
    )
    figa3.add_trace(
        go.Scatter(x=a3['row_col'], y=a3['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
        secondary_y=False,
    )
    figa3.add_trace(
        go.Scatter(x=a3['row_col'], y=a3['slide_height_mm'], name="Slide_height (mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    figa3.update_layout(width=1400,height=800,
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    # Set x-axis title
    figa3.update_xaxes(title_text="Row_Column_Index")
    # Set y-axes titles
    figa3.update_yaxes(title_text="<b>secondary</b> Slide_height(mm) ", secondary_y=True)
    figa3.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
    figa3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figa3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figa3.update_layout(hovermode="x unified")
    return figa3

@app.callback(Output('grapha4', 'figure'),
              [Input('a4', 'value')])
def figure_a4(input_1):
    a4=a4_2[a4_2['date']==input_1]
    sar=np.sort(a4['load_identifier'])[-1]
    a4=a4_2[a4_2['load_identifier']==sar]
    # Create figure with secondary y-axis
    figa4 = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    figa4.add_trace(
        go.Scatter(x=a4['row_col'], y=a4['permissible_angle'], name="permissible_angle",mode = 'lines+markers',
                text=a4['slide_name'],hoverinfo='text',)
    )
    figa4.add_trace(
        go.Scatter(x=a4['row_col'], y=a4['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
        secondary_y=False,
    )
    figa4.add_trace(
        go.Scatter(x=a4['row_col'], y=a4['slide_height_mm'], name="Slide_height (mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    figa4.update_layout(width=1400,height=800,
        legend=dict(
            traceorder="reversed",
            font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    # Set x-axis title
    figa4.update_xaxes(title_text="Row_Column_Index")
    # Set y-axes titles
    figa4.update_yaxes(title_text="<b>secondary</b> Slide_height(mm) ", secondary_y=True)
    figa4.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
    figa4.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figa4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figa4.update_layout(hovermode="x unified")
    return figa4
#__________________________________________________________________________________________ Z vs thicc PLOT __________________________________________________________________________________________
merged=pd.read_csv("apps/merged.csv")
#dividing scanner wise

m1=merged[merged['scanner_name']=='H01CBA05P']
m2=merged[merged['scanner_name']=='H01CBA02P']
m3=merged[merged['scanner_name']=='H01CBA06P']
m4=merged[merged['scanner_name']=='H01CBA03P']

@app.callback(Output('graphs1', 'figure'),
              [Input('s1', 'value')])
def figure_s1(input_1):
    s1=m1[m1['date_x']==input_1]
    sar=np.sort(s1['load_identifier'])[-1]
    s1=m1[m1['load_identifier']==sar]
    # Create figure with secondary y-axis
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig1.add_trace(
        go.Scatter(x=s1['slide_name'], y=s1['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig1.add_trace(
        go.Scatter(x=s1['slide_name'], y=s1['slide_thickness'], name="Slide thickness(mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig1.update_layout(width=1800,height=1000,
                font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ))
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig1.update_yaxes(title_text="<b>primary</b> Best-Z", secondary_y=False)
    fig1.update_yaxes(title_text="<b>secondary</b> Slide Thickness(mm)", secondary_y=True)
    fig1.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig1

@app.callback(Output('graphs2', 'figure'),
              [Input('s2', 'value')])
def figure_s2(input_1):
    s2=m2[m2['date_x']==input_1]
    sar=np.sort(s2['load_identifier'])[-1]
    s2=m2[m2['load_identifier']==sar]
    # Create figure with secondary y-axis
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig2.add_trace(
        go.Scatter(x=s2['slide_name'], y=s2['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig2.add_trace(
        go.Scatter(x=s2['slide_name'], y=s2['slide_thickness'], name="Slide thickness(mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig2.update_layout(width=1800,height=1000,
                font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ))
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig2.update_yaxes(title_text="<b>primary</b> Best-Z", secondary_y=False)
    fig2.update_yaxes(title_text="<b>secondary</b> Slide thickness(mm)", secondary_y=True)
    fig2.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig2

@app.callback(Output('graphs3', 'figure'),
              [Input('s3', 'value')])
def figure_s3(input_1):
    s3=m3[m3['date_x']==input_1]
    sar=np.sort(s3['load_identifier'])[-1]
    s3=m3[m3['load_identifier']==sar]
    # Create figure with secondary y-axis
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig3.add_trace(
        go.Scatter(x=s3['slide_name'], y=s3['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig3.add_trace(
        go.Scatter(x=s3['slide_name'], y=s3['slide_thickness'], name="Slide thickness(mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig3.update_layout(width=1800,height=1000,
                font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ))
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig3.update_yaxes(title_text="<b>primary</b> Best-Z", secondary_y=False)
    fig3.update_yaxes(title_text="<b>secondary</b> Slide thickness(mm)", secondary_y=True)
    fig3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig3
@app.callback(Output('graphs4', 'figure'),
              [Input('s4', 'value')])
def figure_s4(input_1):
    s4=m4[m4['date_x']==input_1]
    sar=np.sort(s4['load_identifier'])[-1]
    s4=m4[m4['load_identifier']==sar]
    # Create figure with secondary y-axis
    fig4 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig4.add_trace(

        go.Scatter(x=s4['slide_name'], y=s4['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig4.add_trace(
        go.Scatter(x=s4['slide_name'], y=s4['slide_thickness'], name="Slide thickness(mm)",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig4.update_layout(width=1800,height=1000,
                font=dict(
                family="Times New Roman,monospace",
                size=16,
                color="black"
            ))
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig4.update_yaxes(title_text="<b>primary</b> Best-Z", secondary_y=False)
    fig4.update_yaxes(title_text="<b>secondary</b> Slide thickness(mm)", secondary_y=True)
    fig4.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig4
#__________________________________________________________________________________________ acq PLOT __________________________________________________________________________________________
parse=pd.read_csv("apps/parse_bb.csv")

cols=['slide_name','blob_index','Biopsy','Debris','Background','date']

parse[['scanner_name','slide_id','1','2']]=parse["slide_name"].str.split("_",expand=True)
parse=parse.drop(['1','2'],axis=1)

parse['Biopsy']=parse['Biopsy'].replace([True,False],['true','false'])
parse['Debris']=parse['Debris'].replace([True,False],['true','false'])
parse['Background']=parse['Background'].replace([True,False],['true','false'])

par1=parse[parse['scanner_name']=='H01CBA05P']
par2=parse[parse['scanner_name']=='H01CBA02P']
par3=parse[parse['scanner_name']=='H01CBA06P']
par4=parse[parse['scanner_name']=='H01CBA03P']

@app.callback(Output('grapht1', 'figure'),
              [Input('t1', 'value')])
def figure_t1(input_1):
    t1=par1[par1['date']>=str(input_1)]
    
    layout=dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df[['slide_name','blob_index','Biopsy','Debris','Background','date']]],
    data=df.to_dict('records'),
    export_format="csv",
    editable=False,
    style_data_conditional=[
        {
            'if': {
                'filter_query': '{Debris} = true',
                'column_id': 'Debris',
            },
            'backgroundColor': 'lightgreen'
        },
        {
            'if': {
                'filter_query': '{Background} = true',
                'column_id': 'Background',
            },
            'backgroundColor': 'lightgreen'
        },
        {
            'if': {
                'filter_query': '{Biopsy} = true',
                'column_id': 'Biopsy',
            },
            'backgroundColor': 'lightgreen'
        },
        {
            'if': {
                'state': 'active'  # 'active' | 'selected'
            },
           'backgroundColor': 'rgba(0, 116, 217, 0.3)',
           'border': '1px solid rgb(0, 116, 217)'
        }

    ]
)

@app.callback(Output('grapht2', 'figure'),
              [Input('t2', 'value')])
def figure_t2(input_1):
    t2=par2[par2['date']>=input_1]
    fill_color = []
    n = len(t2)
    for col in cols:
        if col == 'Debris':
            fill_color.append(t2["color2"].to_list())
        elif col == 'Biopsy':
            fill_color.append(t2["color1"].to_list())
        elif col == 'Background':
            fill_color.append(t2["color3"].to_list())
        else:
            fill_color.append(['#e6f2fd']*n)
    data=[go.Table(columnwidth = [100,50,50,50,50],
    header=dict(values=[f"<b>{col}</b>" for col in cols],
                # fill_color='#b9e2ff',
                line_color='red',
                align='center',
                font=dict(color='black', family="Lato", size=20),
                height=30
                ),
               cells=dict(values=t2[cols].values.T,
               fill_color=fill_color,
               line_color='black',
               align='center',
               font=dict(color='black', family="Lato", size=20),
               height=30
               ))]
    figt2 = go.Figure(data=data)
    figt2.update_layout(width=1000, height=800)
    return figt2

@app.callback(Output('grapht3', 'figure'),
              [Input('t3', 'value')])
def figure_t2(input_1):
    t3=par3[par3['date']>=input_1]
    
    fill_color = []
    n = len(t3)
    for col in cols:
        if col == 'Debris':
            fill_color.append(t3["color2"].to_list())
        elif col == 'Biopsy':
            fill_color.append(t3["color1"].to_list())
        elif col == 'Background':
            fill_color.append(t3["color3"].to_list())
        else:
            fill_color.append(['#e6f2fd']*n)
    data=[go.Table(columnwidth = [100,50,50,50,50],
    header=dict(values=[f"<b>{col}</b>" for col in cols],
                # fill_color='#b9e2ff',
                line_color='red',
                align='center',
                font=dict(color='black', family="Lato", size=20),
                height=30
                ),
               cells=dict(values=t3[cols].values.T,
               fill_color=fill_color,
               line_color='black',
               align='center',
               font=dict(color='black', family="Lato", size=20),
               height=30
               ))]
    figt3 = go.Figure(data=data)
    figt3.update_layout(width=1000, height=800)
    return figt3
if __name__ == '__main__':
    app.run_server(port=8080,debug=True)
