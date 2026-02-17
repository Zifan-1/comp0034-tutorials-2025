import pandas as pd
import plotly.express as px
import requests


API_ALL_URL = "http://127.0.0.1:8000/all"


def get_api_data(url):
    """
    Get JSON data from the mock API and return a DataFrame.

    Args:
        url (str): API endpoint URL.

    Returns:
        pd.DataFrame: Data from the API.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)


def line_chart(feature):
    """
    Create a line chart over time for a selected feature.

    Args:
        feature (str): One of "sports", "participants", "events", "countries".

    Returns:
        plotly.graph_objs._figure.Figure: Line chart figure.
    """
    valid = ["sports", "participants", "events", "countries"]
    if feature not in valid:
        raise ValueError(f"feature must be one of {valid}")

    df = get_api_data(API_ALL_URL)

    chart_df = df[["event_type", "year", feature]].copy()

    fig = px.line(
        chart_df,
        x="year",
        y=feature,
        color="event_type",
        title=f"How has the number of {feature} changed over time?",
        labels={"year": "Year", feature: ""},
        template="simple_white",
    )
    return fig


def bar_chart(event_type):
    """
    Create a stacked bar chart showing male/female ratio for one event type.

    Args:
        event_type (str): "Winter" or "Summer".

    Returns:
        plotly.graph_objs._figure.Figure: Stacked bar chart figure.
    """
    df = get_api_data(API_ALL_URL)

    needed = [
        "event_type",
        "year",
        "place_name",
        "participants_m",
        "participants_f",
        "participants",
    ]

    df_plot = df[needed].copy()
    df_plot = df_plot.dropna(subset=["participants_m", "participants_f"])
    df_plot = df_plot.query("event_type == @event_type")

    df_plot["Male"] = pd.NA
    df_plot["Female"] = pd.NA

    non_zero = df_plot["participants"] != 0
    df_plot.loc[non_zero, "Male"] = (
        df_plot.loc[non_zero, "participants_m"]
        / df_plot.loc[non_zero, "participants"]
    )
    df_plot.loc[non_zero, "Female"] = (
        df_plot.loc[non_zero, "participants_f"]
        / df_plot.loc[non_zero, "participants"]
    )

    df_plot = df_plot.dropna(subset=["Male", "Female"])
    df_plot["xlabel"] = df_plot["place_name"] + " " + df_plot["year"].astype(str)
    df_plot = df_plot.sort_values(["event_type", "year"])

    fig = px.bar(
        df_plot,
        x="xlabel",
        y=["Male", "Female"],
        title=(
            "How has the ratio of female:male participants changed "
            f"in the {event_type} paralympics?"
        ),
        labels={"xlabel": "", "value": "", "variable": ""},
        template="simple_white",
    )
    fig.update_xaxes(ticklen=0)
    fig.update_yaxes(tickformat=".0%")
    return fig


def scatter_map():
    """
    Create a world map with markers for Paralympics host locations.

    Returns:
        plotly.graph_objs._figure.Figure: Scatter geo figure.
    """
    df = get_api_data(API_ALL_URL)

    chart_df = df[["year", "place_name", "latitude", "longitude"]].copy()
    chart_df["longitude"] = chart_df["longitude"].astype(float)
    chart_df["latitude"] = chart_df["latitude"].astype(float)
    chart_df["name"] = chart_df["place_name"] + " " + chart_df["year"].astype(str)

    fig = px.scatter_geo(
        chart_df,
        lat="latitude",
        lon="longitude",
        hover_name="name",
        title="Where have the paralympics been held?",
        template="simple_white",
    )
    return fig


if __name__ == "__main__":
    fig1 = line_chart("sports")
    fig1.show()

    fig2 = bar_chart("Summer")
    fig2.show()

    fig3 = scatter_map()
    fig3.show()
