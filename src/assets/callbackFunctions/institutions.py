"""
Filename: institutions.py
Created by: Luciano L. Lorenzana
Date: 2/1/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca

def institutionsFilters(app):
    @app.callback(
        dash.Output(component_id="accord-02", component_property="children"),
        dash.Output(component_id="toggle-02", component_property="style"),
        dash.Output(component_id="toggle-02", component_property="children"),
        dash.Input(component_id="toggle-02", component_property="n_clicks")
    )
    def openAppFilter(toggle):
        tmpDF = ca.programDF
        programSet = set()

        if (toggle % 2) == 0:
            tmpColor = {"background-color":"#AE8BF0"}
            tmpLabel = "Show Open Status Only",

            for tmpPro in ca.programDF["Institution"]:
                programSet.add(tmpPro)
                pass

        else:
            tmpColor = {"background-color":"#0087D5"}
            tmpLabel = "Show All"

            tmpDF = ca.programDF[ca.programDF["Open Status"] != "CLOSED"]

            for tmpPro in tmpDF["Institution"]:
                programSet.add(tmpPro)
                pass

        tmpAccord = ca.accordChildren(programSet, tmpDF, "Institution", "Program")
        return tmpAccord, tmpColor, tmpLabel
