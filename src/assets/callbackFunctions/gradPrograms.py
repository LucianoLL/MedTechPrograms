"""
Filename: gradPrograms.py
Created by: Luciano L. Lorenzana
Date: 2/1/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca

def gradProgramsFilters(app):
    @app.callback(
        dash.Output(component_id="accord-01", component_property="children"),
        dash.Output(component_id="toggle-01", component_property="style"),
        dash.Output(component_id="toggle-01", component_property="children"),
        dash.Output(component_id="row-01", component_property="children"),
        dash.Input(component_id="toggle-01", component_property="n_clicks")
    )
    def openAppFilter(toggle):
        tmpColor = {"background-color": "#AE8BF0"}
        tmpLabel = "Show Open Status Only",
        tmpDF = ca.programDF
        tmpChildren = None
        programSet = set()

        if (toggle % 2) == 0:
            for tmpPro in ca.programDF["Program"]:
                programSet.add(tmpPro)
                pass

        else:
            tmpColor = {"background-color":"#0087D5"}
            tmpLabel = "Show All"

            tmpDF = ca.programDF[ca.programDF["Open Status"] != "CLOSED"]

            for tmpPro in tmpDF["Program"]:
                programSet.add(tmpPro)
                pass

        if tmpDF.empty:
            tmpChildren = dash.html.Center(children=[
                ca.closedAppText,
                dbc.Col(children=[ca.img01],
                        lg=5)]
            )

        tmpAccord = ca.accordChildren(programSet, tmpDF, "Program", "Institution")
        return tmpAccord, tmpColor, tmpLabel, tmpChildren
