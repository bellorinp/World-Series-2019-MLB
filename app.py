# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:24:10 2020

Dashboard con estadísticas de los equipos de la serie mundial 2019 de la MLB.

@author: bellorinp
"""

import pathlib
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objs as go

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

"""Dataframes"""

#Bateo Astros
dfastrosbat = pd.read_csv(DATA_PATH.joinpath('Houston Astros Batting.csv'),
                 encoding = " ISO 8859-1")

dfastrosbat['BA'] = dfastrosbat['BA'].map('{:.3f}'.format)
dfastrosbat['OBP'] = dfastrosbat['OBP'].map('{:.3f}'.format)
dfastrosbat['SLG'] = dfastrosbat['SLG'].map('{:.3f}'.format)
dfastrosbat['OPS'] = dfastrosbat['OPS'].map('{:.3f}'.format)
dfastrosbat['BA1'] = dfastrosbat['BA1'].map('{:.3f}'.format)
dfastrosbat['OPS1'] = dfastrosbat['OPS1'].map('{:.3f}'.format)

#Pitcheo Astros
dfastrospitch = pd.read_csv(DATA_PATH.joinpath('Houston Astros Pitching.csv'),
                 encoding = " ISO 8859-1")

dfastrospitch['ERA'] = dfastrospitch['ERA'].map('{:.2f}'.format)
dfastrospitch['ERA.1'] = dfastrospitch['ERA.1'].map('{:.2f}'.format)
dfastrospitch['IP'] = dfastrospitch['IP'].map('{:.1f}'.format)
dfastrospitch['IP.1'] = dfastrospitch['IP.1'].map('{:.1f}'.format)
dfastrospitch['WHIP'] = dfastrospitch['WHIP'].map('{:.3f}'.format)
dfastrospitch['WHIP.1'] = dfastrospitch['WHIP.1'].map('{:.3f}'.format)

#Bateo Nationals
dfnatbat = pd.read_csv(DATA_PATH.joinpath('Washington Nationals Batting.csv'),
                 encoding = " ISO 8859-1")

dfnatbat['BA'] = dfnatbat['BA'].map('{:.3f}'.format)
dfnatbat['OBP'] = dfnatbat['OBP'].map('{:.3f}'.format)
dfnatbat['SLG'] = dfnatbat['SLG'].map('{:.3f}'.format)
dfnatbat['OPS'] = dfnatbat['OPS'].map('{:.3f}'.format)
dfnatbat['BA1'] = dfnatbat['BA1'].map('{:.3f}'.format)
dfnatbat['OPS1'] = dfnatbat['OPS1'].map('{:.3f}'.format)

#Pitcheo Nationals
dfnatpitch = pd.read_csv(DATA_PATH.joinpath('Washington Nationals Pitching.csv'),
                 encoding = " ISO 8859-1")

dfnatpitch['ERA'] = dfnatpitch['ERA'].map('{:.2f}'.format)
dfnatpitch['ERA.1'] = dfnatpitch['ERA.1'].map('{:.2f}'.format)
dfnatpitch['IP'] = dfnatpitch['IP'].map('{:.1f}'.format)
dfnatpitch['IP.1'] = dfnatpitch['IP.1'].map('{:.1f}'.format)
dfnatpitch['WHIP'] = dfnatpitch['WHIP'].map('{:.3f}'.format)
dfnatpitch['WHIP.1'] = dfnatpitch['WHIP.1'].map('{:.3f}'.format)


#Listas
bateadores = ['Jose Altuve', 'Yordan Álvarez', 'Michael Brantley', 'Alex Bregman',	
              'Robinson Chirinos', 'Gerrit Cole', 'Carlos Correa', 'Chris Devenski',
              'Aledmys Díaz', 'Zack Greinke', 'Yuli Gurriel', 'Will Harris',	
              'Josh James',	'Martin Maldonado',	'Jake Marisnick', 'Roberto Osuna',
              'Brad Peacock', 'Ryan Pressly', 'Josh Reddick', 'Hector Rondon',
              'Joe Smith', 'George Springer', 'Kyle Tucker', 'Jose Urquidy',
              'Justin Verlander', 'Astros de Houston', 'Matt Adams', 'Asdrubal Cabrera',	
              'Patrick Corbin',	'Sean Doolittle', 'Brian Dozier', 'Adam Eaton',	'Yan Gomes',	
              'Javy Guerra', 'Daniel Hudson', 'Howie Kendrick',	'Gerardo Parra',	
              'Tanner Rainey', 'Anthony Rendon', 'Victor Robles', 'Fernando Rodney', 
              'Joe Ross', 'Anibal Sanchez',	'Max Scherzer',	'Juan Soto', 'Stephen Strasburg',	
              'Wander Suero', 'Kurt Suzuki', 'Michael A. Taylor', 'Trea Turner',	
              'Ryan Zimmerman',	'Nacionales de Washington']

pitchers = ['Gerrit Cole', 'Chris Devenski', 'Zack Greinke', 'Will Harris', 'Josh James',
            'Roberto Osuna', 'Brad Peacock', 'Ryan Pressly', 'Hector Rondon','Joe Smith',
            'Jose Urquidy', 'Justin Verlander', 'Astros de Houston', 'Patrick Corbin', 
            'Sean Doolittle', 'Javy Guerra', 'Daniel Hudson', 'Tanner Rainey', 'Fernando Rodney',
            'Joe Ross', 'Anibal Sanchez', 'Max Scherzer', 'Stephen Strasburg', 'Wander Suero',
            'Nacionales de Washington']

#Bateo Jugador 
dfbat = pd.read_csv(DATA_PATH.joinpath('Playoff Batting.csv'),
                 encoding = " ISO 8859-1")

#Pitcheo Jugador 1
dfpitch = pd.read_csv(DATA_PATH.joinpath('Playoff Pitching.csv'),
                 encoding = " ISO 8859-1")

#Glosario
dfglo = pd.read_csv(DATA_PATH.joinpath('Glosary.csv'),
                 encoding = " ISO 8859-1")

"""App"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

"""Layaout"""

app.layout = html.Div([
        #Header
        html.Div(children=[
            html.H2("Estadísticas Equipos World Series 2019"), 
            html.Div(html.Img(id="logo", src=app.get_asset_url("logoWs2019.png"),
                               style={'height':'10%', 
                                      'width':'10%', 
                                      'position':'absolute',
                                      'top': '5px',
                                      'right': '10px',
                                      'display': 'inline-block',
                                      })
                     ),
            ], style={'display': 'inline-block', 'padding': '5px 5px 25px 5px'}
            ),
                
         #Tabs
            html.Div([
                dcc.Tabs(id="tabs", style={"height":"8","verticalAlign":"middle"},
                    children=[          
                    
                #Tab Astros de Houston    
                dcc.Tab(label='Astros de Houston', children=[                           
                    html.Div([html.Img(src=app.get_asset_url('Astros de Houston.jpg'),
                                       style={'height':'8%', 
                                               'width':'8%', 
                                              }
                                        ),
                            html.H3('Estadísticas de Bateo'),
                                dash_table.DataTable(
                                            data=dfastrosbat.to_dict('records'),
                                            columns=[
                                                     {"name": ["", "Nombre"], "id": "Nombre"},
                                                     {"name": ["Serie Playoff", "G"], "id": "G"},
                                                     {"name": ["Serie Playoff", "AB"], "id": "AB"},
                                                     {"name": ["Serie Playoff", "R"], "id": "R"},
                                                     {"name": ["Serie Playoff", "H"], "id": "H"},
                                                     {"name": ["Serie Playoff", "2B"], "id": "2B"},
                                                     {"name": ["Serie Playoff", "3B"], "id": "3B"},
                                                     {"name": ["Serie Playoff", "HR"], "id": "HR"},
                                                     {"name": ["Serie Playoff", "RBI"], "id": "RBI"},
                                                     {"name": ["Serie Playoff", "BB"], "id": "BB"},
                                                     {"name": ["Serie Playoff", "SO"], "id": "SO"},
                                                     {"name": ["Serie Playoff", "BA"], "id": "BA"},
                                                     {"name": ["Serie Playoff", "OBP"], "id": "OBP"},
                                                     {"name": ["Serie Playoff", "SLG"], "id": "SLG"},
                                                     {"name": ["Serie Playoff", "OPS"], "id": "OPS"},
                                                     {"name": ["Serie Playoff", "SB"], "id": "SB"},
                                                     {"name": ["Serie Playoff", "CS"], "id": "CS"},
                                                     {"name": ["Serie Playoff", "E"], "id": "E"},
                                                     {"name": ["Serie Playoff", "WPA"], "id": "WPA"},
                                                     {"name": ["Serie Regular", "G"], "id": "G1"},
                                                     {"name": ["Serie Regular", "AB"], "id": "AB1"},
                                                     {"name": ["Serie Regular", "R"], "id": "R1"},
                                                     {"name": ["Serie Regular", "H"], "id": "H1"},
                                                     {"name": ["Serie Regular", "RBI"], "id": "RBI1"},
                                                     {"name": ["Serie Regular", "SB"], "id": "SB1"},
                                                     {"name": ["Serie Regular", "BA"], "id": "BA1"},
                                                     {"name": ["Serie Regular", "OPS"], "id": "OPS1"},
                                                     ],
                                                      
                                            merge_duplicate_headers=True,
                                            sort_action='native',
                                            fixed_rows={'headers': True},
                                             
                                            style_table={'height': '300px', 
                                                        'overflowY': 'auto',
                                                        'overflowX': 'auto'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                        'height': 'auto', 
                                                        'minWidth': '15px', 'width': '30px', 'maxWidth': '80px',
                                                        'fontSize': 12,
                                                        'textAlign': 'center'},
                                                          
                                            style_header={'backgroundColor': '#191970',
                                                        'border': '2px solid #cd4f39',
                                                        'fontSize': 14,
                                                        'color': 'white'},
                                                           
                                            style_data_conditional=[
                                                        {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'},
                                                                    
                                                        {
                                                        'if': {'filter_query': '{Nombre} contains  "Totales y Promedios"'},
                                                        'backgroundColor': '#cd4f39',
                                                        'color': 'white',
                                                        'fontsize': 11,
                                                        'fontWeight': 'bold'},                                                            
                                                            ],
                                            ),
                                            
                                html.P(id="leyenda-astros-bateo",
                                      children="*Bateador Zurdo."
                                         ),
                                                   
                                        ], style={'width': '98%', 
                                                  'display': 'block',
                                                   'padding': '5px 5px 5px 5px',
                                                 }
                                ),                            
                                   
                               html.Div([
                                    html.H3('Estadísticas de Pitcheo'),
                                        dash_table.DataTable(
                                            data=dfastrospitch.to_dict('records'),
                                            columns=[
                                                     {"name": ["", "Nombre"], "id": "Nombre"},
                                                     {"name": ["Serie Playoff", "G"], "id": "G"},
                                                     {"name": ["Serie Playoff", "GS"], "id": "GS"},
                                                     {"name": ["Serie Playoff", "ERA"], "id": "ERA"},
                                                     {"name": ["Serie Playoff", "W"], "id": "W"},
                                                     {"name": ["Serie Playoff", "L"], "id": "L"},
                                                     {"name": ["Serie Playoff", "SV"], "id": "SV"},
                                                     {"name": ["Serie Playoff", "CG"], "id": "CG"},
                                                     {"name": ["Serie Playoff", "IP"], "id": "IP"},
                                                     {"name": ["Serie Playoff", "H"], "id": "H"},
                                                     {"name": ["Serie Playoff", "R"], "id": "R"},
                                                     {"name": ["Serie Playoff", "ER"], "id": "ER"},
                                                     {"name": ["Serie Playoff", "BB"], "id": "BB"},
                                                     {"name": ["Serie Playoff", "SO"], "id": "SO"},
                                                     {"name": ["Serie Playoff", "WHIP"], "id": "WHIP"},
                                                     {"name": ["Serie Playoff", "WPA"], "id": "WPA"},
                                                     {"name": ["Serie Regular", "G"], "id": "G.1"},
                                                     {"name": ["Serie Regular", "GS"], "id": "GS.1"},
                                                     {"name": ["Serie Regular", "ERA"], "id": "ERA.1"},
                                                     {"name": ["Serie Regular", "W"], "id": "W.1"},
                                                     {"name": ["Serie Regular", "L"], "id": "L.1"},
                                                     {"name": ["Serie Regular", "SV"], "id": "SV.1"},
                                                     {"name": ["Serie Regular", "IP"], "id": "IP.1"},
                                                     {"name": ["Serie Regular", "H"], "id": "H.1"},
                                                     {"name": ["Serie Regular", "BB"], "id": "BB.1"},
                                                     {"name": ["Serie Regular", "SO"], "id": "SO.1"},
                                                     {"name": ["Serie Regular", "WHIP"], "id": "WHIP.1"},
                                                     ],
                                              
                                            merge_duplicate_headers=True,
                                            sort_action='native',
                                            fixed_rows={'headers': True},
                                              
                                            style_table={'height': '400px', 
                                                        'overflowY': 'auto',
                                                        'overflowX': 'auto'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                        'height': 'auto', 
                                                        'minWidth': '15px', 'width': '30px', 'maxWidth': '80px',
                                                        'fontSize': 12,
                                                        'textAlign': 'center'},
                                                           
                                            style_header={
                                                        'backgroundColor': '#191970',
                                                        'border': '2px solid #cd4f39',
                                                        'fontSize': 14,
                                                        'color': 'white'},
                                                        
                                            style_data_conditional=[
                                                        {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'},
                                                            
                                                        {
                                                        'if': {'filter_query': '{Nombre} contains  "Totales y Promedios"'},
                                                        'backgroundColor': '#cd4f39',
                                                        'color': 'white',
                                                        'fontsize': 12,
                                                        'fontWeight': 'bold'},                                                            
                                                        ],
                                              ), 

                                html.P(id="permisos-astros",
                                        children="Fuente: Baseball Reference, \
                                        https://www.baseball-reference.com/postseason/2019_WS.shtml, \
                                        Copyright © 2000-2020 Sports Reference LLC."  
                                        "Logos tomados de: Chris Creamer's Sports Logos Page - SportsLogos.Net, \
                                        https://www.sportslogos.net, \
                                        Copyright ©1997-2020 Chris Creamer.\
                                        All logos are the trademark & property of their owners. \
                                        We present them h
