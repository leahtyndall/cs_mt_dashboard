from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import layout.Funcs.defs as defs
import websockets
import dash_player
from shapely.geometry import Point, Polygon
import plotly.graph_objects as go
import layout.Funcs.missions as mis
import pandas as pd

COLOURS = { #CHANGE TO VODAFONE THEME + ADD LOGOS
    'red':"#A9002A",
    'white': "#FFFFFF",
    'backgnd': "#C0C0C0",
    'black':'#333333',
    'blue': "#005172",
    'green': '#136C5C',
    'yellow': "#C49824",
    'purple': '#674F71'
    #'red': "#C52620"
}
def updateP():
    with open('layout/assets/pistonStat.txt', 'rt') as f:
        p = f.read()
        #f.close()
    if p == '0':
        piston='#AF1D18'
    elif p == '1':
        piston ='#8FC78F'
    return piston

    #gate 
def updateG():
    with open('layout/assets/gateStat.txt', 'rt') as f:
        g = f.read()
        f.close()
    if g == '0':
        gate='#AF1D18'
    elif g == '1':
        gate='#8FC78F'
    return gate
    

    


df = pd.read_csv('layout/assets/PositionList.csv')
name = df['label']
#guid = df['value']

layout2 = html.Div(
    style = {'backgroundColor': COLOURS['backgnd'],'font-family':'Arial', 'font-size':'18px', 'line-height':'1','wdth':'100%', 'height':'100vh'}, children= [
        dcc.Tabs(style = {'height':'40px'}, children = [
            dcc.Tab(label='Dashboard 🤖', children=[
                dbc.Container([  
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('Mobile Robot',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
                                    'margin':'0px',
                                    'verticalAlign':'top'})
                        ]), width = 8),

                        dbc.Col(html.Div([ # r1c2
                            html.Img(src='assets/IMR-Primary Logo_RGB.png',
                                style ={'width': '100%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2),               
                        dbc.Col(html.Div([ #r1c3
                            html.Img(src='assets/coresense-logo.png',
                                style ={'width': '40%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2)

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }
                    ), #row1 close
                    #################################################################    
                    #LEFT COL         
                    #################################################################      
                            
                    dbc.Row([ #row 2 open                
                        dbc.Col(children = [ #r2c1
                            dbc.Row([ #inside r2c1
                                dbc.Col(html.Div([  #LEFT r2c1          
                                    html.H4('Robot Status:',
                                        style = {
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['green'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'}),

                                        html.Div(id= 'battery'),
                                        html.Div(id='time')],
                                    #other data in this block enter here
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '150px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }
                                )),
                                dbc.Col(children=[
                                    dbc.Row([
                                        dbc.Col(html.Div([ #r2c1c2 
                                            html.H4('Current State:', 
                                                style={
                                                    'color': COLOURS['white'],
                                                    'padding':'8px',
                                                    'backgroundColor': COLOURS['red'],
                                                    'borderRadius':'10px',
                                                    'margin':'5px',
                                                    'verticalAlign':'top',
                                                    'height':'40px'
                                                }
                                            ),
                                            #html.P('Executing: '),
                                            #html.P(id = 'status'),
                                            html.Div(id ='robotLocation')],
                                            style={
                                                'color': COLOURS['black'],
                                                'width':'100%',
                                                'padding':'10px',
                                                'backgroundColor': COLOURS['white'],
                                                'borderRadius':'10px',
                                                'margin':'10px',
                                                'verticalAlign':'top',
                                                'display': 'inline-block',
                                                'height': '150px',
                                                'box-shadow':'5px 5px 5px grey'
                                                }

                                        ))
                                    ]),

                                ],
                                        
                                )
                            ]),  

                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H3('Tasks:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['yellow'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top'
                                            }
                                    ),
                                    
                                            
                                    dcc.Button('Go to charger', id = 'charge', n_clicks = 0, style={'color':COLOURS['red'], 'outline':COLOURS['black']}), #1
                                    #--delivery missions--
                                    dcc.Button('Collect from B1', id = 'cfb1', n_clicks = 0, style={'color':COLOURS['black']}),#2
                                    dcc.Button('Deposit at B1',id = 'dab1', n_clicks = 0, style={'color':COLOURS['black']} ),#3
                                    dcc.Button('Collect from B2', id='cfb2', n_clicks = 0, style={'color':COLOURS['black']}),#4
                                    dcc.Button('Deposit at B2', id='dab2', n_clicks = 0, style={'color':COLOURS['black']}),#5
                                    dcc.Button('Left side of B2', id ='b2LEFT', n_clicks = 0, style={'color':COLOURS['black']}),#6
                                    #-===--Temporary-----
                                    dcc.Button('Pick', id='pick', n_clicks = 0, style={'color':COLOURS['black']}),#7
                                    dcc.Button('Place', id='place', n_clicks = 0, style={'color':COLOURS['black']}),#7
                                    #-------------------
                                    dcc.Button('Refresh List', id ='refresh', n_clicks = 0, style={'color':COLOURS['red']}),#8
                                    dcc.Button('Clear Queue', id ='clear', n_clicks = 0, style={'color':COLOURS['red']}),#9


                                    html.Div(id ='container', children = '')], 
    
                                    

                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }
                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H3('Other Locations:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['blue'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top'
                                            }
                                    ),
                                    
                                    dcc.Dropdown(name, id ='posList'),
                                    dcc.Button('Submit', id = 'submit', n_clicks = 0),
                                    html.Div(id='ddOutput')       
                                ], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }
                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([ #col 3
                                    html.H3('Errors: ',
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['green'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top'
                                            }
                                    ),

                                    html.P(id = 'errors')],

                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                        }
                                    


                                ))


                            ])
                            
                        ]),
                    #################################################################    
                    #map
                    #################################################################            
                        dbc.Col( #r2c2 MAP
                            html.Div([ 
                                html.Img(src = "http://192.168.30.90:8080/stream?topic=/camera/camera/color/image_raw",
                                         #http://192.168.30.109:8080/stream?topic=/camera/camera/color/image_raw
                                         #'http://192.168.30.102:8080/stream?topic=/riskam/annotated_image',
                                    #src='http://192.168.30.102:8080/stream?topic=/image_raw&type=ros_compressed', 
                                    style={'width': '100%',
                                        'width': '100%',
                                        'padding':'10px',
                                        'backgroundColor': COLOURS['purple'],
                                        'borderRadius':'10px',
                                        'margin':'10px',
                                        'verticalAlign':'top',
                                        'display': 'inline-block',
                                        'box-shadow':'5px 5px 5px grey'})])
                        ) #r2c2 close

                    ]),
                ]),

            ]),
############################################################################################  
# TAB 2
############################################################################################ 
            dcc.Tab(label='Info 📊', children=[
                dbc.Container([  
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('Mobile Robot',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
                                    'margin':'0px',
                                    'verticalAlign':'top'})
                        ]), width = 8),

                        dbc.Col(html.Div([ # r1c2
                            html.Img(src='assets/IMR-Primary Logo_RGB.png',
                                style ={'width': '100%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2),               
                        dbc.Col(html.Div([ #r1c3
                            html.Img(src='assets/coresense-logo.png',
                                style ={'width': '40%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2)

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }

                    ), #row1 close
                    #fine^
                    #################################################################    
                    #LEFT COL         
                    #################################################################      
                            
                    dbc.Row([ #row 2 open                
                        dbc.Col( #r2c1
                            dbc.Row([ #inside r2c1
                                dbc.Col(html.Div([  #LEFT r2c1          
                                    html.P('Status response:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px',
                                            }),
                                    #html.P('Executing: '),
                                    html.P(id = 'latency')],
                                    #html.P(id = '')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '140px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                   #other data in this block enter here

                                )),

                                dbc.Col(html.Div([ #r2c1c2 
                                    html.P('Average stream rate: ', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['blue'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'}),
                                    #html.P('Executing: '),
                                    html.P(id = 'fps'),
                                    html.P(id = 'actualfps')],
                                    #html.P('Delay: ~4-5ms')],
                                    #html.P(id = '')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }  
                                    

                                )),
                            
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.P('Task response: ', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['green'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'
                                        }
                                    ),
                                    #html.P('Executing: '),
                                    html.P(id = 'taskLatency'),
                                    html.P('')],

                                         style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }           
                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([ #col 3
                                    html.P('Network:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['yellow'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'
                                        }
                                    ),
                                        html.Div(id = 'signallevel')],
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                        }    
                                ))


                            ])
                            ])
                        ),
                    #################################################################    
                    #RIGHT COL         
                    #################################################################            
                        dbc.Col( #r2c2 MAP
                            html.Div([ 
                                dcc.Graph(id='plot'),
                                
                            ])
                        ) #r2c2 close

                
                    ]),
        

                ]),


            ]),#row 5
            dcc.Tab(label='Project Summary 🎯',children =[
                dbc.Container([
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('Mobile Robot',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
                                    'margin':'0px',
                                    'verticalAlign':'top'})
                        ]), width = 8),

                        dbc.Col(html.Div([ # r1c2
                            html.Img(src='assets/IMR-Primary Logo_RGB.png',
                                style ={'width': '100%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2),               
                        dbc.Col(html.Div([ #r1c3
                            html.Img(src='assets/coresense-logo.png',
                                style ={'width': '40%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2)

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }

                    ), #row1 close
                    #################################################################    
                    #LEFT COL         
                    #################################################################      
                            
                    dbc.Row([ #row 2 open                
                        dbc.Col( #r2c1
                            dbc.Row([ #inside r2c1
                                dbc.Col(html.Div([  #LEFT r2c1          
                                    html.H2('Overview', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'width':'14%',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            #'verticalAlign':'top',
                                            'height':'50px'}),
                                    #html.P('Executing: '),
                                    html.P('')],
                                    #html.P(id = '')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'98%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin-top':'20px',
                                            'verticalAlign':'top',
                                            'word-spacing':'3px',
                                            'line-height':'1.3',
                                            'display': 'inline-block',
                                            'height': '220px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                   #other data in this block enter here

                                )),

                                
                            
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H2('Network', 
                                        style={
                                            'width':'12%',
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['yellow'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'height':'50px'}),
                                    html.P('')],
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin-top':'20px',
                                            'verticalAlign':'top',
                                            'word-spacing':'3px',
                                            'line-height':'1.3',
                                            'display': 'inline-block',
                                            'height': '200px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                 



                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H2('Robots in the Workplace', 
                                        style={
                                            'width':'31%',
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['green'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'height':'50px'}),
                                    html.P('')],
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin-top':'20px',
                                            'verticalAlign':'top',
                                            'word-spacing':'3px',
                                            'line-height':'1.3',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                 



                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([ #col 3

                                ]))


                            ])
                            ])
                        ),
                    #################################################################    
                    #RIGHT COL         
                    #################################################################            

                
                    ]),
        

                ]),
                ]),
                dcc.Tab(label='Rviz 🗺️', children=[
                dbc.Container([  
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('Mobile Robot',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
                                    'margin':'0px',
                                    'verticalAlign':'top'})
                        ]), width = 8),

                        dbc.Col(html.Div([ # r1c2
                            html.Img(src='assets/IMR-Primary Logo_RGB.png',
                                style ={'width': '100%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2),               
                        dbc.Col(html.Div([ #r1c3
                            html.Img(src='assets/coresense-logo.png',
                                style ={'width': '40%',
                                    'verticalAlign':'top', 
                                    'float':'right',
                                    'margin':'0px'})
                        ]), width = 2)

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }
                    ), #row1 close
                    #################################################################    
                    #       MAP BELOW HERE          
                    #################################################################      
                    dbc.Row([    
                        dbc.Col(
                            html.Div([
                                dcc.Graph(id='map', 
                                          style={'width': '600px', 'height': '600px'}),
                                html.Div(id='click-output')],
                                
                            )
                        )
                    ])

                    ]),
                ]),


            ]),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,
            n_intervals=0),

        dcc.Interval(id='interval-comp2', interval = 4*1000, n_intervals = 0),

        dcc.Store(id='browser-fps-store', data=0),
        dcc.Interval(id='fps-ticker', interval=1000, n_intervals=0)


])