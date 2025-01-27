"""
Filename: home.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca
import assets.pageAssets.homeAssets as ha

dash.register_page(__name__,
                   title="Home",
                   path='/')


homeTabs = dbc.Tabs(children=[
    dbc.Tab(children=[ha.introText],
            active_label_style={"font-weight": "bold",
                                "fontSize":20},
            label="Welcome",
            tab_id="card01",
            style={"fontSize":25}),
    dbc.Tab(children=[ha.aboutText],
            active_label_style={"font-weight": "bold",
                                "fontSize": 20},
            label="About",
            tab_id="card02",
            style={"fontSize": 25}
            )],
    active_tab="card01"
)

homeRow = dbc.Nav(children=[
    dbc.Row(children=[
        dbc.Col(homeTabs,
                lg=5)],
    style={"margin":"auto",
           "margin-bottom":25,
           "margin-top":25})],

)


layout = dash.html.Div(children=[ha.headerTitle,
                                 homeRow],
                       style={"width":"auto"})
