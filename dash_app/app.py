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
# df_time.plot.line(figsize=(9, 7))

fig = get_layout(df_time)
# df_24 = df.groupby(["sender", "hour"]).size().reset_index(name="prod_count")
# s = df.sender.value_counts()
# df_24["prod_count"] = df_24["prod_count"].div(df_24["sender"].map(s))
# grp_24 = df_24.groupby(["sender", "hour"]).sum()
# df_24 = grp_24.unstack("sender")
# df_24.replace(np.nan, 0, inplace=True)
# df_24.plot(kind="line", figsize=(9, 7))

app.layout = html.Div(
    children=[
        html.H1(children="WhatsApp Analysis"),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
