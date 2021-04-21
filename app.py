import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
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
offset=pd.read_csv("apps/angleoffset.csv")
offset=offset.dropna(subset=['load_identifier'])
offset['date'] = pd.to_datetime(offset['time_stamp']).dt.date
offset['date2']=offset['time_stamp']
offset['date'] = pd.to_datetime(offset['date'])

offset['row_col']=offset['row_index'].map(str)+','+offset['col_index'].map(str)

o1_2=offset[offset['scanner_name']=='H01CBA02P']
o2_2=offset[offset['scanner_name']=='H01CBA03P']
o3_2=offset[offset['scanner_name']=='H01CBA01P']
o4_2=offset[offset['scanner_name']=='H01CBA06P']
o1_3=offset[offset['scanner_name']=='S1']

@app.callback(Output('graphx1', 'figure'),
              [Input('x1', 'value')])
def figure_x1(input_1):
    # filter the data

    x1 = o1_2[o1_2['date']==input_1]
    x1=x1[x1['load_identifier']==np.sort(x1['load_identifier'])[-1]]
    # Create a plotly figure
    figo1 = px.scatter(x1, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "slide_name": "Slide_name",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=3500)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=1000,height=1100,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-4000, 4000])
    return figo1

@app.callback(Output('graphx11', 'figure'),
              [Input('x11', 'value')])
def figure_x11(input_1):
    # filter the data
    x11 = o1_2[o1_2['date']==input_1]
    x11=x11[x11['load_identifier']==np.sort(x11['load_identifier'])[-1]]
    # Create a plotly figure
    figo1 = px.scatter(x11, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "slide_name": "Slide_name",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=3500)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=1000,height=1100,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-4000, 4000])
    return figo1

@app.callback(Output('graphx2', 'figure'),
              [Input('x2', 'value')])
def figure_x2(input_1):
    # filter the data

    x2 = o2_2[o2_2['date']==input_1]
    x2=x2[x2['load_identifier']==np.sort(x2['load_identifier'])[-1]]
    # Create a plotly figure
    figo1 = px.scatter(x2, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "slide_name": "Slide_name",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=3500)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=1000,height=1100,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-4000, 4000])
    return figo1

@app.callback(Output('graphx22', 'figure'),
              [Input('x22', 'value')])
def figure_x22(input_1):
    # filter the data

    x22 = o2_2[o2_2['date']==input_1]
    x22=x22[x22['load_identifier']==np.sort(x22['load_identifier'])[-1]]
    # Create a plotly figure
    figo1 = px.scatter(x22, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "slide_name": "Slide_name",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=3500)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=1000,height=1100,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-4000, 4000])
    return figo1

@app.callback(Output('graphx3', 'figure'),
              [Input('x3', 'value')])
def figure_x3(input_1):
    # filter the data

    x3 = o2_2[o2_2['date']==input_1]
    x3=x3[x3['load_identifier']==np.sort(x3['load_identifier'])[-1]]
    # Create a plotly figure
    figo1 = px.scatter(x3, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "slide_name": "Slide_name",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=3500)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=1000,height=1100,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-4000, 4000])
    return figo1

@app.callback(Output('graphx33', 'figure'),
              [Input('x33', 'value')])
def figure_x33(input_1):
    # filter the data

    x33 = o3_2[o3_2['date']==input_1]
    x33=x33[x33['load_identifier']==np.sort(x33['load_identifier'])[-1]]
    # Create a plotly figure
    figo1 = px.scatter(x33, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",
                     labels={
                         "x_offset_um": "X- offset (um)",
                         "slide_name": "Slide_name",
                     },)
    figo1.update_traces(mode="markers",                 
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    figo1.add_vrect(x0=-3500, x1=3500)
    figo1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figo1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figo1.update_layout(width=1000,height=1100,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),
                     )
    figo1.update_xaxes(range=[-4000, 4000])
    return figo1

@app.callback(Output('graphy1', 'figure'),
              [Input('y1', 'value')])
def figure_y1(input_1):
    # filter the data
    y1 = o1_2[o1_2['date']==input_1]
    y1=y1[y1['load_identifier']==np.sort(y1['load_identifier'])[-1]]
    
    figy1 = px.scatter(y1, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
    figy1.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy1.add_hrect(y0=0, y1=5000)
    figy1.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy1.update_layout(width=1000,height=700,
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
    y11=y11[y11['load_identifier']==np.sort(y11['load_identifier'])[-1]]
    
    figy11 = px.scatter(y11, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
    figy11.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy11.add_hrect(y0=0, y1=5000)
    figy11.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy11.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy11.update_layout(width=1000,height=700,
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
    y3=y3[y3['load_identifier']==np.sort(y3['load_identifier'])[-1]]
    
    figy3 = px.scatter(y3, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
    figy3.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy3.add_hrect(y0=0, y1=5000)
    figy3.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy3.update_layout(width=1000,height=700,
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
    y33=y33[y33['load_identifier']==np.sort(y33['load_identifier'])[-1]]
    
    figy33 = px.scatter(y33, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
    figy33.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy33.add_hrect(y0=0, y1=5000)
    figy33.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy33.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy33.update_layout(width=1000,height=700,
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
    y2=y2[y2['load_identifier']==np.sort(y2['load_identifier'])[-1]]
    
    figy2 = px.scatter(y2, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
    figy2.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy2.add_hrect(y0=0, y1=5000)
    figy2.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy2.update_layout(width=1000,height=700,
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
    y22=y22[y22['load_identifier']==np.sort(y22['load_identifier'])[-1]]
    
    figy22 = px.scatter(y22, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
    figy22.update_traces(mode="markers",
                      marker=dict(size=5,
                                  line=dict(width=1,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    figy22.add_hrect(y0=0, y1=5000)
    figy22.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
    figy22.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figy22.update_layout(width=1000,height=700,
                      font=dict(
                          family="Courier New, monospace",
                          size=16,
                          color="RebeccaPurple"
                      ),)
    #figo11.update_layout(hovermode="y")
    figy22.update_yaxes(range=[-500, 6000])
    return figy22
#__________________________________________________________________________________________ CURRENT PLOT __________________________________________________________________________________________
current=pd.read_csv("apps/current.csv")
#current['date2'] = pd.to_datetime(offset['time_stamp']).dt.date
S1_2=current[current['scanner_name']=='H01CBA02P']
S2_2=current[current['scanner_name']=='H01CBA03P']
S3_2=current[current['scanner_name']=='H01CBA01P']
S4_2=current[current['scanner_name']=='H01CBA06P']
S1_3=current[current['scanner_name']=='S1']

@app.callback(Output('graphc1', 'figure'),
              [Input('c1', 'value')])
def figure_c1(input_1):
    c1=S1_2[S1_2['date']==input_1]
    c1=c1[c1['load_identifier']==np.sort(c1['load_identifier'])[-1]]
    c1['col_index']=np.sort(c1['col_index'])
    figc1 = px.scatter(c1, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col"],
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
                size=10,
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
    c2=c2[c2['load_identifier']==np.sort(c2['load_identifier'])[-1]]
    c2['col_index']=np.sort(c2['col_index'])
    figc2 = px.scatter(c2, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col"],
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
                size=10,
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
    c3=c3[c3['load_identifier']==np.sort(c3['load_identifier'])[-1]]
    c3['col_index']=np.sort(c3['col_index'])
    figc3 = px.scatter(c3, x="row_col", y="first_initial_current",width=1400,height=800,
                  hover_name="slide_name", hover_data=["first_initial_current", "row_col"],
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
                size=10,
                color="black"
            ),
            bgcolor="LightSteelBlue",bordercolor="Black",borderwidth=1))
    figc3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    figc3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    figc3.update_layout(hovermode="x")
    return figc3

#__________________________________________________________________________________________ angle PLOT __________________________________________________________________________________________
angle=pd.read_csv("apps/angleoffset.csv")
angle=angle.dropna(subset=['load_identifier'])
angle['date'] = pd.to_datetime(angle['time_stamp']).dt.date
angle['date2']=angle['date']
angle['date'] = pd.to_datetime(angle['date'])
a1_2=angle[angle['scanner_name']=='H01CBA02P']
a2_2=angle[angle['scanner_name']=='H01CBA03P']
a3_2=angle[angle['scanner_name']=='H01CBA06P']
a4_2=angle[angle['scanner_name']=='H01CBA05P']
a1_3=angle[angle['scanner_name']=='S1']

@app.callback(Output('grapha1', 'figure'),
              [Input('a1', 'value')])
def figure_a1(input_1):
    a1=a1_2[a1_2['date']==input_1]
    a1=a1[a1['load_identifier']==np.sort(a1['load_identifier'])[-1]]
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
                size=10,
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
    a2=a2[a2['load_identifier']==np.sort(a2['load_identifier'])[-1]]
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
                size=10,
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
    #a3=a3[a3['load_identifier']==np.sort(a3['load_identifier'])[-1]]
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
                size=10,
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

#__________________________________________________________________________________________ angle PLOT __________________________________________________________________________________________
merged=pd.read_csv("apps/merged.csv")
#dividing scanner wise

m1=merged[merged['scanner_name']=='H01CBA02P']
m2=merged[merged['scanner_name']=='H01CBA03P']
m3=merged[merged['scanner_name']=='H01CBA01P']
m4=merged[merged['scanner_name']=='H01CBA06P']

@app.callback(Output('graphs1', 'figure'),
              [Input('s1', 'value')])
def figure_s1(input_1):
    s1=m1[m1['date']==input_1]
    s1=s1[s1['load_identifier']==np.sort(s1['load_identifier'])[-1]]
    # Create figure with secondary y-axis
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig1.add_trace(
        go.Scatter(x=s1['slide_name'], y=s1['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig1.add_trace(
        go.Scatter(x=s1['slide_name'], y=s1['slide_thickness'], name="Slide",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig1.update_layout(
        title_text="Multi-Axis plot with Best-Z and slide thickness",width=1800,height=1000
    )
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig1.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
    fig1.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
    fig1.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig1

@app.callback(Output('graphs2', 'figure'),
              [Input('s2', 'value')])
def figure_s2(input_1):
    s2=m2[m2['date']==input_1]
    s2=s2[s2['load_identifier']==np.sort(s2['load_identifier'])[-1]]
    # Create figure with secondary y-axis
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig2.add_trace(
        go.Scatter(x=s2['slide_name'], y=s2['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig2.add_trace(
        go.Scatter(x=s2['slide_name'], y=s2['slide_thickness'], name="Slide",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig2.update_layout(
        title_text="Multi-Axis plot with Best-Z and slide thickness",width=1800,height=1000
    )
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig2.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
    fig2.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
    fig2.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig2

@app.callback(Output('graphs3', 'figure'),
              [Input('s3', 'value')])
def figure_s3(input_1):
    s3=m3[m3['date']==input_1]
    s3=s3[s3['load_identifier']==np.sort(s3['load_identifier'])[-1]]
    # Create figure with secondary y-axis
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig3.add_trace(
        go.Scatter(x=s3['slide_name'], y=s3['best_z'], name="best-Z",mode = 'lines+markers'),
        secondary_y=False,
    )

    fig3.add_trace(
        go.Scatter(x=s3['slide_name'], y=s3['slide_thickness'], name="Slide",mode = 'lines+markers'),
        secondary_y=True,
    )
    # Add figure title
    fig3.update_layout(
        title_text="Multi-Axis plot with Best-Z and slide thickness",width=1800,height=1000
    )
    # Set x-axis title
    #fig1.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")
    # Set y-axes titles
    fig3.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
    fig3.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
    fig3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
    fig3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
    return fig3

if __name__ == '__main__':
    app.run_server(port=8080,debug=True)
