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

homeImage = dash.html.Img(src="assets/homeLogo.png",
                          width=550,)


homeTabs = dbc.Tabs(children=[
    dbc.Tab(children=[ha.introText],
            active_label_style={"font-weight": "bold"},
            label="Welcome",
            tab_id="card01",
            style={"fontSize":25}),
    dbc.Tab(children=[ha.aboutText],
            active_label_style={"font-weight": "bold"},
            label="About",
            tab_id="card02",
            style={"fontSize": 25}
            )],
    active_tab="card01"
)

homeRow = dbc.Row(children=[
    dbc.Col(children=[homeTabs],
            width=6),
    dbc.Col(children=[homeImage],
            width={"offset":1})],
    style={"margin":"auto",
           "margin-bottom":25,
           "margin-top":25})


layout = dash.html.Div(children=[ha.headerTitle,
                                 homeRow],
                       style={"width":"auto"})
