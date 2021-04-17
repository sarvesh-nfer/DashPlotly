import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import numpy as np
import dash_table
from datetime import date
from datetime import timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________BestZ vs thickness_______________________________________________________________________________________________________
'''
__________________________________________________

For yesterday's date
__________________________________________________
'''



merged=pd.read_csv("apps/merged.csv")
#diving scanner wise
#s11=merged[merged['scanner_name']=='S1']
s1=merged[merged['scanner_name']=='H01CBA02P']
s2=merged[merged['scanner_name']=='H01CBA03P']
s3=merged[merged['scanner_name']=='H01CBA06P']
s4=merged[merged['scanner_name']=='H01CBA05P']

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


#fig1.show()

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
#fig2.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")

# Set y-axes titles
fig2.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
fig2.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
fig2.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)


#fig33.show()# Create figure with secondary y-axis
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
#fig3.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")

# Set y-axes titles
fig3.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
fig3.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
fig3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
#fig3.update_layout(hovermode="x")
'''
#fig33.show()# Create figure with secondary y-axis
fig4 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig4.add_trace(
    go.Scatter(x=s4['slide_name'], y=s4['best_z'], name="best-Z",mode = 'lines+markers'),
    secondary_y=False,
)

fig4.add_trace(
    go.Scatter(x=s4['slide_name'], y=s4['slide_thickness'], name="Slide",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
fig4.update_layout(
    title_text="Multi-Axis plot with Best-Z and slide thickness for S3-CS002",width=1800,height=1000
)

# Set x-axis title
fig4.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")

# Set y-axes titles
fig4.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
fig4.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
fig4.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
#fig4.update_layout(hovermode="x")

#fig33.show()

# Create figure with secondary y-axis
fig5 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig5.add_trace(
    go.Scatter(x=s11['slide_name'], y=s11['best_z'], name="best-Z",mode = 'lines+markers'),
    secondary_y=False,
)

fig5.add_trace(
    go.Scatter(x=s11['slide_name'], y=s11['slide_thickness'], name="Slide",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
fig5.update_layout(
    title_text="Multi-Axis plot with Best-Z and slide thickness for S3-CS002",width=1800,height=1000
)

# Set x-axis title
fig5.update_xaxes(title_text="Multi-Axis plot with Best-Z and slide thickness")

# Set y-axes titles
fig5.update_yaxes(title_text="<b>primary</b> Best-Z Values", secondary_y=False)
fig5.update_yaxes(title_text="<b>secondary</b> Slide Thickness values", secondary_y=True)
fig5.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig5.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
fig5.update_layout(hovermode="x")

#fig33.show()
'''
#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________Current plots_______________________________________________________________________________________________________

current=pd.read_csv("apps/current.csv")

S1_2=current[current['scanner_name']=='H01CBA02P']
S2_2=current[current['scanner_name']=='H01CBA03P']
S3_2=current[current['scanner_name']=='H01CBA06P']
S4_2=current[current['scanner_name']=='H01CBA05P']
S1_3=current[current['scanner_name']=='S1']

'''
s11=s11[s11['.load_identifier']==np.sort(s11['load_identifier'])[-1]]
s1=s1[s1['load_identifier']==np.sort(s1['load_identifier'])[-1]]
s2=s2[s2['load_identifier']==np.sort(s2['load_identifier'])[-1]]
s3=s3[s3['load_identifier']==np.sort(s3['load_identifier'])[-1]]
'''
#S1_3=S1_3[S1_3['load_identifier']==np.sort(S1_3['load_identifier'])[-1]]
S1_2=S1_2[S1_2['load_identifier']==np.sort(S1_2['load_identifier'])[-1]]
S2_2=S2_2[S2_2['load_identifier']==np.sort(S2_2['load_identifier'])[-1]]
#S3_2=S3_2[S3_2['load_identifier']==np.sort(S3_2['load_identifier'])[-1]]
#S4_2=S4_2[S4_2['load_identifier']==np.sort(S4_2['load_identifier'])[-1]]

S1_2=S1_2.reset_index(drop=True)
S2_2=S2_2.reset_index(drop=True)
S3_2=S3_2.reset_index(drop=True)
S4_2=S4_2.reset_index(drop=True)
S1_3=S1_3.reset_index(drop=True)

################
#plot
##############


fig11 = px.scatter(S1_2, x="slide_name", y="first_initial_current",hover_name='first_read_angle',hover_data=['first_status'],
labels={
"first_initial_current": "Current Readings",
"slide_name": "Slide_name",
}
) 
fig11.add_scatter(x=S1_2['slide_name'], y=S1_2['first_final_current'],mode="markers+lines",hovertext=S1_2['first_final_current'],name="final_current",hoverinfo='text')
fig11.add_scatter(x=S1_2['slide_name'], y=S1_2['first_current_diff'],mode="markers+lines",hovertext=S1_2['first_current_diff'],name="difference_current",hoverinfo='text')

fig11.update_traces(mode="markers+lines",showlegend=True,
name='first_initial_current',
marker=dict(size=5,
line=dict(width=1,
color='DarkSlateGrey')),
selector=dict(mode='markers'))
fig11.update_layout(
title="Overall first Iteration Current Reading",
font=dict(
family="Courier New, monospace",
size=16,
color="RebeccaPurple"
),
legend=dict(
traceorder="reversed",
title_font_family="Times New Roman",
font=dict(
family="Courier",
size=16,
color="black"
),
bgcolor="LightSteelBlue",
bordercolor="Black",
borderwidth=2
)
)
fig11.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig11.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
fig11.update_layout(hovermode="x")
#fig11.show()

#######################################################################################################

fig22 = px.scatter(S2_2, x="slide_name", y="first_initial_current",hover_name='first_read_angle',hover_data=['first_status'],
labels={
"first_initial_current": "Current Readings",
"slide_name": "Slide_name",
}
) 
fig22.add_scatter(x=S2_2['slide_name'], y=S2_2['first_final_current'],mode="markers+lines",hovertext=S2_2['first_final_current'],name="final_current",hoverinfo='text')
fig22.add_scatter(x=S2_2['slide_name'], y=S2_2['first_current_diff'],mode="markers+lines",hovertext=S2_2['first_current_diff'],name="difference_current",hoverinfo='text')

fig22.update_traces(mode="markers+lines",showlegend=True,
name='first_initial_current',
marker=dict(size=5,
line=dict(width=1,
color='DarkSlateGrey')),
selector=dict(mode='markers'))
fig22.update_layout(
title="Overall first Iteration Current Reading",
font=dict(
family="Courier New, monospace",
size=16,
color="RebeccaPurple"
),
legend=dict(
traceorder="reversed",
title_font_family="Times New Roman",
font=dict(
family="Courier",
size=16,
color="black"
),
bgcolor="LightSteelBlue",
bordercolor="Black",
borderwidth=2
)
)
fig22.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig22.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
fig22.update_layout(hovermode="x")
#fig22.show()

#####################################################################################################################

fig33 = px.scatter(S3_2, x="slide_name", y="first_initial_current",hover_name='first_read_angle',hover_data=['first_status'],
labels={
"first_initial_current": "Current Readings",
"slide_name": "Slide_name",
}
) 
fig33.add_scatter(x=S3_2['slide_name'], y=S3_2['first_final_current'],mode="markers+lines",hovertext=S3_2['first_final_current'],name="final_current",hoverinfo='text')
fig33.add_scatter(x=S3_2['slide_name'], y=S3_2['first_current_diff'],mode="markers+lines",hovertext=S3_2['first_current_diff'],name="difference_current",hoverinfo='text')

fig33.update_traces(mode="markers+lines",showlegend=True,
name='first_initial_current',
marker=dict(size=5,
line=dict(width=1,
color='DarkSlateGrey')),
selector=dict(mode='markers'))
fig33.update_layout(
title="Overall first Iteration Current Reading",
font=dict(
family="Courier New, monospace",
size=16,
color="RebeccaPurple"
),
legend=dict(
traceorder="reversed",
title_font_family="Times New Roman",
font=dict(
family="Courier",
size=16,
color="black"
),
bgcolor="LightSteelBlue",
bordercolor="Black",
borderwidth=2
)
)
fig33.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig33.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
fig33.update_layout(hovermode="x")
#fig33.show()

#########################################################################################################################################
'''
fig44 = px.scatter(S4_2, x="slide_name", y="first_initial_current",hover_name='first_read_angle',hover_data=['first_status'],
labels={
"first_initial_current": "Current Readings",
"slide_name": "Slide_name",
}
) 
fig44.add_scatter(x=S4_2['slide_name'], y=S4_2['first_final_current'],mode="markers+lines",hovertext=S4_2['first_final_current'],name="final_current",hoverinfo='text')
fig44.add_scatter(x=S4_2['slide_name'], y=S4_2['first_current_diff'],mode="markers+lines",hovertext=S4_2['first_current_diff'],name="difference_current",hoverinfo='text')

fig44.update_traces(mode="markers+lines",showlegend=True,
name='first_initial_current',
marker=dict(size=5,
line=dict(width=1,
color='DarkSlateGrey')),
selector=dict(mode='markers'))
fig44.update_layout(
title="Overall first Iteration Current Reading",
font=dict(
family="Courier New, monospace",
size=16,
color="RebeccaPurple"
),
legend=dict(
traceorder="reversed",
title_font_family="Times New Roman",
font=dict(
family="Courier",
size=16,
color="black"
),
bgcolor="LightSteelBlue",
bordercolor="Black",
borderwidth=2
)
)
fig44.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig44.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
fig44.update_layout(hovermode="x")
#fig44.show()

####################################################################################################


fig55 = px.scatter(S1_3, x="slide_name", y="first_initial_current",hover_name='first_read_angle',hover_data=['first_status'],
labels={
"first_initial_current": "Current Readings",
"slide_name": "Slide_name",
}
) 
fig55.add_scatter(x=S1_3['slide_name'], y=S1_3['first_final_current'],mode="markers+lines",hovertext=S1_3['first_final_current'],name="final_current",hoverinfo='text')
fig55.add_scatter(x=S1_3['slide_name'], y=S1_3['first_current_diff'],mode="markers+lines",hovertext=S1_3['first_current_diff'],name="difference_current",hoverinfo='text')

fig55.update_traces(mode="markers+lines",showlegend=True,
name='first_initial_current',
marker=dict(size=5,
line=dict(width=1,
color='DarkSlateGrey')),
selector=dict(mode='markers'))
fig55.update_layout(
title="Overall first Iteration Current Reading",
font=dict(
family="Courier New, monospace",
size=16,
color="RebeccaPurple"
),
legend=dict(
traceorder="reversed",
title_font_family="Times New Roman",
font=dict(
family="Courier",
size=16,
color="black"
),
bgcolor="LightSteelBlue",
bordercolor="Black",
borderwidth=2
)
)
fig55.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
fig55.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
fig55.update_layout(hovermode="x")
#fig55.show()

'''


################################################################################################################

#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________angle permissible plots_______________________________________________________________________________________________________

angle=pd.read_csv("apps/angleoffset.csv")
angle=angle.dropna(subset=['load_identifier'])
a1_2=angle[angle['scanner_name']=='H01CBA02P']
a2_2=angle[angle['scanner_name']=='H01CBA03P']
a3_2=angle[angle['scanner_name']=='H01CBA06P']
a4_2=angle[angle['scanner_name']=='H01CBA05P']
a1_3=angle[angle['scanner_name']=='S1']

#a1_3=a1_3[a1_3['load_identifier']==np.sort(a1_3['load_identifier'])[-1]]
a1_2=a1_2[a1_2['load_identifier']==np.sort(a1_2['load_identifier'])[-1]]
a2_2=a2_2[a2_2['load_identifier']==np.sort(a2_2['load_identifier'])[-1]]
a3_2=a3_2[a3_2['load_identifier']==np.sort(a3_2['load_identifier'])[-1]]
#a4_2=a4_2[a4_2['load_identifier']==np.sort(a4_2['load_identifier'])[-1]]

a1_2=a1_2.reset_index(drop=True)
a2_2=a2_2.reset_index(drop=True)
a3_2=a3_2.reset_index(drop=True)
a4_2=a4_2.reset_index(drop=True)
a1_3=a1_3.reset_index(drop=True)
#######################################################################


# Create figure with secondary y-axis
figa1 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
figa1.add_trace(
    go.Scatter(x=a1_2['slide_name'], y=a1_2['permissible_angle'], name="permissible_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa1.add_trace(
    go.Scatter(x=a1_2['slide_name'], y=a1_2['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa1.add_trace(
    go.Scatter(x=a1_2['slide_name'], y=a1_2['slide_width_um'], name="slide_width",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
figa1.update_layout(
    title_text="Multi-Axis plot for Permissible_angle & slide_width(um)",width=1600,height=800,
        font=dict(
        family="Courier New, monospace",
        size=16,
        color="RebeccaPurple"
    ),
)
# Set x-axis title
figa1.update_xaxes(title_text="Slide_name")
# Set y-axes titles
figa1.update_yaxes(title_text="<b>secondary</b> Slide_width(um) ", secondary_y=True)
figa1.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
figa1.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
figa1.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figa1.update_layout(hovermode="x")
#figa1.show()


# Create figure with secondary y-axis
figa2 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
figa2.add_trace(
    go.Scatter(x=a2_2['slide_name'], y=a2_2['permissible_angle'], name="permissible_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa2.add_trace(
    go.Scatter(x=a2_2['slide_name'], y=a2_2['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa2.add_trace(
    go.Scatter(x=a2_2['slide_name'], y=a2_2['slide_width_um'], name="slide_width",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
figa2.update_layout(
    title_text="Multi-Axis plot for Permissible_angle & slide_width(um)",width=1600,height=800,
        font=dict(
        family="Courier New, monospace",
        size=16,
        color="RebeccaPurple"
    ),
)
# Set x-axis title
figa2.update_xaxes(title_text="Slide_name")
# Set y-axes titles
figa2.update_yaxes(title_text="<b>secondary</b> Slide_width(um) ", secondary_y=True)
figa2.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
figa2.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
figa2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figa2.update_layout(hovermode="x")
#figa1.show()

# Create figure with secondary y-axis
figa3 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
figa3.add_trace(
    go.Scatter(x=a3_2['slide_name'], y=a3_2['permissible_angle'], name="permissible_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa3.add_trace(
    go.Scatter(x=a3_2['slide_name'], y=a3_2['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa3.add_trace(
    go.Scatter(x=a3_2['slide_name'], y=a3_2['slide_width_um'], name="slide_width",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
figa3.update_layout(
    title_text="Multi-Axis plot for Permissible_angle & slide_width(um)",width=1600,height=800,
        font=dict(
        family="Courier New, monospace",
        size=16,
        color="RebeccaPurple"
    ),
)
# Set x-axis title
figa3.update_xaxes(title_text="Slide_name")
# Set y-axes titles
figa3.update_yaxes(title_text="<b>secondary</b> Slide_width(um) ", secondary_y=True)
figa3.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
figa3.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
figa3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figa3.update_layout(hovermode="x")
#figa1.show()

# Create figure with secondary y-axis
figa4 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
figa4.add_trace(
    go.Scatter(x=a4_2['slide_name'], y=a4_2['permissible_angle'], name="permissible_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa4.add_trace(
    go.Scatter(x=a4_2['slide_name'], y=a4_2['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa4.add_trace(
    go.Scatter(x=a4_2['slide_name'], y=a4_2['slide_width_um'], name="slide_width",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
figa4.update_layout(
    title_text="Multi-Axis plot for Permissible_angle & slide_width(um)",width=1600,height=800,
        font=dict(
        family="Courier New, monospace",
        size=16,
        color="RebeccaPurple"
    ),
)
# Set x-axis title
figa4.update_xaxes(title_text="Slide_name")
# Set y-axes titles
figa4.update_yaxes(title_text="<b>secondary</b> Slide_width(um) ", secondary_y=True)
figa4.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
figa4.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
figa4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figa4.update_layout(hovermode="x")
#figa1.show()

# Create figure with secondary y-axis
figa5 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
figa5.add_trace(
    go.Scatter(x=a1_3['slide_name'], y=a1_3['permissible_angle'], name="permissible_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa5.add_trace(
    go.Scatter(x=a1_3['slide_name'], y=a1_3['actual_angle'], name="Actual_angle",mode = 'lines+markers'),
    secondary_y=False,
)
figa5.add_trace(
    go.Scatter(x=a1_3['slide_name'], y=a1_3['slide_width_um'], name="slide_width",mode = 'lines+markers'),
    secondary_y=True,
)

# Add figure title
figa5.update_layout(
    title_text="Multi-Axis plot for Permissible_angle & slide_width(um)",width=1600,height=800,
        font=dict(
        family="Courier New, monospace",
        size=16,
        color="RebeccaPurple"
    ),
)
# Set x-axis title
figa5.update_xaxes(title_text="Slide_name")
# Set y-axes titles
figa5.update_yaxes(title_text="<b>secondary</b> Slide_width(um) ", secondary_y=True)
figa5.update_yaxes(title_text="<b>primary</b> Permissible_angle & Actual_angle", secondary_y=False)
figa5.update_xaxes(showspikes=True, spikecolor="royalblue", spikemode="across",spikethickness=1)
figa5.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figa5.update_layout(hovermode="x")
#figa1.show()


#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________Offset plots_______________________________________________________________________________________________________

offset=pd.read_csv("apps/angleoffset.csv")
offset=offset.dropna(subset=['load_identifier'])
offset['row_col']=offset['row_index'].map(str)+','+offset['col_index'].map(str)

o1_2=offset[offset['scanner_name']=='H01CBA02P']
o2_2=offset[offset['scanner_name']=='H01CBA03P']
o3_2=offset[offset['scanner_name']=='H01CBA06P']
o4_2=offset[offset['scanner_name']=='H01CBA05P']
o1_3=offset[offset['scanner_name']=='S1']


#o1_3=o1_3[o1_3['load_identifier']==np.sort(o1_3['load_identifier'])[-1]]
o1_2=o1_2[o1_2['load_identifier']==np.sort(o1_2['load_identifier'])[-1]]
o2_2=o2_2[o2_2['load_identifier']==np.sort(o2_2['load_identifier'])[-1]]
o3_2=o3_2[o3_2['load_identifier']==np.sort(o3_2['load_identifier'])[-1]]
#o4_2=o4_2[o4_2['load_identifier']==np.sort(o4_2['load_identifier'])[-1]]

o1_2=o1_2.reset_index(drop=True)
o2_2=o2_2.reset_index(drop=True)
o3_2=o3_2.reset_index(drop=True)
o4_2=o4_2.reset_index(drop=True)
o1_3=o1_3.reset_index(drop=True)


figo1 = px.scatter(o1_2, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",hover_name="row_col",
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
#figo1.show()


#######################################################

figo2 = px.scatter(o2_2, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",hover_name="row_col",
                 labels={
                     "offset_pos_x_um": "X- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo2.update_traces(mode="markers",                 
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

figo2.add_vrect(x0=-3500, x1=3500)
figo2.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo2.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo2.update_layout(width=1000,height=1100,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),
                 )
figo2.update_xaxes(range=[-4000, 4000])
#figo2.show()
###########################################################

figo3 = px.scatter(o3_2, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",hover_name="row_col",
                 labels={
                     "offset_pos_x_um": "X- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo3.update_traces(mode="markers",                 
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

figo3.add_vrect(x0=-3500, x1=3500)
figo3.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo3.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo3.update_layout(width=1000,height=1100,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),
                 )
figo3.update_xaxes(range=[-4000, 4000])
#figo3.show()

###########################################################
'''
figo4 = px.scatter(o4_2, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",hover_name="row_col",
                 labels={
                     "offset_pos_x_um": "X- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo4.update_traces(mode="markers",                 
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

figo4.add_vrect(x0=-3500, x1=3500)
figo4.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo4.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo4.update_layout(width=1000,height=1100,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),
                 )
figo4.update_xaxes(range=[-4000, 4000])
#figo4.show()
'''
###########################################################
"""
figo5 = px.scatter(o1_3, y="slide_name", x="offset_pos_x_um",title="X-Offset Deviation",hover_name="row_col",
                 labels={
                     ".offset_pos_x_um": "X- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo5.update_traces(mode="markers",                 
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

figo5.add_vrect(x0=-3500, x1=3500)
figo5.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo5.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo5.update_layout(width=1000,height=1100,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),
                 )
figo5.update_xaxes(range=[-4000, 4000])
#figo5.show()
"""


figo11 = px.scatter(o1_2, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo11.update_traces(mode="markers",
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
figo11.add_hrect(y0=0, y1=5000)
figo11.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo11.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo11.update_layout(width=1200,height=600,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),)
#figo11.update_layout(hovermode="y")
figo11.update_yaxes(range=[-500, 6000])
#fig.show()

###################################################################
figo22 = px.scatter(o2_2, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo22.update_traces(mode="markers",
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
figo22.add_hrect(y0=0, y1=5000)
figo22.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo22.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo22.update_layout(width=1200,height=600,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),)
#figo22.update_layout(hovermode="y")
figo22.update_yaxes(range=[-500, 6000])
#fig.show()

###################################################################
figo33 = px.scatter(o3_2, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo33.update_traces(mode="markers",
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
figo33.add_hrect(y0=0, y1=5000)
figo33.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo33.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo33.update_layout(width=1200,height=600,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),)
#figo33.update_layout(hovermode="y")
figo33.update_yaxes(range=[-500, 6000])
#fig.show()

###################################################################
'''
figo44 = px.scatter(o4_2, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo44.update_traces(mode="markers",
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
figo44.add_hrect(y0=0, y1=5000)
figo44.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo44.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo44.update_layout(width=1200,height=600,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),)
#figo44.update_layout(hovermode="y")
figo44.update_yaxes(range=[-500, 6000])
#fig.show()

###################################################################

figo55 = px.scatter(o1_3, x="slide_name", y="offset_pos_y_um",title="Y-Offset Deviation",hover_name="row_col",
                labels={
                     "y_offset_um": "Y- offset (um)",
                     "slide_name": "Slide_name",
                 },)
figo55.update_traces(mode="markers",
                  marker=dict(size=5,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
figo55.add_hrect(y0=0, y1=5000)
figo55.update_xaxes(showspikes=True, spikecolor="yellow", spikemode="across",spikethickness=1)
figo55.update_yaxes(showspikes=True, spikecolor="royalblue", spikethickness=1)
figo55.update_layout(width=1200,height=600,
                  font=dict(
                      family="Courier New, monospace",
                      size=16,
                      color="RebeccaPurple"
                  ),)
#figo55.update_layout(hovermode="y")
figo55.update_yaxes(range=[-500, 6000])
#figo55.show()
'''
#_________________________________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________Centering and intensity_______________________________________________________________________________________________________

post2=pd.read_csv("apps/post2.csv")
post3=pd.read_csv("apps/post3.csv")
post4=pd.read_csv("apps/post4.csv")


figp1 = go.Figure()
figp1.add_trace(go.Scatter(y=post2['mean_red_intensity'],
                            mode='lines',
                            name='mean_red_intensity',line=dict(color='red')))
figp1.add_trace(go.Scatter(y=post2['mean_blue_intensity'],
                            mode='lines',
                            name='mean_blue_intensity',line=dict(color='blue')))
figp1.add_trace(go.Scatter(y=post2['mean_green_intensity'],
                            mode='lines', name='mean_green_intensity',line=dict(color='green')))
figp1.update_yaxes(range=[150, 260])
figp1.update_layout(title="Average Intensity across the z stack"+" "+post2['_source.data.time_stamp'][1],
                    xaxis_title="Z Steps",
                    yaxis_title="Average Intensity",
                    legend_title="Intensity",
                    font=dict(
                        family="Courier New, monospace",
                        size=16,
                        color="RebeccaPurple")
                    )
#fig.update_xaxes()
figp1.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp1.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson')

figp11 = go.Figure()
x=[968]
y=[608]
figp11.add_trace(go.Scatter(x=post2['centring_coordinate_x'],y=post2['centring_coordinate_y'],
                          mode='markers',
                          name='Dispersion',
                         ))
figp11.add_trace(go.Scatter(x=x,y=y,
                          mode='markers',
                          name='Centre',
                         ))
figp11.update_yaxes(range=[0,1216])
figp11.update_xaxes(range=[0,1936])
figp11.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp11.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp11.update_layout(title="Centering for scanner"+" " +post2['_source.data.scanner_name'][1]+" "+post2['_source.data.time_stamp'][1],
                   xaxis_title="Width of the AOI",
                   yaxis_title="Height of the AOI",
                   font=dict(
                       family="Courier New, monospace",
                       size=16,
                       color="RebeccaPurple")
                  )
figp11.add_shape(type="rect",
    xref="x", yref="y",
    x0=768, y0=408, x1=1168, y1=808,
    line_color="red",
)
  
                  
figp2 = go.Figure()
figp2.add_trace(go.Scatter(y=post3['mean_red_intensity'],
                            mode='lines',
                            name='mean_red_intensity',line=dict(color='red')))
figp2.add_trace(go.Scatter(y=post3['mean_blue_intensity'],
                            mode='lines',
                            name='mean_blue_intensity',line=dict(color='blue')))
figp2.add_trace(go.Scatter(y=post3['mean_green_intensity'],
                            mode='lines', name='mean_green_intensity',line=dict(color='green')))
figp2.update_yaxes(range=[150, 260])
figp2.update_layout(title="Average Intensity across the z stack"+" "+post3['_source.data.time_stamp'][1],
                    xaxis_title="Z Steps",
                    yaxis_title="Average Intensity",
                    legend_title="Intensity",
                    font=dict(
                        family="Courier New, monospace",
                        size=16,
                        color="RebeccaPurple")
                    )
#fig.update_xaxes()
figp2.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp2.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson')


figp22 = go.Figure()
x=[968]
y=[608]
figp22.add_trace(go.Scatter(x=post3['centring_coordinate_x'],y=post3['centring_coordinate_y'],
                          mode='markers',
                          name='Dispersion',
                         ))
figp22.add_trace(go.Scatter(x=x,y=y,
                          mode='markers',
                          name='Centre',
                         ))
figp22.update_yaxes(range=[0,1216])
figp22.update_xaxes(range=[0,1936])
figp22.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp22.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp22.update_layout(title="Centering for scanner"+" " +post3['_source.data.scanner_name'][1]+" "+post3['_source.data.time_stamp'][1],
                   xaxis_title="Width of the AOI",
                   yaxis_title="Height of the AOI",
                   font=dict(
                       family="Courier New, monospace",
                       size=16,
                       color="RebeccaPurple")
                  )
figp22.add_shape(type="rect",
    xref="x", yref="y",
    x0=768, y0=408, x1=1168, y1=808,
    line_color="red",
)
                    
figp3 = go.Figure()
figp3.add_trace(go.Scatter(y=post4['mean_red_intensity'],
                            mode='lines',
                            name='mean_red_intensity',line=dict(color='red')))
figp3.add_trace(go.Scatter(y=post4['mean_blue_intensity'],
                            mode='lines',
                            name='mean_blue_intensity',line=dict(color='blue')))
figp3.add_trace(go.Scatter(y=post4['mean_green_intensity'],
                            mode='lines', name='mean_green_intensity',line=dict(color='green')))
figp3.update_yaxes(range=[150, 260])
figp3.update_layout(title="Average Intensity across the z stack"+" "+post4['_source.data.time_stamp'][1],
                    xaxis_title="Z Steps",
                    yaxis_title="Average Intensity",
                    legend_title="Intensity",
                    font=dict(
                        family="Courier New, monospace",
                        size=16,
                        color="RebeccaPurple")
                    )
#fig.update_xaxes()
figp3.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp3.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson')


figp33 = go.Figure()
x=[968]
y=[608]
figp33.add_trace(go.Scatter(x=post4['centring_coordinate_x'],y=post4['centring_coordinate_y'],
                          mode='markers',
                          name='Dispersion',
                         ))
figp33.add_trace(go.Scatter(x=x,y=y,
                          mode='markers',
                          name='Centre',
                         ))
figp33.update_yaxes(range=[0,1216])
figp33.update_xaxes(range=[0,1936])
figp33.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp33.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson')
figp33.update_layout(title="Centering for scanner"+" " +post4['_source.data.scanner_name'][1]+" "+post4['_source.data.time_stamp'][1],
                   xaxis_title="Width of the AOI",
                   yaxis_title="Height of the AOI",
                   font=dict(
                       family="Courier New, monospace",
                       size=16,
                       color="RebeccaPurple")
                  )
figp33.add_shape(type="rect",
    xref="x", yref="y",
    x0=768, y0=408, x1=1168, y1=808,
    line_color="red",
)
                    
#____________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________AOI'_______________________________________________________________________________________________________


#df=pd.read_csv("C:/Users/sarve/OneDrive/Documents/Work/daily/apps/best_idx.csv")


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
            html.H1(children='Components status',style={
            'textAlign': 'center',
            'color': colors['text']}),
            html.H1(children='\t\t- Last updated for :'+str(date.today()- timedelta(days = 1)),style={
            'textAlign': 'center',
            'color': colors['text']})

        ]),
        dcc.Tab(label='Station 1',style=tab_style, selected_style=tab_selected_style, children=[
        html.Br(),
        html.H1(children='Current Difference'),
        dcc.Graph(
            figure=fig11
        ),
        html.Br(),
        html.H1(children='Angle permissible'),
        dcc.Graph(
            figure=figa1
        ),
                    html.Br(),
        html.H1(children='X-offset deviation'),
        dcc.Graph(
            figure=figo1
        ),
                    html.Br(),
        html.H1(children='Y-offset deviation'),
        dcc.Graph(
            figure=figo11
        ),
                    html.Br(),
        html.H1(children='RGB intensity'),
        dcc.Graph(
            figure=figp1
        ),
                    html.Br(),
        html.H1(children='Centering Info'),
        dcc.Graph(
            figure=figp11
        ),
                    html.Br(),
        html.H1(children='Best Z Vs Slide Thickness'),
        dcc.Graph(
            figure=fig1
        ),
    ]),
    dcc.Tab(label='Station 2',style=tab_style, selected_style=tab_selected_style, children=[
        html.Br(),
        html.H1(children='Current Difference'),
        dcc.Graph(
            figure=fig22
        ),
        html.Br(),
        html.H1(children='Angle permissible'),
        dcc.Graph(
            figure=figa2
        ),
                    html.Br(),
        html.H1(children='X-offset deviation'),
        dcc.Graph(
            figure=figo2
        ),
                    html.Br(),
        html.H1(children='Y-offset deviation'),
        dcc.Graph(
            figure=figo22
        ),
                    html.Br(),
        html.H1(children='RGB intensity'),
        dcc.Graph(
            figure=figp2
        ),
                    html.Br(),
        html.H1(children='Centering Info'),
        dcc.Graph(
            figure=figp22
        ),
        html.Br(),
        html.H1(children='Best Z Vs Slide Thickness'),
        dcc.Graph(
            figure=fig2
        ),
    ]),
    dcc.Tab(label='Station 3',style=tab_style, selected_style=tab_selected_style, children=[
        html.Br(),
        html.H1(children='Current Difference'),
        dcc.Graph(
            figure=fig33
        ),
        html.Br(),
        html.H1(children='Angle permissible'),
        dcc.Graph(
            figure=figa3
        ),
                    html.Br(),
        html.H1(children='X-offset deviation'),
        dcc.Graph(
            figure=figo3
        ),
                    html.Br(),
        html.H1(children='Y-offset deviation'),
        dcc.Graph(
            figure=figo33
        ),
                    html.Br(),
        html.H1(children='RGB intensity'),
        dcc.Graph(
            figure=figp3
        ),
                    html.Br(),
        html.H1(children='Centering Info'),
        dcc.Graph(
            figure=figp33
        ),
                    html.Br(),
        html.H1(children='Best Z Vs Slide Thickness'),
        dcc.Graph(
            figure=fig3
        )
    ]),
]) 
])


'''
if __name__ == '__main__':
    app.run_server(debug=True,port=8700)
'''
