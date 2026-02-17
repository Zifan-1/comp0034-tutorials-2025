import streamlit as st
from io import StringIO
import pandas as pd

from src.data.mock_api import get_event_data
from src.utils.line_chart import line_chart


@st.cache_data
# Load data
def load_data():
    """Load paralympics data from mock API into a DataFrame."""
    para_data = get_event_data()
    df = pd.read_json(StringIO(para_data))
    df["start"] = pd.to_datetime(df["start"], dayfirst=True)
    df["end"] = pd.to_datetime(df["end"], dayfirst=True)
    return df


st.title("Paralympics1 data")

df = load_data()

st.dataframe(df)
# Line Chart
chart = line_chart("participants", df)
st.plotly_chart(chart)
