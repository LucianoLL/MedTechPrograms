"""
Filename: app.py
Created by: Luciano L. Lorenzana
Date: 1/18/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca
import assets.callbackFunctions.gradPrograms as gpf
import assets.callbackFunctions.institutions as icf


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.LUX,
                                      dbc.icons.FONT_AWESOME],
                use_pages=True)

server = app.server

app._favicon = "logo.ico"


siteLogo = dash.html.Img(src="assets/logo.png",
                         style={"width": "30%"})

siteNavbar = dbc.Navbar(children=[
    dbc.Col(children=[
        dash.html.A(children=[siteLogo],
                    href="/",
                    style={"margin-left":"1%"})]),
    dbc.Nav(children=[
            dash.html.Div(children=[
                dbc.Button(children=["GitHub Repo"],
                           href="https://github.com/LucianoLL/MedTechPrograms",
                           style={"background-color":"#AE8BF0"},
                           target="_blank")])], # "#68BAEC"
        fill=True,
        style={"margin-right":"2%"})],
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

gpf.gradProgramsFilters(app=app)
icf.institutionsFilters(app=app)

if __name__ == '__main__':
    app.run_server(debug=True)
    # app.run(debug=True)

