from io import StringIO

import pandas as pd
from dash import Dash, dcc, dash_table, html

from src.data.mock_api import get_event_data
from src.utils.line_chart import line_chart


def load_data():
    """Load paralympics event data from mock API into a DataFrame."""
    para_data = get_event_data()

    df = pd.read_json(StringIO(para_data))

    if "start" in df.columns:
        df["start"] = pd.to_datetime(df["start"], dayfirst=True)

    if "end" in df.columns:
        df["end"] = pd.to_datetime(df["end"], dayfirst=True)

    return df


df = load_data()

app = Dash(__name__)

app.layout = [
    html.H1(children="Paralympics data"),
    dash_table.DataTable(
        data=df.to_dict("records"),
        page_size=10,
    ),
    dcc.Graph(
        figure=line_chart("participants", df),
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
