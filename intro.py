import dash
from dash import html

dash.register_page(__name__, path='/', name="Business-case", order = 1)

####################### PAGE LAYOUT #############################
layout = html.Div([
    html.Div(children=[
        html.H2("RFM Analyse Business Case"),
        """
        De Business Case is om klantrelaties te optimaliseren met behulp van een RFM-analyse. 
        Deze analyse segmenteert klanten op basis van Recency (hoe recent ze hebben gekocht), Frequency (hoe vaak ze kopen), 
        en Monetary (hoeveel ze uitgeven), waardoor we waardevolle inzichten verkrijgen in hun koopgedrag. 
        Deze inzichten zijn belangrijk voor het verhogen van klanttevredenheid, verbeteren van klantretentie, en maximaliseren van de omzet.
        """,
        html.Br(),
        """
        Het identificeren en analyseren van elk segment stelt ons in staat om gerichte strategieën 
        te ontwikkelen die aansluiten bij de behoeften en gedragingen van onze klanten. De Klanten zijn opgedeeld in vijf segmenten:
        """,
        html.Br(),
        html.B("Champions: "),
        "Klanten die recent hebben gekocht, frequent kopen en veel uitgeven. Beloon deze klanten met exclusieve aanbiedingen en VIP-voordelen om hun loyaliteit te behouden.",
        html.Br(),
        html.B("Potential Loyalists: "),
        "Klanten met een hoge koopfrequentie die recent zijn begonnen met kopen. Ontwikkel relaties via loyaliteitsprogramma's en aanbiedingen om hun loyaliteit te versterken.",
        html.Br(),
        html.B("At Risk Customers: "),
        "Klanten die veel hebben gekocht maar nu minder vaak kopen. Herstel de betrokkenheid met gepersonaliseerde communicatie en aanbiedingen om hun activiteit te reactiveren.",
        html.Br(),
        html.B("Can't Lose Them: "),
        "Klanten die vroeger vaak en veel kochten, maar wiens aankoopfrequentie is gedaald. Intensieve re-engagement campagnes zijn nodig om deze klanten te behouden.",
        html.Br(),
        html.B("Lost Customers: "),
        "Klanten die in het verleden actief waren maar nu gestopt zijn met kopen. Ontwikkel heractivatiecampagnes met speciale aanbiedingen om hun interesse te krijgen.",
        html.Br(),html.Br(),
        """
        De pagina "Overzicht Klantensegmenten", toont een visuele weergave van de klantenbasis verdeeld over de verschillende RFM-segmenten. 
        Daarbij is te zien wat de gemiddelde RFM-waarde zijn voor de klant segmenten. 
        Dit overzicht helpt ons snel te identificeren welke segmenten de meeste aandacht nodig hebben.
        """,
        html.Br(),
        """
        Op de tweede pagina, "Klantlevenscyclus Analyse", zien we in welke klantsegmenten de klanten over tijd zijn. 
        Met behulp van de filter is het mogelijk om te zien welke klant segmenten aanwezig zijn in welke geselecteerde periode.
        Via deze pagina is het makkelijker om te identificeren in welke periode er veel klanten verloren zijn."
        """,
        html.Br(),
        "De dataset voor deze analyse komt van: ",
        html.A("https://data.world/ehughes/superstore-sales-2023", 
               href="https://data.world/ehughes/superstore-sales-2023", 
               target="_blank"),
    ], className="bg-light p-4 m-2"),
])
