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

homeImage = dash.html.Img(src="assets/homeImg.png",
                          width="75%",)


homeTabs = dbc.Tabs(children=[
    dbc.Tab(children=[ha.introText],
            active_label_style={"font-weight": "bold"},
            label="Welcome",
            tab_id="tab01",
            style={"fontSize":25}),
    dbc.Tab(children=[ha.aboutText],
            active_label_style={"font-weight": "bold"},
            label="About",
            tab_id="tab02",
            style={"fontSize": 25}),
    dbc.Tab(children=[ha.updateText],
            active_label_style={"font-weight": "bold"},
            label="Updates",
            tab_id="tab03",
            style={"fontSize": 25}),
    ],
    active_tab="tab01"
)

homeRow = dbc.Row(children=[
    dbc.Col(children=[homeTabs],
            lg=5),
    dbc.Col(children=[homeImage],
            width={"offset":2})],
    style={"margin":"auto",
           "margin-bottom":"2%",
           "margin-top":"2%"})


layout = dash.html.Div(children=[ha.headerTitle,
                                 homeRow],
                       style={"width":"auto"})
