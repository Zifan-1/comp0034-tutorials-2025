# Introduction to creating charts with Plotly Express and Go

# Tutorial 2: Creating and adding charts to a Dash app

## Introduction

In this tutorial you will learn to create and add charts to an app. The approach for this varies
by framework, so where there are variants of an activity, please follow the version for your
chosen framework.

## Plotly graphing library for Python

The Plotly graphing library for Python has two packages within it, Plotly Express and Plotly Go.

Plotly Express provides Python classes and functions to create most types of charts, and in most
cases will be enough for the coursework.

If you need to edit aspects of a chart that are not available through Express functions, use Go
instead.

Many of the chart examples in the [Plotly documentation](https://plotly.com/python/) start with an
Express example, then show features that require Go. They also include a version that can be added 
to a Dash app.

## Choosing the type of chart

The Plotly documentation shows examples of code for many types of chart. However, this assumes you
already know the type of chart you want to create. To help you decide which type of chart may be 
suited to your particular data and audience, try one of the following:

- [Data Visualisation Catalogue](https://datavizcatalogue.com/search.html)
- [Depict Data Studio](https://depictdatastudio.com/charts/)
- [Page with links to other chart choosers](https://coolinfographics.com/dataviz-guides)

## Creating a chart

The general approach to creating a chart and adding it to a web app is:

1. Access the required data, e.g. from:

    - sqlite database
    - .csv/.xlsx file
    - REST API in JSON format
2. Manipulate the data in a Pandas dataframe
3. Create a chart object using the dataframe data
4. Add the chart object to the Dash app layout

The database, `paralympics.db` has the following tables:

The Excel file, `paralympics.xlsx` has the following columns:

There is code that returns both the .xlsx and each of the tables in JSON format in `mock_api.py`:

- `def get_event_data()` reads the Excel table and returns the rows as JSON
- `class MockAPI()` has functions that each reads all rows from one of the tables abd returns the rows as JSON


[Next activity](2-2-line-chart.md)