"""
Filename: homeAssets.py
Created by: Luciano L. Lorenzana
Date: 1/20/2025
"""

import dash
import dash_bootstrap_components as dbc

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
"""
... to showcase and announce
       the variety of programs and majors that combine both medical and engineering fields. It 
       can be difficult to find work and programs that can blend both fields, difficult but not
       impossible. That's why this website was created, not only to inform the general public
       that such programs exist, but that two fields that can be perceived as exclusively separate 
       can in fact coexist.
"""
introText = dash.html.P(children=[
    dash.html.B(children=["""MedTech Programs """]),
    """
    is a site for people who have an interest in both engineering and medicine. Here, you'll 
    find institutions and degree programs within the medtech field. You can view the entire 
    database of programs and institutions, you can search programs via 
    institution, or search institutions via programs.
    """],
    style={"margin-top":"2%",
           "margin-bottom":"2%",
           "margin-left":"2%",
           "margin-right":"2%"})

aboutText = dash.html.P(children=[
    """
    The site started off as a Google spreadsheet, inspired after attending the
    """,
    dash.html.B(children=[" Pre-Health Conference at UC Davis "]),
    """
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
    style={"margin-top":"2%",
           "margin-bottom":"2%",
           "margin-left": "2%",
           "margin-right": "2%"})
