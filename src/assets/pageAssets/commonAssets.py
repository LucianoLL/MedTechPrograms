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
            This website is an independent project, and is no way associated directly
            with any university or institution mentioned in this website. Any logos,
            imagery, names, and anything that was created or belongs to any university 
            or institution mentioned is their own intellectual property. This website
            is not monetized nor is intended for any type of monetization, all data and
            information present was hand selected via publicly accessible information
            provided by said universities and institutions online through their own
            websites.
            """],
                             style={"color":"#000000"})],
            style={"margin-top":15,
                   "margin-bottom":15,
                   "margin-right":250,
                   "margin-left":250,
                   })]
    )],
    style={"background-color":"#FF584D", #"#FF1000",
           "margin":"auto"}
)

programDF = pd.read_csv(filepath_or_buffer="assets/EngineeringHealthGradPrograms.csv")

def DFFcn(tmpDF, var01, filterVar, sortVar):
    phDF = tmpDF.loc[tmpDF[filterVar] == var01].sort_values(sortVar)
    return  phDF.loc[:, phDF.columns != filterVar]
    pass
