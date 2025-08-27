import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])


price_increase_date = pd.to_datetime("2021-01-15")
df["Period"] = df["date"].apply(
    lambda x: "Before" if x < price_increase_date else "After"
)


sales_summary = df.groupby("Period")["sales"].sum().reset_index()


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Before vs After Price Increase"),
    
    dcc.Graph(
        id="sales-comparison",
        figure=px.bar(
            sales_summary, 
            x="Period", 
            y="sales", 
            color="Period",
            title="Total Sales Before and After Price Increase"
        )
    )
])

if __name__ == "__main__":
    app.run(debug=True)
