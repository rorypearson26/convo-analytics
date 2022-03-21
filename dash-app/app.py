# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

from pre_processing.main_data import RawData, ProcessedData

app = Dash(__name__)

raw = RawData("murphys_clan_new.txt", alias_dict={"+44 7964 738500": "Mum"})
processed = ProcessedData(raw)
df = processed.df
df_time = df.groupby(["sender", df["datetime"].dt.date]).size()
df_time = df_time.unstack("sender").replace(np.nan, 0)
idx = pd.date_range(df_time.index.min(), df_time.index.max())
df_time = df_time.reindex(idx, fill_value=0)
df_time = df_time.rolling(60).mean()
# df_time.plot.line(figsize=(9, 7))

fig = px.line(df_time, x=df_time.index, y=df_time.columns)

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for your data.
    """
        ),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
