import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px

# Registreer de pagina met Dash (ervan uitgaande dat Dash multi-page support correct is ingesteld)
dash.register_page(__name__, path='/Klantlevenscyclus_Analyse', name="Klantlevenscyclus Analyse", order = 4)

# Data laden
df_orders = pd.read_csv("orders.csv")  # Ordergegevens
df_rfm = pd.read_csv("rfm_df.csv")  # RFM-gegevens

# Datumkolom converteren naar datetime
df_orders['Date Order was placed'] = pd.to_datetime(df_orders['Date Order was placed'], format='%d-%b-%y')

# Vind de laatste orderdatum voor elk CustomerID
last_order_dates = df_orders.groupby('CustomerID')['Date Order was placed'].max().reset_index()

# Combineer de gegevens op basis van CustomerID en de laatste orderdatum
df_combined = pd.merge(last_order_dates, df_rfm, on='CustomerID')

# Definieer de minimale en maximale datums voor de RangeSlider
min_date = df_combined['Date Order was placed'].min()
max_date = df_combined['Date Order was placed'].max()

# Zet de datums om naar timestamps voor de RangeSlider
min_date_ts = int(min_date.timestamp())
max_date_ts = int(max_date.timestamp())

# Layout aanpassing om de geselecteerde periode weer te geven
layout = html.Div([
    html.H1("Klantlevenscyclus Analyse"),
    html.Label("Selecteer een periode:"),
    dcc.RangeSlider(
        id='date-slider',
        min=min_date_ts,
        max=max_date_ts,
        marks={min_date_ts: min_date.strftime('%Y-%m-%d'),
               max_date_ts: max_date.strftime('%Y-%m-%d')},
        value=[min_date_ts, max_date_ts]
    ),
    html.Div(id='slider-output-container'),  # Container voor de slider output
    dcc.Graph(id='customer-lifecycle-graph')
])

# Callback voor het bijwerken van de grafiek
@callback(
    Output('customer-lifecycle-graph', 'figure'),
    Input('date-slider', 'value')
)
def update_customer_lifecycle_graph(date_range):
    start_date = pd.to_datetime(date_range[0], unit='s')
    end_date = pd.to_datetime(date_range[1], unit='s')
    
    filtered_data = df_combined[(df_combined['Date Order was placed'] >= start_date) &
                                (df_combined['Date Order was placed'] <= end_date)]

    fig = px.histogram(filtered_data, x='RFM Customer Segments', color='RFM Customer Segments',
                       title="Klantlevenscyclus Analyse",
                       labels={'RFM Customer Segments': 'RFM Segment', 'count': 'Aantal Klanten'})

    return fig

# Nieuwe callback om de slider-output-container te updaten
@callback(
    Output('slider-output-container', 'children'),
    Input('date-slider', 'value')
)
def update_output(value):
    start_date = pd.to_datetime(value[0], unit='s').strftime('%Y-%m-%d')
    end_date = pd.to_datetime(value[1], unit='s').strftime('%Y-%m-%d')
    return f"Geselecteerde periode: {start_date} tot {end_date}"


