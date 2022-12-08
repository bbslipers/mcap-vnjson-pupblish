import dash
from dash import html

dash.register_page(__name__, path='/auth')

layout = html.Div(children=[
    html.H1(children='Страница регистрации')
])