"""
Filename: institutions.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca

dash.register_page(__name__,
                   title="Institutions")

headerTitle = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.Center(children=[
            dash.html.H1(children="Institutions",
                         style={"fontSize":45,
                                "margin-top":"1%",
                                "margin-bottom":"1%"})],
        )])],
    style={"background-color":"#68BAEC",
           "margin":"auto"}
)

text01 = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.P(children=["""All institutions are organized by their offered""",
                              dash.html.B(children=[" MedTech "]),
                              """
                              programs. Clicking on each institution will display
                              a table of programs offered at that institution.
                              """],
                    style={"margin-right":"15%",
                           "margin-left":"15%"})],
        style={"fontSize":25,
               "margin-top":"2%",
               "margin-bottom":"2%"}
    )],
    style={"margin":"auto"}
)

toggleButton = dbc.Button(id="toggle-02",
                          n_clicks=0,
                          style={"background-color":"#AE8BF0"})

institutionAccordian = dash.html.Div(children=[
    dbc.Accordion(always_open=False,
                  id="accord-02")
])

closedAppMsg = dash.html.Center(children=[
    dash.html.Div(id="div-02",
                  style=ca.basicTextMargins01)])

layout = dash.html.Div(children=[headerTitle,
                                 text01,
                                 toggleButton,
                                 institutionAccordian,
                                 closedAppMsg])
