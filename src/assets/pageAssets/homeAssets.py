"""
Filename: homeAssets.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc
import assets.pageAssets.commonAssets as ca


headerTitle = dbc.Row(children=[
    dbc.Col(children=[
        dash.html.Center(children=[
            dash.html.H1(children="Home",
                         style={"fontSize":45,
                                "margin-top":"1%",
                                "margin-bottom":"1%"})]
        )])],
    style={"background-color":"#68BAEC",
           "margin":"auto"}
)

introText = dash.html.P(children=[
    dash.html.B(children=["""MedTech Programs """]),
    """
    is a site for people who have an interest in both engineering and medicine. Here, you'll 
    find institutions and degree programs within the medtech field. You can view the entire 
    database of programs and institutions, you can search programs via 
    institution, or search institutions via programs.
    """],
    style=ca.basicTextMargins01)

aboutText = dash.html.P(children=[
    """
    The site started off as a Google spreadsheet, inspired after attending a pre-health conference
    and realizing that there were very few programs that combined health, medicine, and 
    engineering. Yet, at the same time also realizing that there was a variety of majors
    and programs within medicine that allowed for engineering in their research.
    Thus, the search began for collecting information on programs that allowed for
    medicine and engineering, checking several university websites, scouring various
    major catalogues, information that's publicly accessible to anyone online.
    The only issue with a Google spreadsheet is that it's not as easy to
    share with the general public, which is why this site was created. The goal is for
    people to find this site in hopes of finding a major or program within the medtech
    field. Medicine and engineering don't have to be exclusively separate, nor should 
    they be.
    """],
    style=ca.basicTextMargins01)

updateText = dash.html.Div(children=[
    dash.html.H2(children=["4/25/2025"]),
    dash.html.P(children=[
        """
        Updated the database; updated the open status for the following programs who have closed their application 
        portals:
        """
    ]),
    dash.html.Ul(children=[
        dash.html.Li(children=["University of California, Los Angeles",
                               dash.html.Ul(children=[dash.html.Li(children=["Bioinformatics, Master of Science (MS)"])
                                                      ])
                               ])
    ]),
    dash.html.P(children=[
        """
        Also included a new message for the empty the dataframes since all known applications are currently closed, at 
        least those mentioned on the site. 
        """]),
    dash.html.P(children=[
        """
        There's also a new feature when clicking the "OPEN STATUS ONLY" filter. Since most applications are now closed,
        and the filter will now display an empty page, a message will take that place describing the current situation.
        """
    ])],
    style=ca.basicTextMargins01)

