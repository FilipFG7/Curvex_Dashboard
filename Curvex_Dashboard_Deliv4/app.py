# importing the libraries
from ctypes import alignment
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from numpy import size  
import pandas as pd   
import plotly.express as px 
import pages_plugin
import dash_labs as dl
import dash_auth


# app creation in dash
app= dash.Dash(__name__, plugins=[dl.plugins.pages],external_stylesheets=[dbc.themes.LUX])

# create a login
auth = dash_auth.BasicAuth(
    app,
    {'Filip':'Gavalier',
     'Ryan':'Denzel'}
)


curvex_logo= "assets/curvexlogo.png"
# creating a dropdown for the pages
dropdown=dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                    if page["module"] != "pages.not_found_404"

                ],
                nav=True,
                label="More pages",
                in_navbar=True,
                
                
            )
# creating a responsive header for the webapp
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=curvex_logo, height="50px")),
                        
                        dbc.Col(dbc.NavbarBrand("Representation of data", className="ms-2", style={'fontSize':'200%', 'fontColor':'#F2F2F2'})),
                        
                    ],
                    align="center",
                    className="g-0",
                    
                ),
               
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="#262626",
    dark=True,
    className="mb-5",
    
)

# giving the app a layout - resposive header and page contents
app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)
        
# running webapp
if __name__ == '__main__':
    app.run_server(debug=True)

