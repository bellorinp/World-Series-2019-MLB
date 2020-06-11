# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:24:10 2020

Dashboard con estadísticas de los equipos de la serie mundial 2019 de la MLB.

@author: bellorinp
"""

import os
from random import randint
import pathlib
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objs as go

#Data folder
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
#Server
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

"""Layaout"""

app.layout = html.Div([
        #Header
        html.Div(children=[
            html.H2("Estadísticas Equipos World Series 2019"), 
            html.Div(html.Img(id="logo", src=app.get_asset_url("logoWS2019.png"),
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
                dcc.Tab(label='Astros de Houston', className="one column", children=[                           
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
                                        Copyright © 2000-2020 Sports Reference LLC. Logos tomados de: \
                                        Chris Creamer's Sports Logos Page - SportsLogos.Net, \
                                        https://www.sportslogos.net, \
                                        Copyright ©1997-2020 Chris Creamer.\
                                        All logos are the trademark & property of their owners. \
                                        We present them here for purely educational purposes.",
                                        style={'fontSize': 11},  
                                            ),   
                                                                                    
                                ], style={'width': '98%', 
                                          'display': 'block', 
                                          'padding': '5px 5px 5px 5px'}
                                ),
                            ]),

        #Tab Nacionales de Washington
                dcc.Tab(label='Nacionales de Washington',className="one column", children=[ 
                    html.Div([html.Img(src=app.get_asset_url('Nacionales de Washington.jpg'),
                                       style={'height':'8%', 
                                               'width':'8%', 
                                              }
                                        ),

                            html.H3('Estadísticas de Bateo'),                       
                                dash_table.DataTable(
                                           data=dfnatbat.to_dict('records'),
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
                                             
                                            style_table={'height': '400px', 
                                                        'overflowY': 'auto',
                                                        'overflowX': 'auto'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                        'height': 'auto', 
                                                        'minWidth': '15px', 'width': '30px', 'maxWidth': '80px',
                                                        'fontSize': 12,
                                                        'textAlign': 'center'},
                                                          
                                            style_header={'backgroundColor': '#191970',
                                                        'border': '2px solid #8b0000',
                                                        'fontSize': 14,
                                                        'color': 'white'},
                                                           
                                            style_data_conditional=[
                                                           {
                                                        'if': {'row_index': 'odd'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'},
                                                                    
                                                            {
                                                        'if': {'filter_query': '{Nombre} contains  "Totales y Promedios"'},
                                                        'backgroundColor': '#8b0000',
                                                        'color': 'white',
                                                        'fontsize': 12,
                                                        'fontWeight': 'bold'},                                                                                                                        
                                                            ],
                                              ),
                                            
                                        html.P(id="leyenda-nationals-bateo",
                                                   children="*Bateador Zurdo  #Bateador Ambidiestro."
                                                  ),
                                                   
                                            ], style={'width': '98%', 
                                                      'display': 'block',
                                                      'padding': '5px 5px 5px 5px',
                                                      }
                                ),                            
                                   
                             html.Div([ 
                                html.H3('Estadísticas de Pitcheo'),
                                    dash_table.DataTable(
                                            data=dfnatpitch.to_dict('records'),
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
                                              
                                            style_table={'height': '300px', 
                                                          'overflowY': 'auto',
                                                          'overflowX': 'auto'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                           'height': 'auto', 
                                                           'minWidth': '15px', 'width': '30x', 'maxWidth': '80px',
                                                           'fontSize': 12,
                                                           'textAlign': 'center'},
                                                           
                                            style_header={
                                                            'backgroundColor': '#191970',
                                                            'border': '2px solid #8b0000',
                                                            'fontSize': 14,
                                                            'color': 'white'},
                                                        
                                            style_data_conditional=[
                                                            {
                                                            'if': {'row_index': 'odd'},
                                                            'backgroundColor': 'rgb(248, 248, 248)'},
                                                            
                                                            {
                                                             'if': {'filter_query': '{Nombre} contains  "Totales y Promedios"'},
                                                             'backgroundColor': '#8b0000',
                                                             'color': 'white',
                                                             'fontsize': 12,
                                                             'fontWeight': 'bold'},
                                                            
                                                            ],
                                              ),
                                                
                            html.P(id="leyenda-nationals-pitcheo",
                                                   children="*Lanzador Zurdo.",

                                                  ),
                                            
                            html.P(id="permisos-nationals",
                                    children="Fuente: Baseball Reference, \
                                    https://www.baseball-reference.com/postseason/2019_WS.shtml, \
                                    Copyright © 2000-2020 Sports Reference LLC. Logos tomados de: \
                                    Chris Creamer's Sports Logos Page - SportsLogos.Net, \
                                    https://www.sportslogos.net, \
                                    Copyright ©1997-2020 Chris Creamer.\
                                    All logos are the trademark & property of their owners. \
                                    We present them here for purely educational purposes.",
                                    
                                    style={'fontSize': 11},  
                                    ),
                                                   
                            ], style={'width': '98%', 
                                      'display': 'block',
                                      'padding': '5px 5px 5px 5px'}
                                ),
                            ]),                                     
                                
        #Tab Comparativas de Jugadores
            dcc.Tab(label='Comparativa de Jugadores', children=[ html.H3('Serie Playoff'),                       
                    #Bateadores
                html.Div([
                    html.Div(['Bateador 1',
                        dcc.Dropdown(
                                    id='filtro-bateador1',
                                    options=[{'label': i, 'value': i} for i in bateadores],
                                    value='Jose Altuve' #valor que saldrá por defecto en la app
                                    ),
             
                            ],style={'width': '15%', 'display': 'inline-block',
                                    'padding': '5px 5px 5px 120px'}
                            ),
                                        
                    html.Div(['Bateador 2',
                        dcc.Dropdown(
                                    id='filtro-bateador2',
                                    options=[{'label': i, 'value': i} for i in bateadores],
                                    value='Asdrubal Cabrera' #valor que saldrá por defecto en la app
                                    ),
                            ],style={'width': '15%', 'display': 'inline-block',
                                    'padding': '5px 5px 5px 40px'}
                            ),

                    ], style={
                            'borderBottom': 'thin lightgrey solid',
                            'backgroundColor': 'rgb(250, 250, 250)',
                            'padding': '5px 5px 5px 10px'},
                        ),
                        
                    html.Div([
                        html.Div([
                            html.Img(id='img-bat1',
                                    src=[{'label': i, 'value': i} for i in bateadores],
                                    style={'height':'8%',
                                            'width': '8%',
                                            'float': 'left',
                                            'padding': '5px 5px 0px 200px'
                                            },
                                    )
                              ]),
                              
                        html.Div([
                            html.Img(id='img-bat2',
                                    src=[{'label': i, 'value': i} for i in bateadores],
                                    style={'height':'8%', 
                                            'width':'8%',
                                            'padding': '5px 5px 0px 120px'
                                             },
                                    )
                             ]),
                                 
                        ], style={'display': 'inline'}
                                 ),
                                                                               
                        html.Div([                                                                                                                               
                            html.Div([                                       
                                dash_table.DataTable(
                                           id='bateador1',
                                            data=dfbat.to_dict('records'),
                                            columns=[
                                                     {"name": "", "id": "Atributo"},
                                                     {"name": "", "id": "Valor"},
                                                     ],                                                      
                                            style_table={'height': '250px'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                        'height': 'auto', 
                                                        'minWidth': '3px', 'width': '3px', 'maxWidth': '3px',
                                                        'fontSize': 16,
                                                        'textAlign': 'center'},
                                                          
                                            style_data={ 'border': '1px solid Lightblue' },
                                             
                                            style_data_conditional=[{
                                                     'if': {'column_id': 'Atributo'},
                                                     'backgroundColor': 'Navy',
                                                     'color': 'white',
                                                     'border': '0px solid blue',
                                                     'header': 'crimson'},
                                                     {'if': {'column_id': 'Atributo'},
                                                           'width': '25%'},
                                                     {'if': {'column_id': 'Valor'},
                                                            'width': '75%'},
                                                     ],
                                                          
                                            style_header={'backgroundColor': 'navy',
                                                           'border': '1px solid navy'},                                                                                                   
                                              ), 

                                        ], style={'width': '25%', 
                                                  'display': 'inline-block',
                                                   'padding': '0px 5px 5px 0px'},
                                    ),
                                             
                        html.Div([          
                            dash_table.DataTable(
                                            id='bateador2',
                                            data=dfbat.to_dict('records'),
                                            columns=[
                                                     {"name": "", "id": "Valor"},
                                                     ],                                                      
                                             
                                            style_table={'height': '250px'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                        'height': 'auto', 
                                                        'minWidth': '3px', 'width': '3px', 'maxWidth': '3px',
                                                        'fontSize': 16,
                                                        'textAlign': 'center',
                                                        },
                                            style_data={ 'border': '1px solid Lightblue' },
                                                          
                                            style_header={'backgroundColor': 'crimson',
                                                           'border': '1px solid crimson'},
                                            ),

                                        ], style={'width': '19%', 
                                                   'display': 'inline-block',
                                                   'padding': '0px 0px 5px 5px'},
                                        ),
                                             
                            html.Div([
                                dcc.Graph(id='gráfica-scatter'),
                                     ], style={'display': 'inline-block', 'float': 'right',
                                               'width': '40%'}
                                       ),
                                     
                            html.Div([
                                dcc.Graph(id='gráfica-bar'),
                                     ], style={'display': 'inline-block', 'float': 'right',
                                               'width': '12%'}
                                      ),
                                             
                                             
                                ]), 
                              
                    #Pitchers
                    html.Div([
                         html.Div(['Pitcher 1',
                            dcc.Dropdown(
                                        id='filtro-pitcher1',
                                        options=[{'label': i, 'value': i} for i in pitchers],
                                        value='Zack Greinke' #valor que saldrá por defecto en la app
                                      ),
             
                                   ],style={'width': '15%', 'display': 'inline-block',
                                            'padding': '80px 5px 5px 120px'}
                                 ),
                                        
                        html.Div(['Pitcher 2',
                            dcc.Dropdown(
                                        id='filtro-pitcher2',
                                        options=[{'label': i, 'value': i} for i in pitchers],
                                        value='Max Scherzer' #valor que saldrá por defecto en la app
                                       ),
                                   ],style={'width': '15%', 'display': 'inline-block',
                                            'padding': '5px 5px 5px 40px'}
                                 ),
                        
                        ], style={'borderBottom': 'thin lightgrey solid',
                                  'backgroundColor': 'rgb(250, 250, 250)',
                                   'padding': '120px 5px 5px 10px'},
                                ),
                        
                        html.Div([
                            html.Div([
                                html.Img(id='img-pitch1',
                                            src=[{'label': i, 'value': i} for i in pitchers],
                                            style={'height':'8%',
                                                   'width': '8%',
                                                   'float': 'left',
                                                   'padding': '5px 5px 0px 200px'
                                                },
                                         )
                                   ]),
                              
                        html.Div([
                            html.Img(id='img-pitch2',
                                            src=[{'label': i, 'value': i} for i in pitchers],
                                            style={'height':'8%', 
                                                   'width':'8%',
                                                   'padding': '5px 5px 0px 120px'
                                               },
                                        )
                               ]),
                                 
                        ], style={'display': 'inline'}
                                 ),
                                                                               
                        html.Div([                                                                                                                               
                             html.Div([                                       
                                dash_table.DataTable(
                                            id='pitcher1',
                                            data=dfbat.to_dict('records'),
                                            columns=[
                                                     {"name": "", "id": "Atributo"},
                                                     {"name": "", "id": "Valor"},
                                                     ],                                                      
                                            style_table={'height': '250px'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                        'height': 'auto', 
                                                        'minWidth': '3px', 'width': '3px', 'maxWidth': '3px',
                                                        'fontSize': 16,
                                                        'textAlign': 'center'},
                                                          
                                            style_data={ 'border': '1px solid Lightblue' },
                                             
                                            style_data_conditional=[{
                                                     'if': {'column_id': 'Atributo'},
                                                     'backgroundColor': 'Navy',
                                                     'color': 'white',
                                                     'border': '0px solid blue',
                                                     'header': 'crimson'},
                                                     {'if': {'column_id': 'Atributo'},
                                                           'width': '25%'},
                                                     {'if': {'column_id': 'Valor'},
                                                            'width': '75%'},
                                                     ],
                                                          
                                            style_header={'backgroundColor': 'navy',
                                                           'border': '1px solid navy'},                                                                                                   
                                              ), 

                                            ], style={'width': '25%', 
                                                      'display': 'inline-block',
                                                      'padding': '0px 5px 5px 0px'},
                                    ),
                                             
                        html.Div([          
                            dash_table.DataTable(
                                            id='pitcher2',
                                            data=dfbat.to_dict('records'),
                                            columns=[
                                                     {"name": "", "id": "Valor"},
                                                     ],                                                      
                                             
                                            style_table={'height': '250px'},
                                                           
                                            style_cell={'whiteSpace': 'normal', 
                                                          'height': 'auto', 
                                                          'minWidth': '3px', 'width': '3px', 'maxWidth': '3px',
                                                          'fontSize': 16,
                                                          'textAlign': 'center',
                                                          },
                                            style_data={ 'border': '1px solid Lightblue' },
                                                          
                                            style_header={'backgroundColor': 'crimson',
                                                           'border': '1px solid crimson'},
                                            ),

                                            ], style={'width': '19%', 
                                                      'display': 'inline-block',
                                                      'padding': '0px 0px 5px 5px'},
                                        ),
                                             
                        html.Div([
                            dcc.Graph(id='gráfica-scatter2'),
                                     ], style={'display': 'inline-block', 'float': 'right',
                                             'width': '40%'}
                                       ),
                                     
                        html.Div([
                            dcc.Graph(id='gráfica-bar2'),
                                     ], style={'display': 'inline-block', 'float': 'right',
                                             'width': '12%'}
                                      ),                                                                               
                                             
                                 ]), 
                                     
                        html.P(id="permisos-imagenes",
                            children= "Logos tomados de: Chris Creamer's Sports Logos Page - SportsLogos.Net, \
                                       https://www.sportslogos.net, \
                                       Copyright ©1997-2020 Chris Creamer.\
                                       Imagenes de jugadores tomados de: FantasyPros.com © Copyright 2010-2020 \
                                       https://www.fantasypros.com/mlb/compare/\
                                       All logos and images are the trademark & property of their owners. \
                                       We present them here for purely educational purposes.",
                                       style={'fontSize': 11,
                                              'width': '98%', 
                                              'display': 'block',
                                              'padding': '150px 5px 5px 5px',
                                                     },  
                                ),
                                                                       
                                     
                            ]),
                                                                                                              
        #Tab Glosario    
            dcc.Tab(label='Glosario', children=[                           
                html.Div([
                    html.H3('Glosario'),
                        dash_table.DataTable(
                                    data=dfglo.to_dict('records'),
                                    columns=[
                                            {"name": ["Abreviatura"], "id": "Abreviatura"},
                                            {"name": ["Definición"], "id": "Definición"},
                                             ],
                                                      
                                    fixed_rows={'headers': True},
                                             
                                    style_table={'height': '600px', 
                                                 'overflowY': 'auto',
                                                 'overflowX': 'auto'},
                                                           
                                    style_cell={'whiteSpace': 'normal', 
                                                'height': 'auto',
                                                'fontSize': 14,
                                                'textAlign': 'left'},
                                                          
                                    style_header={'backgroundColor': '#191970',
                                                  'border': '2px solid #cd4f39',
                                                  'fontSize': 16,
                                                  'color': 'white'},
                                                           
                                    style_cell_conditional=[
                                                    {'if': {'column_id': 'Abreviatura'},
                                                           'width': '10%'},
                                                    {'if': {'column_id': 'Definición'},
                                                            'width': '90%'},
                                                     {'if': {'row_index': 'odd'},
                                                            'backgroundColor': 'rgb(248, 248, 248)'},
                                                       ],
                                                           
                                              ),
                                                                                               
                                ], style={'width': '100%', 
                                          'display': 'block',
                                          'padding': '5px 5px 5px 5px',
                                                      }
                            ),                                                                                            
                    ]),                                                                                                                       
            ]),
       ]),
])


#Imagenes Bateadores
@app.callback(
        dash.dependencies.Output('img-bat1', 'src'),
        [dash.dependencies.Input("filtro-bateador1", "value")])

def update_image_bat1(bateador):
    image_name = '{}.jpg'.format(bateador)
    return app.get_asset_url(image_name)
                                                       

@app.callback(
        dash.dependencies.Output('img-bat2', 'src'),
        [dash.dependencies.Input("filtro-bateador2", "value")])

def update_image_bat2(bateador):
    image_name = '{}.jpg'.format(bateador)
    return app.get_asset_url(image_name)


#Tablas Bateadores
@app.callback(
        dash.dependencies.Output('bateador1', 'data'),
        [dash.dependencies.Input("filtro-bateador1", "value")])

def render_tablabat1(filtro_tabla1):

    dftabla1 = dfbat[(dfbat['Nombre'] == filtro_tabla1)] 
    return dftabla1.to_dict(orient='records')

@app.callback(
        dash.dependencies.Output('bateador2', 'data'),
        [dash.dependencies.Input("filtro-bateador2", "value")])

def render_tablabat2(filtro_tabla2):

    dftabla2 = dfbat[(dfbat['Nombre'] == filtro_tabla2)] 
    return dftabla2.to_dict(orient='records')
 
#Gráfica de Líneas
@app.callback(
    dash.dependencies.Output('gráfica-scatter', 'figure'),
    [dash.dependencies.Input('filtro-bateador1', 'value'),
    dash.dependencies.Input('filtro-bateador2', 'value')])
                
def crear_grafica_bateador(data_filtro1, data_filtro2):
    dfbatone = dfbat.copy()
    index_equipo = dfbatone[(dfbatone['Atributo'] == 'Equipo') ].index
    index_BA = dfbatone[(dfbatone['Atributo'] == 'BA') ].index
    index_OPS = dfbatone[(dfbatone['Atributo'] == 'OPS') ].index

    dfbatone.drop(index_equipo, inplace=True)
    dfbatone.drop(index_BA, inplace=True)
    dfbatone.drop(index_OPS, inplace=True)
    
    df2bat = dfbatone[dfbatone['Nombre'] == data_filtro1]
    df3bat = dfbatone[dfbatone['Nombre'] == data_filtro2]
    
    trace1 = go.Scatter(x = df2bat['Atributo'],
                        y = df2bat['Valor'], 
                        name = data_filtro1,
                        showlegend = False,
                        line = dict(width = 2, color = 'navy')
                        )
    
    trace2 = go.Scatter(x = df3bat['Atributo'], 
                        y = df3bat['Valor'], 
                        name = data_filtro2,
                        showlegend = False,
                        line = dict(width = 2, color = 'crimson')
                        )
    return {
        'data': [trace1, trace2],
        'layout': {
            'yaxis' : {'gridwidth': 1, 'gridcolor':'Lightblue'},
            'height':400,
            'margin': {'l': 40, 'b': 30, 'r': 0, 't': 10},}
           }

#Gráfica de Barras
@app.callback(
    dash.dependencies.Output('gráfica-bar', 'figure'),
    [dash.dependencies.Input('filtro-bateador1', 'value'),
    dash.dependencies.Input('filtro-bateador2', 'value')])
                
def crear_grafica_bateador2(data_filtro1, data_filtro2):
    dfbatwo = dfbat.copy()
    BA = dfbatwo[dfbatwo['Atributo'] == 'BA']
    OPS = dfbatwo[dfbatwo['Atributo'] == 'OPS']

    dfbatwo = pd.concat([BA, OPS])
   
    df2bat = dfbatwo[dfbatwo['Nombre'] == data_filtro1]
    df3bat = dfbatwo[dfbatwo['Nombre'] == data_filtro2]
    
    trace1 = go.Bar(x = df2bat['Atributo'],
                    y = df2bat['Valor'], 
                    name = data_filtro1,
                    showlegend = False,
                    opacity= 0.8,
                    marker = {'color':'navy'}
                    )
    
    trace2 = go.Bar(x = df3bat['Atributo'], 
                    y = df3bat['Valor'], 
                    name = data_filtro2,
                    showlegend = False,
                    opacity= 0.8,
                    marker = {'color':'crimson'}
                    )
    
    return {
        'data': [trace1, trace2],
        'layout': {
            'yaxis' : {'gridwidth': 0.5, 'gridcolor':'Lightblue'},
            'height':400,
            'margin': {'l': 20, 'b': 30, 'r': 0, 't': 10},}
           }

#Imagenes Pitchers
@app.callback(
        dash.dependencies.Output('img-pitch1', 'src'),
        [dash.dependencies.Input("filtro-pitcher1", "value")])

def update_image_pitch1(pitcher):
    image_name = '{}.jpg'.format(pitcher)
    return app.get_asset_url(image_name)
                                                       

@app.callback(
        dash.dependencies.Output('img-pitch2', 'src'),
        [dash.dependencies.Input("filtro-pitcher2", "value")])

def update_image_pitch2(pitcher):
    image_name = '{}.jpg'.format(pitcher)
    return app.get_asset_url(image_name)


#Tablas Pitchers
@app.callback(
        dash.dependencies.Output('pitcher1', 'data'),
        [dash.dependencies.Input("filtro-pitcher1", "value")])

def render_tablapicth1(filtro_tabla1):

    dftabla1 = dfpitch[(dfpitch['Nombre'] == filtro_tabla1)] 
    return dftabla1.to_dict(orient='records')

@app.callback(
        dash.dependencies.Output('pitcher2', 'data'),
        [dash.dependencies.Input("filtro-pitcher2", "value")])

def render_tablapitch2(filtro_tabla2):

    dftabla2 = dfpitch[(dfpitch['Nombre'] == filtro_tabla2)] 
    return dftabla2.to_dict(orient='records')
 
#Gráfica de Líneas
@app.callback(
    dash.dependencies.Output('gráfica-scatter2', 'figure'),
    [dash.dependencies.Input('filtro-pitcher1', 'value'),
    dash.dependencies.Input('filtro-pitcher2', 'value')])
                
def crear_grafica_pitcher(data_filtro1, data_filtro2):
    dfpitchone = dfpitch.copy()
    index_equipo = dfpitchone[(dfpitchone['Atributo'] == 'Equipo') ].index
    index_ERA = dfpitchone[(dfpitchone['Atributo'] == 'ERA') ].index
    index_WHIP = dfpitchone[(dfpitchone['Atributo'] == 'WHIP') ].index

    dfpitchone.drop(index_equipo, inplace=True)
    dfpitchone.drop(index_ERA, inplace=True)
    dfpitchone.drop(index_WHIP, inplace=True)
    
    df2pitch = dfpitchone[dfpitchone['Nombre'] == data_filtro1]
    df3pitch = dfpitchone[dfpitchone['Nombre'] == data_filtro2]
    
    trace3 = go.Scatter(x = df2pitch['Atributo'],
                        y = df2pitch['Valor'], 
                        name = data_filtro1,
                        showlegend = False,
                        line = dict(width = 2, color = 'navy')
                        )
    
    trace4 = go.Scatter(x = df3pitch['Atributo'], 
                        y = df3pitch['Valor'], 
                        name = data_filtro2,
                        showlegend = False,
                        line = dict(width = 2, color = 'crimson')
                        )
    return {
        'data': [trace3, trace4],
        'layout': {
            'yaxis' : {'gridwidth': 1, 'gridcolor':'Lightblue'},
            'height':400,
            'margin': {'l': 40, 'b': 30, 'r': 0, 't': 10},}
           }

#Gráfica de Barras
@app.callback(
    dash.dependencies.Output('gráfica-bar2', 'figure'),
    [dash.dependencies.Input('filtro-pitcher1', 'value'),
    dash.dependencies.Input('filtro-pitcher2', 'value')])
                
def crear_grafica_pitcher2(data_filtro1, data_filtro2):
    dfpitchtwo = dfpitch.copy()
    ERA = dfpitchtwo[dfpitchtwo['Atributo'] == 'ERA']
    WHIP = dfpitchtwo[dfpitchtwo['Atributo'] == 'WHIP']

    dfpitchtwo = pd.concat([ERA, WHIP])
   
    df2pitch = dfpitchtwo[dfpitchtwo['Nombre'] == data_filtro1]
    df3pitch = dfpitchtwo[dfpitchtwo['Nombre'] == data_filtro2]
    
    trace3 = go.Bar(x = df2pitch['Atributo'],
                    y = df2pitch['Valor'], 
                    name = data_filtro1,
                    showlegend = False,
                    opacity= 0.8,
                    marker = {'color':'navy'}
                    )
    
    trace4 = go.Bar(x = df3pitch['Atributo'], 
                    y = df3pitch['Valor'], 
                    name = data_filtro2,
                    showlegend = False,
                    opacity= 0.8,
                    marker = {'color':'crimson'}
                    )
    
    return {
        'data': [trace3, trace4],
        'layout': {
            'yaxis' : {'gridwidth': 0.5, 'gridcolor':'Lightblue'},
            'height':400,
            'margin': {'l': 20, 'b': 30, 'r': 0, 't': 10},}
           }
                                 
"""Run App"""

if __name__ == "__main__":
    app.run_server(debug=True, threaded=True) 
