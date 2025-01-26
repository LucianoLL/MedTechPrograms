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
    dash.html.B(children=[
        """MedTech Programs """]),
    """
    is a site for people who have an interest in both engineering and medicine. Here, you'll 
    find institutions and degree programs within the med tech field. You can view the entire 
    database of programs and institutions at it's current state, you can search programs via 
    institution, or search institutions via programs.
    """],
    style={"margin-left":15,
           "margin-right":15})
