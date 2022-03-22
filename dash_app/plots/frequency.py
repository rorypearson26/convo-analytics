from dash import Dash, html, dcc
import plotly.express as px


def get_layout(df_time):
    fig = px.line(df_time, x=df_time.index, y=df_time.columns)
    fig.update_xaxes(
        rangeslider_visible=True,
        type="date",
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
    )

    return fig
