### library required for dashboard

import plotly.graph_objects as go
import dash
import dash_html_components as html

app = dash.Dash()
server = app.server
### defining the HTML component

app.layout = html.Div([html.Div("Welcome to the dashboard", style= { "color": "white", "text-align": "center", "background-color": "blue",   "display":"block", 'font-size':'5vw', 'marginLeft': 100, 'marginRight': 100, 'marginTop': 30, 'marginBottom': 100, 'border': 'thin lightgrey dashed', 'padding':'10px 10px 10px 10px'}),
                       html.Div("Here is my first dashboard", style= { "color": "green", "text-align": "center", "background-color": "primary", "display":"block", 'font-size':'5vw', 'marginLeft': 100, 'marginRight':100, 'marginTop': 30, 'marginBottom': 100, 'border': 'thin lightgrey dashed', 'padding': '10px 10px 10px 10px'})])

if __name__ == '__main__':
    app.run_server(debug=True)
