"""
Filename: fullDatabase.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import assets.pageAssets.commonAssets as ca
import assets.pageAssets.fullDatabaseAssets as fda

dash.register_page(__name__,
                   title="Full Database")

firstTable = dbc.Table.from_dataframe(ca.programDF.sort_values("Program"),
                                      color="info",
                                      striped=True)

layout = dash.html.Div(children=[fda.headerTitle,
                                 fda.text01,
                                 firstTable])
