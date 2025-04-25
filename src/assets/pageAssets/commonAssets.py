"""
Filename: commonAssets.py
Created by: Luciano L. Lorenzana
Date: 1/19/2025
"""
import dash
import pandas as pd
import dash_bootstrap_components as dbc


""" Common Images """
img01 = dash.html.Img(src="assets/closedAppsImg.png",
                      width="50%")

""" Universal CSS """
basicTextMargins01 = {"margin-top": "2%",
                      "margin-bottom": "2%",
                      "margin-left": "2%",
                      "margin-right": "2%"}

""" Common Text """
siteFooter = dbc.Row(children=[
        dash.html.Center(children=["Updated as of 4/16/2025"],
                         style={"color": "#000000",
                                "margin-bottom": "1%",
                                "margin-top": "1%"})],
    style={"background-color":"#0087D5",
           "margin":"auto",
           "margin-top":"2%"}
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
            with or endorsed by any university or institution mentioned on this site. Any logos,
            imagery, names, and anything that was created or belonging to any
            university or institution is their own intellectual property and or trademark. 
            This website is not monetized nor is it intended for any type of monetization 
            or revenue, all data and information present is hand selected via publicly 
            accessible information from said universities and institutions online through 
            their own websites.
            """],
                             style={"color":"#000000"})],

            style={"margin-top":"1%",
                   "margin-bottom":"5%",
                   "margin-right":"15%",
                   "margin-left":"15%",
                   })]
    )],
    style={"background-color":"#AE8BF0", #"#FF1000", "#9D72ED", "#FF584D"
           "margin":"auto"}
)

closedAppText = dash.html.P(children=[
    dash.html.H1(children=[
        dash.html.B(children="All Applications Are Currently Closed")],
        style={"text-align": "center"}
    ),
    """
    All applications for Fall of 2025 are currently closed, at least for the programs referenced on this site.
    Please check throughout the year to see if any institutions or programs have opened their applications
    for Fall of next year. You can also take a look at each institution's website, or contact their own admissions 
    office to see when applications open up again.
    """],
    style={"text-align":" center",
           "fontSize": "150%"}
)


""" Common Functions """
def clickableLinkFcn(tmpURL):
    return dash.html.A(children=[tmpURL],
                       target="_blank",
                       href=tmpURL)

    pass

programDF = pd.read_csv(filepath_or_buffer="assets/medtechDatabase.csv")
programDF["Program Website"] = programDF["Program Website"].apply(clickableLinkFcn)

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
