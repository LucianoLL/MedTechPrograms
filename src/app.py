"""
Filename: app.py
Created by: Luciano L. Lorenzana
Date: 1/18/2025
"""

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import assets.pageAssets.commonAssets as ca

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.LUX,
                                      dbc.icons.FONT_AWESOME],
                use_pages=True)

app._favicon = "logo.ico"


siteLogo = dash.html.Img(src="assets/logo.png",
                         style={"width": 450})

headerRow = dash.html.A(
    dbc.Row(children=[dbc.Col(children=siteLogo)]),
    href="/",
    style={"margin-left":100}
)

siteNavbar = dbc.Navbar(children=[headerRow],
    color="light"
)

pagesNavbar = dbc.Nav([
    dbc.NavItem(
        dbc.NavLink(children=page["title"],
                    id="button" + str(ind),
                    href=page["relative_path"])
    ) for ind, page in enumerate(dash.page_registry.values())],
    justified=True,
    style={"background-color":"#0087D5",
           "fontSize":30}
)

app.layout = dash.html.Div(children=[siteNavbar,
                                     pagesNavbar,
                                     dash.page_container,
                                     ca.siteFooter,
                                     ca.disclaimerFooter])


if __name__ == '__main__':
    app.run(debug=True, port=8060)
