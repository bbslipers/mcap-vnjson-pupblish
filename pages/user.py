import dash
from dash import html

dash.register_page(__name__, path_template="/user/<user_id>")

def layout(user_id=None):
    return html.Div(
        f"ID пользователя: {user_id}"
    )