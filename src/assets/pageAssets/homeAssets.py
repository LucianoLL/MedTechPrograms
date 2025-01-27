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
                                "margin-top":15,
                                "margin-bottom":15})]
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
    """,
    dash.html.Br()
    ,
    """
    Updates on this website will be sparse since it is only one person running the site,
    and can be difficult to keep track of new programs and institutions, along with
    keeping track of deadlines. Perhaps in the future more people could contribute,
    but for now it is just one person running everything.
    """],
    style={"margin-left":15,
           "margin-right":15})

aboutText = dash.html.P(children=[
    """
    The site started off as a Google spreadsheet, inspired after attending the
    """,
    dash.html.B(children=[" Pre-Health Conference at UC Davis "]),
    """
    and realizing that there were very few programs that combined health, medicine, and 
    engineering. Yet, at the same time also realizing that there was a variety of majors
    and programs within medicine that allowed for engineering in their research.
    Thus the search began for collecting information on programs that allowed for
    medicine and engineering, through that research is also how the term
    """,
    dash.html.B(children=" medtech "),
    """
    came to light. The only issue with a Google spreadsheet is that it's not as easy to
    share with the general public, which is why this site was created.
    """],
    style={"margin-left": 15,
           "margin-right": 15})
