import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    # `dash_html_components`が提供するクラスは`childlen`属性を有している。
    # `childlen`属性を慣例的に最初の属性にしている。
    html.H1(children='Hello Dash'),

    html.Div(children='Dash: A web application framework for Python.'),

    # `dash_core_components`が`plotly`に従う機能を提供する。
    # HTMLではSVG要素として表現される。
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)