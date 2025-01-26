"""
Filename: fullDatabaseAssets.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc

headerTitle = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.Center(children=[
            dash.html.H1(children="Full Database",
                         style={"fontSize":45,
                                "margin-top":15,
                                "margin-bottom":15})],
        )])],
    style={"background-color":"#68BAEC",
           "margin":"auto"}
)

text01 = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.P(children=["""
        This is the entire database of schools and programs that are
        aligned in both medical/bio and engineering fields. All other
        pages base their data off this one database. Here you can browse
        all schools and programs at once. For a more organized
        presentation, please take a look at the other pages.
        """],
                    style={"fontSize":25,
                           "margin-top":45,
                           "margin-bottom":45})
    ])],
    style={"margin":"auto"}
)

