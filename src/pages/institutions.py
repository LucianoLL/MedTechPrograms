"""
Filename: institutions.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.institutionsAssets as ia

dash.register_page(__name__,
                   title="Institutions")

toggleButton = dbc.Button(id="toggle-02",
                          n_clicks=0,
                          style={"background-color":"#AE8BF0"})

institutionAccordian = dash.html.Div(children=[
    dbc.Accordion(always_open=False,
                  id="accord-02")
])

layout = dash.html.Div(children=[ia.headerTitle,
                                 ia.text01,
                                 toggleButton,
                                 institutionAccordian])
