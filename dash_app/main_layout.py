from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

# from dash_app.layouts.plot_msg_frequency import get_layout
# from dash_app.main_dash import app
from dash_app.layouts.file_upload import upload_html


# fig = get_layout(df_time)


def create_main_layout():
    main_layout = html.Div(
        children=[
            html.H1(children="WhatsApp Analysis"),
            upload_html,
        ]
    )
    return main_layout
