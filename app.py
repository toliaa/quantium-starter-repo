import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


df = pd.read_csv("output.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard", style={"textAlign": "center", "color": "#292d42"}),

    dcc.RadioItems(
        id="region_selector",
        options=[
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
            {"label": "All", "value": "all"}
        ],
        value="all",
        labelStyle={"display": "inline-block", "margin": "10px", "fontSize": "18px"}
    ),

    dcc.Graph(id="sales_chart", style={"height": "70vh"})
], style={"fontFamily": "Arial", "margin": "20px"})

@app.callback(
    Output("sales_chart", "figure"),
    Input("region_selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        color="region" if selected_region == "all" else None,
        title=f"Pink Morsel Sales ({selected_region.capitalize()})"
    )
    fig.update_layout(template="plotly_dark", title_x=0.5)
    return fig

if __name__ == "__main__":
    app.run(debug=True)
