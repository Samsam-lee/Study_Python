import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
background = '#101010'
text = '#FFFFFF'

app.layout = html.Div(style={'backgroundColor':background}, children = [
    html.H1(children = 'Hello', style={'textAlign' : 'center', 'color' : text}),
    dcc.Graph(
        id = '1',
        figure = {
            'data' : [
                {'x' : [1, 2, 3], 'y' : [3, 3, 3], 'type' : 'bar', 'name' : 'A'},
                {'x' : [1, 2, 3], 'y' : [1, 2, 3], 'type' : 'bar', 'name' : 'B'}
            ],
            'layout' : {
                'plot_bgcolor' : background,
                'paper_bgcolor' : background,
                'font' : {'color' : text}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()