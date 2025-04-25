"""
Filename: gradPrograms.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca

dash.register_page(__name__,
                   title="Grad Programs")

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

toggleButton = dbc.Button(id="toggle-01",
                          n_clicks=0,
                          style={"background-color":"#AE8BF0"})

programAccordian = dash.html.Div(children=[
    dbc.Accordion(always_open=False,
                  id="accord-01")
])

closedAppMsg = dash.html.Center(children=[
    dash.html.Div(id="div-01",
                  style=ca.basicTextMargins01)])



layout = dash.html.Div(children=[headerTitle,
                                 text01,
                                 toggleButton,
                                 programAccordian,
                                 closedAppMsg])