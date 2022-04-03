from datetime import datetime
import base64
import io

from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import pandas as pd

from dash_app.main_dash import app
from pre_processing.main_data import RawData, ProcessedData

upload_html = html.Div(
    [
        dcc.Upload(
            id="upload-file",
            children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
        ),
        html.Div(id="output-file-upload"),
    ]
)


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "txt" in filename:
            # Assume that the user uploaded a What'sApp text export
            raw_text = io.StringIO(decoded.decode("utf-8"))
            raw = RawData(raw_text)
            processed = ProcessedData(raw)
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    df = processed.df.astype(str)

    return html.Div(
        [
            html.H5(filename),
            html.H6(datetime.fromtimestamp(date)),
            dash_table.DataTable(
                df.sender.value_counts().to_dict("records"),
            ),
            # html.Hr(),  # horizontal line
            # # For debugging, display the raw contents provided by the web browser
            # html.Div('Raw Content'),
            # html.Pre(contents[0:200] + '...', style={
            #     'whiteSpace': 'pre-wrap',
            #     'wordBreak': 'break-all'
            # })
        ]
    )


@app.callback(
    Output("output-file-upload", "children"),
    Input("upload-file", "contents"),
    State("upload-file", "filename"),
    State("upload-file", "last_modified"),
)
def update_output(contents, name, date):
    if contents is not None:
        children = parse_contents(contents, name, date)
        return children


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
