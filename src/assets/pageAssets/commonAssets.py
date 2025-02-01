"""
Filename: commonAssets.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""
import dash
import pandas as pd
import dash_bootstrap_components as dbc

siteFooter = dbc.Row(children=[
        dash.html.Center(children="Created: Luciano L. Lorenzana, 2025",
                     style={"color":"#000000",
                            "margin-bottom":25,
                            "margin-top":25})],
    style={"background-color":"#0087D5",
           "margin":"auto"}
)

disclaimerFooter = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.P(children=[
            dash.html.H1(children=[
                dash.html.Center(children=["""
                *** DISCLAIMER ***\n
                """])]),
            dash.html.Center(children=["""
            This website is an independent project, and is in no way directly associated
            with any university or institution mentioned on this site. Any logos,
            imagery, names, and anything that was created or belonging to any
            university or institution is their own intellectual property. 
            This website is not monetized nor is it intended for any type of monetization 
            or revenue, all data and information present is hand selected via publicly 
            accessible information from said universities and institutions online through 
            their own websites.
            """],
                             style={"color":"#000000"})],
            style={"margin-top":15,
                   "margin-bottom":35,
                   "margin-right":250,
                   "margin-left":250,
                   })]
    )],
    style={"background-color":"#AE8BF0", #"#FF1000", "#9D72ED", "#FF584D"
           "margin":"auto"}
)

programDF = pd.read_csv(filepath_or_buffer="assets/EngineeringHealthGradPrograms.csv")

def DFFcn(tmpDF, var01, filterVar, sortVar):
    phDF = tmpDF.loc[tmpDF[filterVar] == var01].sort_values(sortVar)
    return  phDF.loc[:, phDF.columns != filterVar]
    pass

def accordChildren(tmpSet, tmpDF, var01, var02):
    tmpList = [dbc.AccordionItem(children=[
        dbc.Table.from_dataframe(DFFcn(tmpDF, tmpLabel, filterVar=var01, sortVar=var02),
                                 color="info",
                                 striped=True,
                                 style={"margin": "auto"})],
        title=tmpLabel,

    ) for tmpLabel in sorted(tmpSet)]

    return tmpList
    pass
