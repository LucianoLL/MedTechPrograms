"""
Filename: gradProgramsAssets.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc

headerTitle = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.Center(children=[
            dash.html.H1(children="Grad Programs",
                         style={"fontSize":45,
                                "margin-top":"1%",
                                "margin-bottom":"1%"})]
        )])],
    style={"background-color": "#68BAEC",
           "margin": "auto"}
)

text01 = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.P(children=["""All schools and institutions are organized by their""",
                              dash.html.B(children=[" MedTech "]),
                              """
                              programs. Clicking on each program will display a list of
                              schools and institutions that offer that specific program.
                              """],
                    style={"margin-right":"15%",
                           "margin-left":"15%"})],
        style={"fontSize":25,
               "margin-top":"2%",
               "margin-bottom":"2%"}
    )],
    style={"margin":"auto"}
)


