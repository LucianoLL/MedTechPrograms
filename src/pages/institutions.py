"""
Filename: institutions.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import assets.pageAssets.commonAssets as ca
import assets.pageAssets.institutionsAssets as ia

dash.register_page(__name__,
                   title="Institutions")

institutionSet = set()
for tmpInst in ca.programDF["Institution"]:
    institutionSet.add(tmpInst)
    pass

institutionAccordian = dash.html.Div(children=[
    dbc.Accordion(children=[
        dbc.AccordionItem(children=[
            dbc.Table.from_dataframe(ca.DFFcn(ca.programDF, tmpInst, "Institution", "Program"),
                                     color="info",
                                     striped=True,
                                     style={"margin":"auto"})],
            title=tmpInst)
        for tmpInst in sorted(institutionSet)],
        always_open=False)
])

layout = dash.html.Div(children=[ia.headerTitle,
                                 ia.text01,
                                 institutionAccordian])
