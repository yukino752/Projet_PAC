import dash
import dash_bootstrap_components as dbc
from dash import html, Dash, dcc, Input, Output
import mysql.connector
import pandas as pd
from mysql.connector import errorcode
from DB import QueryRequest, TupleToFloat
from enthalpique import DiagrammeEnthalpie

# Utilisation Bootstrap stylesheets pour customiser le site
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# Nom de page WEB
app.title = "PAC_Dashboard"


DIA = DiagrammeEnthalpie()
DIA.creer_diagramme()
# On positionne les mesures sur le schéma de PAC

def ValeurSchema():
    """
    Cette fonction récupère des valeurs de mesure à partir d'une requête SQL et les place dans une liste d'éléments HTML
    correspondant à des paragraphes contenant la valeur de mesure et une classe CSS associée.

    Returns:
        list: Une liste d'éléments HTML représentant les valeurs de mesure.
    """
    # Récupération des valeurs de mesure à partir de la base de données via une requête SQL.
    hp = TupleToFloat(QueryRequest(1))  # pression haute pression
    bp = TupleToFloat(QueryRequest(2))  # pression basse pression
    ecp = TupleToFloat(QueryRequest(3))  # Entrée du compresseur
    scp = TupleToFloat(QueryRequest(4))  # Sortie du compresseur
    ecd = TupleToFloat(QueryRequest(5))  # Entrée du condenseur
    scd = TupleToFloat(QueryRequest(6))  # Sortie du condenseur
    ed = TupleToFloat(QueryRequest(7))  # Entrée du detenteur
    sd = TupleToFloat(QueryRequest(8))  # Sortie du detenteur
    se = TupleToFloat(QueryRequest(9))  # Sortie d'évaporateur
    be = TupleToFloat(QueryRequest(10))  # Bac d'eau

    # Création d'une liste d'éléments HTML pour chaque mesure récupérée.
    valeurs = [
        html.P(str(hp) + "bar", className="HP_schema"),  # pression haute pression
        html.P(str(bp) + "bar", className="BP_schema"),  # pression basse pression
        html.P(str(ecp) + "°C", className="ECP_schema"),  # Entrée du compresseur
        html.P(str(scp) + "°C", className="SCP_schema"),  # Sortie du compresseur
        html.P(str(ecd) + "°C", className="ECD_schema"),  # Entrée du condenseur
        html.P(str(scd) + "°C", className="SCD_schema"),  # Sortie du condenseur
        html.P(str(ed) + "°C", className="ED_schema"),  # Entrée du detenteur
        html.P(str(sd) + "°C", className="SD_schema"),  # Sortie du detenteur
        html.P(str(se) + "°C", className="SE_schema"),  # Sortie d'évaporateur
        html.P(str(be) + "°C", className="BE_schema")  # Bac d'eau
    ]

    # Retourne la liste d'éléments HTML représentant les valeurs de mesure.
    return valeurs



def generateTable():
    # création de l'entête du tableau
    table_header = [html.Thead(html.Tr([html.Th("Désignation"), html.Th(
        "Point de mesures"), html.Th("Valeur"), html.Th("Unité")]))]
    # le contenu des lignes
    row8 = html.Tr([html.Td("Sortie du detenteur (T6)"), html.Td(
        "6"), html.Td(QueryRequest(8)), html.Td("°C")])
    row1 = html.Tr([html.Td("Haute Pression (HP)"), html.Td(
        "1"), html.Td(QueryRequest(1)), html.Td("Bar")])
    row2 = html.Tr([html.Td("Basse Pression (BP)"), html.Td(
        "2"), html.Td(QueryRequest(2)), html.Td("Bar")])
    row3 = html.Tr([html.Td("Entrée du compresseur (T1)"), html.Td(
        "1"), html.Td(QueryRequest(3)), html.Td("°C")])
    row4 = html.Tr([html.Td("Sortie du compresseur (T2)"), html.Td(
        "2"), html.Td(QueryRequest(4)), html.Td("°C")])
    row5 = html.Tr([html.Td("Entrée du condenseur (T3)"), html.Td(
        "3"), html.Td(QueryRequest(5)), html.Td("°C")])
    row6 = html.Tr([html.Td("Sortie du condenseur (T4)"), html.Td(
        "4"), html.Td(QueryRequest(6)), html.Td("°C")])
    row7 = html.Tr([html.Td("Entrée du detenteur (T5)"), html.Td(
        "5"), html.Td(QueryRequest(7)), html.Td("°C")])
    row9 = html.Tr([html.Td("Sortie d'évaporateur (T7)"), html.Td(
        "7"), html.Td(QueryRequest(9)), html.Td("°C")])
    row10 = html.Tr([html.Td("Bac d'eau (T8)"), html.Td(
        "8"), html.Td(QueryRequest(10)), html.Td("°C")])
    # on fusionne l'entête du tableau et les lignes du tableau
    table_body = [html.Tbody(
        [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10])]
    return dbc.Table(
        table_header +
        table_body,
        striped=True,
        hover=True,
        responsive=True,
    )


body = dbc.Container([dbc.Row([dbc.Col([html.H1("PAC Dashboard",
                                                className="Titre_page"),
                                        ],width=12,
                                       ),
                               ]),
                      dbc.Row([dbc.Col([html.Div(generateTable(),
                               id="table-data",
                                                 )],width=6
                                       ),
                               dbc.Col([html.Div(children=[html.Img(src=app.get_asset_url('schema.png'),
                                                                    className="image_schema"),
                                                           html.Div(ValeurSchema(),
                                                                    className="Tv_schema")])],width=6)]),
                      dbc.Row([dbc.Col([html.Img(src=app.get_asset_url('diagramme.png'),
                                                 )],width=12,
                                       ),
                               ]),
                      ])
# app.layout détermine la structure d'un tableau de bord et décrit
# l'aspect de l'application
app.layout = html.Div([body, dcc.Interval(
    id='interval-component', interval=1 * 10000, n_intervals=0), ])

# ce callback rafraichi les données du tableau de mesures


@app.callback(Output('table-data', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_table(interval):
    return generateTable()


if __name__ == '__main__':
    app.run_server(debug=True)
