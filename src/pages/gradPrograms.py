"""
Filename: gradPrograms.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca
import assets.pageAssets.gradProgramsAssets as gpa

dash.register_page(__name__,
                   title="Grad Programs")

programSet = set()
for tmpPro in ca.programDF["Program"]:
    programSet.add(tmpPro)
    pass

programAccordian = dash.html.Div(children=[
    dbc.Accordion(children=[
        dbc.AccordionItem(children=[
            dbc.Table.from_dataframe(#ca.programAccFcn(ca.programDF, tmpPro),
                                     ca.DFFcn(ca.programDF, tmpPro, "Program", "Institution"),
                                     color="info",
                                     striped=True,
                                     style={"margin":"auto"})],
            title=tmpPro,

        )
        for tmpPro in sorted(programSet)],
        always_open=False)
])


layout = dash.html.Div(children=[gpa.headerTitle,
                                 gpa.text01,
                                 programAccordian])