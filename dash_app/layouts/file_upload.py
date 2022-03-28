from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import pandas as pd

from pre_processing.main_data import RawData, ProcessedData

upload_html = html.Div(
    [
        dcc.Upload(
            ["Drag and Drop or ", html.A("Select a File")],
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
            },
        ),
    ]
)


# alias_dict = {
#     "+44 7964 738500": "Mum",
#     "Rory Pearson": "Rory",
#     "Calum Pearson": "Calum",
# }
# raw = RawData("murphys_clan_new.txt", alias_dict=alias_dict)
# processed = ProcessedData(raw)
# df = processed.df
# df_time = df.groupby(["sender", df["datetime"].dt.date]).size()
# df_time = df_time.unstack("sender").replace(np.nan, 0)
# idx = pd.date_range(df_time.index.min(), df_time.index.max())
# df_time = df_time.reindex(idx, fill_value=0)
# df_time = df_time.rolling(60).mean()
