"""
Filename: institutionAssets.py
Created by: Luciano L. Lorenzana
Date: 1/21/2025
"""

import dash
import dash_bootstrap_components as dbc

headerTitle = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.Center(children=[
            dash.html.H1(children="Institutions",
                         style={"fontSize":45,
                                "margin-top":15,
                                "margin-bottom":15})],
        )])],
    style={"background-color":"#68BAEC",
           "margin":"auto"}
)

text01 = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.P(children=["""All institutions are organized by their offered""",
                              dash.html.B(children=[" MedTech "]),
                              """
                              programs. Clicking on each institute will display
                              a table of programs offered at that institution.
                              """],
                    style={"margin-right":250,
                           "margin-left":250})],
        style={"fontSize":25,
               "margin-top":45,
               "margin-bottom":45}
    )],
    style={"margin":"auto"}
)
