# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

from pre_processing.main_data import RawData, ProcessedData
from dash_app.plots.frequency import get_layout

app = Dash(__name__)
alias_dict = {
    "+44 7964 738500": "Mum",
    "Rory Pearson": "Rory",
    "Calum Pearson": "Calum",
}
raw = RawData("murphys_clan_new.txt", alias_dict=alias_dict)
processed = ProcessedData(raw)
df = processed.df
df_time = df.groupby(["sender", df["datetime"].dt.date]).size()
df_time = df_time.unstack("sender").replace(np.nan, 0)
idx = pd.date_range(df_time.index.min(), df_time.index.max())
df_time = df_time.reindex(idx, fill_value=0)
df_time = df_time.rolling(60).mean()

fig = get_layout(df_time)

app.layout = html.Div(
    children=[
        html.H1(children="WhatsApp Analysis"),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
