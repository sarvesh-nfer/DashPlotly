import dash_html_components as html
import dash
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("CLUSTER PERFORMANCE MANAGEMENT DASHBOARD", className="text-center")
                    , className="mb-5 mt-5")
        ]),        
        dbc.Row([
            dbc.Col(html.Img(src="/assets/spec.png")
                    , className="mb-5 mt-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Clusters',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("CS002", href="/daily",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                dbc.Col(dbc.Button("CS003", href="/daily",
                                                                   color="primary"),
                                                        className="mt-3")], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='HEALTH OF SCANNER',
                                               className="text-center"),
                                       dbc.Button("SCANNER HEALTH",
                                                  href="/health",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Acquisition',
                                               className="text-center"),
                                       dbc.Button("Acquisition",
                                                  href="/gif",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),

    ])

])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)
