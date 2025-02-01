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
        if (toggle % 2) == 0:
            tmpColor = {"background-color":"#AE8BF0"}
            tmpLabel = "Show Open Status Only",

            programSet = set()
            for tmpPro in ca.programDF["Institution"]:
                programSet.add(tmpPro)
                pass

            tmpList = ca.accordChildren(programSet, ca.programDF, "Institution", "Program")

        else:
            tmpColor = {"background-color":"#0087D5"}
            tmpLabel = "Show All"

            openDF = ca.programDF[ca.programDF["Open Status"] != "CLOSED"]
            programSet = set()
            for tmpPro in openDF["Institution"]:
                programSet.add(tmpPro)
                pass

            tmpList = ca.accordChildren(programSet, openDF, "Institution", "Program")

        return tmpList, tmpColor, tmpLabel
