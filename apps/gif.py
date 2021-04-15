#acquisition 
import dash_gif_component as gif
import dash
import dash_html_components as html
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    gif.GifPlayer(
        gif='https://media.giphy.com/media/kfR5iyQgmq7PoiFTAf/giphy.gif',
        still='https://media.giphy.com/media/kfR5iyQgmq7PoiFTAf/giphy.gif',autoplay=True
    ),


])
'''
if __name__ == '__main__':
    app.run_server(debug=True)
'''
