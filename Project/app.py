# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

theme = ['/assets/custom.css']

app = Dash(__name__, external_stylesheets = theme)

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Sticky header
    html.Div([
        # Logo on the left
        html.A([html.Img(src='/assets/N_logo.png', id='logo'),], href='/home'),  
        html.Div(['NBA Stats', html.Br(), 'Analyzer'], id='header-text'),
        html.Img(src='/assets/bwade.png', id='silhouette')
    ], id='header'),

 html.Div(id='navbar', className='navbar', children=[
        html.Ul(children=[
            html.Li(html.A('Players', href='/players')),
            html.Li(html.A('Teams', href='/teams')),
            html.Li(html.A('Settings', href='/settings')),
            html.Li(html.A('About', href='/about')),
        ])
    ]),

html.Div(id='page-content', className='page-content'),

    # Rest of the content
    html.Div([
        # Your content goes here
        html.H1('Welcome to My Dash App'),
        html.H1('1'),
        html.H1('2'),
        html.H1('3'),
        html.H1('4'),
        html.H1('5'),
        html.H1('6')
    ]),
])

# Callback to update page content based on the URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/players':
        # Replace this with your Players content (text and table)
        return [
            html.H1('Players Page'),
            html.P('This is the Players page content.'),
            html.Table([
                # Your table content here
            ])
        ]
    elif pathname == '/teams':
        # Replace this with your Teams content (text and table)
        return [
            html.H1('Teams Page'),
            html.P('This is the Teams page content.'),
            html.Table([
                # Your table content here
            ])
        ]
    elif pathname == '/settings':
        # Replace this with your Settings content (text and table)
        return [
            html.H1('Settings Page'),
            html.P('This is the Settings page content.'),
            html.Table([
                # Your table content here
            ])
        ]
    elif pathname == '/about':
        # Replace this with your About content (text and table)
        return [
            html.H1('About Page'),
            html.P('This is the About page content.'),
            html.Table([
                # Your table content here
            ])
        ]
    else:
        # Default content for the home page
        return [
            html.H1('Home Page'),
            html.P('Welcome to the home page.'),
        ]
    
if __name__ == '__main__':
    app.run_server(debug=True)



