import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import date
from datetime import timedelta


df=pd.read_csv("https://raw.githubusercontent.com/MONSTERharper/extra/main/errorscan.csv")
es1=df[df['ID']=='S1']
es2=df[df['ID']=='S2']
es3=df[df['ID']=='S3']
es4=df[df['ID']=='S4']


fig11 = go.Figure()
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['No grid found'],name='No grid found',text=es1['No grid found'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['Error during restoration'],name='Error during restoration',text=es1['Error during restoration'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['slide thickness error'],name='slide thickness error',text=es1['slide thickness error'],textposition='auto',textfont_size=20,))
#fig11.add_trace(go.Bar(x=es1['Date'], y=es1['Untarring error'],name='untarring error',text=es1['untarring error']))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['Can not place slide'],name='Can not place slide',text=es1['Can not place slide'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['Snap Miss'],name='Snap Miss',text=es1['Snap Miss'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['Failed to Lock Slide'],name='Failed to Lock Slide',text=es1['Failed to Lock Slide'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['Slider did not move'],name='Slider did not move',text=es1['Slider did not move'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['No slide detected'],name='No slide detected',text=es1['No slide detected'],textposition='auto',textfont_size=20,))
fig11.add_trace(go.Bar(x=es1['Date'], y=es1['computed tilt'],name='computed tilt',text=es1['computed tilt'],textposition='auto',textfont_size=20,))
fig11.update_layout(barmode='stack', title_text='Stacked Error trend of s1',xaxis_title="Scan Date",yaxis_title="Number of errors",height=700)

#fig11.show()

fig12 = go.Figure()
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['No grid found'],name='No grid found',text=es2['No grid found'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['Error during restoration'],name='Error during restoration',text=es2['Error during restoration'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['slide thickness error'],name='slide thickness error',text=es2['slide thickness error'],textposition='auto',textfont_size=20,))
#fig12.add_trace(go.Bar(x=es2['Date'], y=es2['Untarring error'],name='untarring error',text=es2['untarring error']))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['Can not place slide'],name='Can not place slide',text=es2['Can not place slide'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['Snap Miss'],name='Snap Miss',text=es2['Snap Miss'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['Failed to Lock Slide'],name='Failed to Lock Slide',text=es2['Failed to Lock Slide'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['Slider did not move'],name='Slider did not move',text=es2['Slider did not move'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['No slide detected'],name='No slide detected',text=es2['No slide detected'],textposition='auto',textfont_size=20,))
fig12.add_trace(go.Bar(x=es2['Date'], y=es2['computed tilt'],name='computed tilt',text=es2['computed tilt'],textposition='auto',textfont_size=20,))
fig12.update_layout(barmode='stack', title_text='Stacked Error trend of s2',xaxis_title="Scan Date",yaxis_title="Number of errors",height=700)

#fig12.show()

fig13 = go.Figure()
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['No grid found'],name='No grid found',text=es3['No grid found'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['Error during restoration'],name='Error during restoration',text=es3['Error during restoration'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['slide thickness error'],name='slide thickness error',text=es3['slide thickness error'],textposition='auto',textfont_size=20,))
#fig13.add_trace(go.Bar(x=es3['Date'], y=es3['Untarring error'],name='untarring error',text=es3['untarring error']))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['Can not place slide'],name='Can not place slide',text=es3['Can not place slide'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['Snap Miss'],name='Snap Miss',text=es3['Snap Miss'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['Failed to Lock Slide'],name='Failed to Lock Slide',text=es3['Failed to Lock Slide'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['Slider did not move'],name='Slider did not move',text=es3['Slider did not move'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['No slide detected'],name='No slide detected',text=es3['No slide detected'],textposition='auto',textfont_size=20,))
fig13.add_trace(go.Bar(x=es3['Date'], y=es3['computed tilt'],name='computed tilt',text=es3['computed tilt'],textposition='auto',textfont_size=20,))
fig13.update_layout(barmode='stack', title_text='Stacked Error trend of s3',xaxis_title="Scan Date",yaxis_title="Number of errors",height=700)

#fig13.show()

fig14 = go.Figure()
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['No grid found'],name='No grid found',text=es4['No grid found'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['Error during restoration'],name='Error during restoration',text=es4['Error during restoration'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['slide thickness error'],name='slide thickness error',text=es4['slide thickness error'],textposition='auto',textfont_size=20,))
#fig14.add_trace(go.Bar(x=es4['Date'], y=es4['Untarring error'],name='untarring error',text=es4['untarring error']))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['Can not place slide'],name='Can not place slide',text=es4['Can not place slide'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['Snap Miss'],name='Snap Miss',text=es4['Snap Miss'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['Failed to Lock Slide'],name='Failed to Lock Slide',text=es4['Failed to Lock Slide'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['Slider did not move'],name='Slider did not move',text=es4['Slider did not move'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['No slide detected'],name='No slide detected',text=es4['No slide detected'],textposition='auto',textfont_size=20,))
fig14.add_trace(go.Bar(x=es4['Date'], y=es4['computed tilt'],name='computed tilt',text=es4['computed tilt'],textposition='auto',textfont_size=20,))
fig14.update_layout(barmode='stack', title_text='Stacked Error trend of s4',xaxis_title="Scan Date",yaxis_title="Number of errors",height=700)


#fig14.show()



data=pd.read_csv("https://raw.githubusercontent.com/MONSTERharper/extra/main/vis.csv")
s1=data[data['ID']=='S1']
s2=data[data['ID']=='S2']
s3=data[data['ID']=='S3']
s4=data[data['ID']=='S4']

##for latest tab

#df2=data.iloc[-4:]## for latest 4 data

##latest graph
###attempt for gauge chart
df2=data.iloc[-4:]
value1=df2['Total Scans'].iloc[0]
value2=df2['Total Scans'].iloc[1]
value3=df2['Total Scans'].iloc[2]
value4=df2['Total Scans'].iloc[3]

#####plots to be for gauge

fig64 = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = value1,
    domain = {'x': [0, 1], 'y': [0, 1]},
    delta = {'reference': 120, 'increasing': {'color': "Red"}},
    gauge = {
        'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 40], 'color': 'Red'},
            {'range': [40, 60], 'color': 'orange'},
            {'range': [60, 80], 'color': 'yellow'},
            {'range': [80, 120], 'color': 'green'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 1,
            'value': 120}}))
fig64.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
import plotly.graph_objects as go
fig65 = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = value2,
    domain = {'x': [0, 1], 'y': [0, 1]},
    delta = {'reference': 120, 'increasing': {'color': "Red"}},
    gauge = {
        'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 40], 'color': 'Red'},
            {'range': [40, 60], 'color': 'orange'},
            {'range': [60, 80], 'color': 'yellow'},
            {'range': [80, 120], 'color': 'green'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 1,
            'value': 120}}))
fig65.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
import plotly.graph_objects as go
fig66 = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = value3,
    #domain = {'x': [0, 1], 'y': [0, 1]},
    delta = {'reference': 120, 'increasing': {'color': "Red"}},
    gauge = {
        'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 40], 'color': 'Red'},
            {'range': [40, 60], 'color': 'orange'},
            {'range': [60, 80], 'color': 'yellow'},
            {'range': [80, 120], 'color': 'green'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 1,
            'value': 120}}))
fig66.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
import plotly.graph_objects as go
fig67 = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = value4,
    domain = {'x': [0, 1], 'y': [0, 1]},
    delta = {'reference': 120, 'increasing': {'color': "Red"}},
    gauge = {
        'axis': {'range': [None, 120], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 40], 'color': 'Red'},
            {'range': [40, 60], 'color': 'orange'},
            {'range': [60, 80], 'color': 'yellow'},
            {'range': [80, 120], 'color': 'green'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 1,
            'value': 120}}))
fig67.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})


###########

fig45 = go.Figure(data=[go.Bar(
    x=df2['ID'],
    y=df2['Total Scans'],text=df2['Total Scans'],textposition='auto',hovertext=df2['Date'])])
fig45.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',marker_line_width=5,textfont_size=52)
fig45.update_layout(
    title_text='Daily Scanners Report', # title of plot
    xaxis_title_text='Scanners', # xaxis label
    yaxis_title_text='Count of Slides Scanned',
    height=800 # yaxis label
)
fig45.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/MONSTERharper/extra/main/spec2.png",
            xref="x",
            yref="y",
            x=0.0000001,
            y=55,
            sizex=40,
            sizey=60,
            opacity=0.1,
            layer="below")
)
#fig45.show()




fig = px.line(x=s1['Date'], y=s1['Positive'],text=s1['Positive'])
fig.update_traces(textposition='bottom center',name='Positive %', showlegend = True,textfont_size=20,)
fig.update_traces(line_color='darkviolet') 
colors = ['lightblue',] * len(s1) 
colors[len(s1)-1] = '#44bd32'
fig.add_bar(x=s1['Date'], y=s1['Total Scans'],text=s1['Total Scans'],marker_color=colors,textposition='auto',textfont_size=20,name='Count of scans')
fig.update_layout(barmode='overlay')
colors = ['blue',] * len(s1)
colors[len(s1)-1] = '#44bd32'
fig.update_layout(
    title_text='Daily S1 Report', # title of plot
    xaxis_title_text='Date of Scan S1', # xaxis label
    yaxis_title_text='Count of Slides Scanned',
    height=700 # yaxis label
)

#fig.show()

fig2 = px.line(x=s2['Date'], y=s2['Positive'],text=s2['Positive'])
fig2.update_traces(textposition='bottom center',name='Positive %', showlegend = True,textfont_size=20)
fig2.update_traces(line_color='darkviolet') 
colors = ['lightblue',] * len(s2) 
colors[len(s2)-1] = '#44bd32'
fig2.add_bar(x=s2['Date'], y=s2['Total Scans'],text=s2['Total Scans'],marker_color=colors,textposition='auto',textfont_size=20,name='Count of scans')
fig2.update_layout(barmode='overlay')
colors = ['blue',] * len(s2)
colors[len(s2)-1] = '#44bd32'
fig2.update_layout(
    title_text='Daily S2 Report', # title of plot
    xaxis_title_text='Date of Scan S2', # xaxis label
    yaxis_title_text='Count of Slides Scanned', # yaxis label
    height=700
)

#fig2.show()

fig3 = px.line(x=s3['Date'], y=s3['Positive'],text=s3['Positive'])
fig3.update_traces(textposition='bottom center',name='Positive %', showlegend = True,textfont_size=20)
fig3.update_traces(line_color='darkviolet') 
colors = ['lightblue',] * len(s3)
colors[len(s3)-1] = '#44bd32'
fig3.add_bar(x=s3['Date'], y=s3['Total Scans'],text=s3['Total Scans'],marker_color=colors,textposition='auto',textfont_size=20,name='Count of scans')
fig3.update_layout(barmode='overlay')
colors = ['blue',] * len(s3)
colors[len(s3)-1] = '#44bd32'
fig3.update_layout(
    title_text='Daily S3 Report', # title of plot
    xaxis_title_text='Date of Scan S3', # xaxis label
    yaxis_title_text='Count of Slides Scanned', # yaxis label
    height=700
)

#fig3.show()

fig4 = px.line(x=s4['Date'], y=s4['Positive'],text=s4['Positive'])
fig4.update_traces(textposition='bottom center',name='Positive %', showlegend = True,textfont_size=20)
fig4.update_traces(line_color='darkviolet') 
colors = ['lightblue',] * len(s4)
colors[len(s4)-1] = '#44bd32'
fig4.add_bar(x=s4['Date'], y=s4['Total Scans'],text=s4['Total Scans'],marker_color=colors,textposition='auto',textfont_size=20,name='Count of scans')
fig4.update_layout(barmode='overlay')
colors = ['blue',] * len(s4)
colors[len(s4)-1] = '#44bd322'
fig4.update_layout(
    title_text='Daily S4 Report', # title of plot
    xaxis_title_text='Date of Scan S4', # xaxis label
    yaxis_title_text='Count of Slides Scanned', # yaxis label
    height=700
)

#fig4.show()

fig7 = go.Figure()
fig7.add_trace(go.Bar(x=df['Date'], y=df['No grid found'],name='No grid found',text=df['No grid found'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['Error during restoration'],name='Error during restoration',text=df['Error during restoration'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['slide thickness error'],name='slide thickness error',text=df['slide thickness error'],textposition='auto',textfont_size=20,hovertext=df['ID']))
#fig7.add_trace(go.Bar(x=df['Date'], y=df['Untarring error'],name='untarring error',text=df['untarring error']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['Can not place slide'],name='Can not place slide',text=df['Can not place slide'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['Snap Miss'],name='Snap Miss',text=df['Snap Miss'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['Failed to Lock Slide'],name='Failed to Lock Slide',text=df['Failed to Lock Slide'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['Slider did not move'],name='Slider did not move',text=df['Slider did not move'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.add_trace(go.Bar(x=df['Date'], y=df['No slide detected'],name='No slide detected',text=df['No slide detected'],textposition='auto',textfont_size=20,hovertext=df['ID']))
fig7.update_layout(barmode='stack', title_text='Frequently occuring error',xaxis_title="Scan Date",yaxis_title="Number of errors",height=800)

df23=pd.read_csv("https://raw.githubusercontent.com/MONSTERharper/extra/main/Cs003_error.csv")
fig77 = go.Figure()
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['No grid found'],name='No grid found',text=df23['No grid found'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['Error during restoration'],name='Error during restoration',text=df23['Error during restoration'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['slide thickness error'],name='slide thickness error',text=df23['slide thickness error'],textposition='auto',textfont_size=20,hovertext=df['ID']))
#fig77.add_trace(go.Bar(x=df['Date'], y=df['Untarring error'],name='untarring error',text=df['untarring error']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['Can not place slide'],name='Can not place slide',text=df23['Can not place slide'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['Snap Miss'],name='Snap Miss',text=df23['Snap Miss'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['Failed to Lock Slide'],name='Failed to Lock Slide',text=df23['Failed to Lock Slide'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['Slider did not move'],name='Slider did not move',text=df23['Slider did not move'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.add_trace(go.Bar(x=df23['Date'], y=df23['No slide detected'],name='No slide detected',text=df23['No slide detected'],textposition='auto',textfont_size=20,hovertext=df23['ID']))
fig77.update_layout(barmode='stack', title_text='Frequently occuring error',xaxis_title="Scan Date",yaxis_title="Number of errors",height=800)

df23=pd.read_csv("https://raw.githubusercontent.com/MONSTERharper/extra/main/Cs003_vis.csv")

fig88 = px.line(x=df23['Date'], y=df23['Positive'],text=df23['Positive'])
fig88.update_traces(textposition='bottom center',name='Positive %', showlegend = True,textfont_size=20)
fig88.update_traces(line_color='darkviolet') 
colors = ['lightblue',] * len(df23) 
colors[len(df23)-1] = '#44bd32'
fig88.add_bar(x=df23['Date'], y=df23['Total Scans'],text=df23['Total Scans'],marker_color=colors,textposition='auto',textfont_size=20,name='Count of scans')
fig88.update_layout(barmode='overlay')
colors = ['blue',] * len(df23)
colors[len(df23)-1] = '#44bd32'
fig88.update_layout(
    title_text='Daily CS003 Report', # title of plot
    xaxis_title_text='Date of Scan CS003', # xaxis label
    yaxis_title_text='Count of Slides Scanned', # yaxis label
    height=700
)


#fig88 for cluster cs003

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

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Introduction Tab',style=tab_style, selected_style=tab_selected_style, children=[
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            #html.Img(src=get_asset_url('/spec2.png'),style={'maxWidth': '100%','maxHeight': '100%','marginLeft': 'auto','marginRight': 'auto'}),
            html.Br(),
            html.Br(),
            html.H1(children='System Performance Analysis',style={
            'textAlign': 'center',
            'color': colors['text']}),
            html.H1(children='\t\t- A snapshot',style={
            'textAlign': 'center',
            'color': colors['text']}),
            html.H1(children='\t\t- For the date :'+str(date.today()- timedelta(days = 1)),style={
            'textAlign': 'center',
            'color': colors['text']})

        ]),
        dcc.Tab(label='Daily reports for S1',style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Graph(
                figure=fig
            ),
            dcc.Graph(
                figure=fig11
            )
        ]),
        dcc.Tab(label='Daily reports for S2',style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Graph(
                figure=fig2
            ),
            dcc.Graph(
                figure=fig12
            )
        ]),
        dcc.Tab(label='Daily reports for S3',style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Graph(
                figure=fig3
            ),
            dcc.Graph(
                figure=fig13
            )
        ]),
        dcc.Tab(label='Daily reports for S4',style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Graph(
                figure=fig4
            ),
            dcc.Graph(
                figure=fig14
            )
        ]),
        dcc.Tab(label='Frequently occuring error',style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Graph(
                figure=fig7
            )]),
        dcc.Tab(label='Cluster CS003',style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Graph(
                figure=fig88
            ),
            dcc.Graph(
                figure=fig77
            )
        ]), 
    ]) 
])


'''
if __name__ == '__main__':
    app.run_server(debug=True,port=9200)
'''
