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
                                "margin-top":"1%",
                                "margin-bottom":"1%"})],
        )])],
    style={"background-color":"#68BAEC",
           "margin":"auto"}
)

text01 = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.P(children=["""
        This is the entire database of programs and institutions that are
        in the medtech field. All other pages base their data off this one 
        database. Here you can browse all programs and institutions at once. 
        For a more organized presentation, please take a look at the other 
        pages.
        """],
                    style={"margin-right": "15%",
                           "margin-left": "15%"})],
        style={"fontSize":25,
               "margin-top":"2%",
               "margin-bottom":"2%"}
    )],
    style={"margin":"auto"}
)

