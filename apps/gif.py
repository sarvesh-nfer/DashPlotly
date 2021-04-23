import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import dash_table
from datetime import date
from datetime import timedelta
#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________code for Dash_______________________________________________________________________________________________________

today = date.today()
yesterday = today - timedelta(days = 1)
today=str(today)
yesterday=str(yesterday)

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

parse=parse[parse['date']>=yesterday]
parse['Biopsy']=parse['Biopsy'].replace([True,False],['true','false'])
parse['Debris']=parse['Debris'].replace([True,False],['true','false'])
parse['Background']=parse['Background'].replace([True,False],['true','false'])
m1=parse[parse['scanner_name']=='H01CBA05P']
m2=parse[parse['scanner_name']=='H01CBA03P']
m3=parse[parse['scanner_name']=='H01CBA01P']
m4=parse[parse['scanner_name']=='H01CBA02P']

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
                dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in m1[['slide_name','blob_index','Biopsy','Debris','Background','date']]],
                        data=m1.to_dict('records'),
                        export_format="csv",
                        editable=False,
                        style_header={'backgroundColor': 'rgb(30, 30, 30)','border': '1px solid pink'},
                        style_data={ 'border': '1px solid blue' },
                        style_cell = {'font_family': 'cursive','font_size': '26px','text_align': 'center'},
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

        ]),
        dcc.Tab(label='Station 2',style=tab_style, selected_style=tab_selected_style, children=[
                html.Br(),
            html.H1(children='Table for grids'),
                dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in m2[['slide_name','blob_index','Biopsy','Debris','Background','date']]],
                        data=m2.to_dict('records'),
                        export_format="csv",
                        editable=False,
                        style_header={'backgroundColor': 'rgb(30, 30, 30)','border': '1px solid pink'},
                        style_data={ 'border': '1px solid blue' },
                        style_cell = {'font_family': 'cursive','font_size': '26px','text_align': 'center'},
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

        ]),
        dcc.Tab(label='Station 3',style=tab_style, selected_style=tab_selected_style, children=[
                html.Br(),
            html.H1(children='Table for grids'),
                dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in m3[['slide_name','blob_index','Biopsy','Debris','Background','date']]],
                        data=m3.to_dict('records'),
                        export_format="csv",
                        editable=False,
                        style_header={'backgroundColor': 'rgb(30, 30, 30)','border': '1px solid pink'},
                        style_data={ 'border': '1px solid blue' },
                        style_cell = {'font_family': 'cursive','font_size': '26px','text_align': 'center'},
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
        ])
    ])
])
'''
if __name__ == '__main__':
    app.run_server(debug=True,port=8700)
'''
