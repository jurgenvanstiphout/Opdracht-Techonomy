import dash
from dash import html, dash_table, dcc
import pandas as pd
import plotly.graph_objects as go

# Registratie van de pagina met Dash
dash.register_page(__name__, path='/combined_distribution_and_scatter', name="Overzicht Klantensegmenten", order = 3)

# Het laden van de dataset uit een CSV-bestand
df = pd.read_csv("rfm_df.csv")

# Vervang komma's door punten in de 'Monetary' kolom en converteer naar float
df['Monetary'] = df['Monetary'].apply(lambda x: float(x.replace(',', '.')))

# Groepeer de data op 'RFM Customer Segments' en bereken het benodigde
aggregated_df = df.groupby('RFM Customer Segments').agg(
    Klant_Aantal=('CustomerID', 'count'),
    Gemiddelde_Frequentie=('Frequency', 'mean'),
    Gemiddelde_Monetary=('Monetary', 'mean'),
    Gemiddelde_Recency=('Recency', 'mean')
).reset_index()

# Bereken het totale aantal klanten
totaal_klanten = aggregated_df['Klant_Aantal'].sum()

# Bereken het percentage van het totaal voor elk segment
aggregated_df['Klant_Percentage'] = ((aggregated_df['Klant_Aantal'] / totaal_klanten) * 100).round(2).astype(str) + '%'

# Rond de gemiddelde waarden af
aggregated_df['Gemiddelde_Frequentie'] = aggregated_df['Gemiddelde_Frequentie'].round(2)
aggregated_df['Gemiddelde_Monetary'] = aggregated_df['Gemiddelde_Monetary'].round(2)
aggregated_df['Gemiddelde_Recency'] = aggregated_df['Gemiddelde_Recency'].round(0)

# Scatterplot maken
fig = go.Figure()
for segment in aggregated_df['RFM Customer Segments']:
    segment_df = aggregated_df[aggregated_df['RFM Customer Segments'] == segment]
    fig.add_trace(go.Scatter(
        x=segment_df['Gemiddelde_Monetary'],
        y=segment_df['Gemiddelde_Frequentie'],
        mode='markers',
        marker=dict(
            size=segment_df['Klant_Aantal'] * 3,  # Vergroot de marker grootte
            opacity=0.7,
            sizemode='area',
            sizeref=2.*max(aggregated_df['Klant_Aantal'])/(40.**2) / 3,
            sizemin=4
        ),
        name=segment
    ))

# Update scatterplot layout met Nederlandse labels
fig.update_layout(
    title="Gemiddelde Monetary vs Frequentie per RFM Klantsegment",
    xaxis_title="Gemiddelde Monetary (€)",
    yaxis_title="Gemiddelde Frequentie",
    legend_title="RFM Klantsegmenten"
)

# Combineer tabel en scatterplot in de layout met Nederlandse koppen
layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(
        id='table',
        columns=[
            {"name": "RFM Klantsegmenten", "id": "RFM Customer Segments"},
            {"name": "Aantal Klanten (%)", "id": "Klant_Percentage"},
            {"name": "Gemiddelde Frequentie", "id": "Gemiddelde_Frequentie"},
            {"name": "Gemiddelde Monetary (€)", "id": "Gemiddelde_Monetary"},
            {"name": "Gemiddelde Recency (Dagen)", "id": "Gemiddelde_Recency"},
        ],
        data=aggregated_df.to_dict('records'),
        page_size=len(aggregated_df),  # Toont alle rijen
        style_cell={'textAlign': 'left'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[]
    ),
    html.Br(),
    dcc.Graph(figure=fig)  # Voeg de scatterplot direct toe aan de layout
])
