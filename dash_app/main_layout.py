from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

# from dash_app.layouts.plot_msg_frequency import get_layout
# from dash_app.main_dash import app
from dash_app.layouts.file_upload import upload_html


# fig = get_layout(df_time)


def create_main_layout():
    # main_layout = html.Div(
    #     [
    #         html.Div(
    #             dbc.Row(html.H1("WhatsApp Analysis")),
    #             dbc.Row([dbc.Col(html.Span(upload_html), width=6)]),
    #         ),
    #     ]
    # )
    main_layout = html.Div(
        [
            dbc.Row(dbc.Col(html.H1("WhatsApp Analysis"))),
            dbc.Row(
                [
                    dbc.Col(html.Div(upload_html)),
                    dbc.Col(html.Div("One of three columns")),
                    dbc.Col(html.Div("One of three columns")),
                ]
            ),
        ]
    )
    return main_layout
