"""
Filename: gradPrograms.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.gradProgramsAssets as gpa

dash.register_page(__name__,
                   title="Grad Programs")

toggleButton = dbc.Button(id="toggle-01",
                          n_clicks=0,
                          style={"background-color":"#AE8BF0"})

programAccordian = dash.html.Div(children=[
    dbc.Accordion(always_open=False,
                  id="accord-01")
])


layout = dash.html.Div(children=[gpa.headerTitle,
                                 gpa.text01,
                                 toggleButton,
                                 programAccordian])