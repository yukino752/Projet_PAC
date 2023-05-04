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


def ValueSchema():
    values = [
        html.P(str(TupleToFloat(QueryRequest(1))) + "bar",
               style={"z-index": "2", "position": "absolute", "right": "400px", "top": "363px"}),
        html.P(str(TupleToFloat(QueryRequest(2))) + "bar",
               style={"z-index": "2", "position": "absolute", "right": "463px", "top": "363px"}),
        html.P(str(TupleToFloat(QueryRequest(3))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "460px", "top": "249px"}),
        html.P(str(TupleToFloat(QueryRequest(4))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "403px", "top": "220px"}),
        html.P(str(TupleToFloat(QueryRequest(5))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "130px", "top": "130px"}),
        html.P(str(TupleToFloat(QueryRequest(6))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "275px", "top": "140px"}),
        html.P(str(TupleToFloat(QueryRequest(7))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "397px", "top": "530px"}),
        html.P(str(TupleToFloat(QueryRequest(8))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "475px", "top": "530px"}),
        html.P(str(TupleToFloat(QueryRequest(9))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "560px", "top": "313px"}),
        html.P(str(TupleToFloat(QueryRequest(10))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "112px", "top": "470px"}),
    ]

    return values

# on génére le tableau de mesures


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
        style={
            "textAlign": "center",
            "width": "95%",
            "bottom": "0",
            "top": "0"})


body = dbc.Container([dbc.Row([dbc.Col([html.H1("PAC Dashboard",
                                                style={"color": "red",
                                                       "textAlign": "center"}),
                                        ],
                                       ),
                               ]),
                      dbc.Row([dbc.Col([html.Div(generateTable(),
                               id="table-data",
                               style={"margin-top": "35px",
                                       "z-index": "2"})],
                                       ),
                               dbc.Col([html.Img(src=app.get_asset_url('schema.png'),
                                                 style={"position": "absolute",
                                                        "top": "120px",
                                                        "right": "120px",
                                                        "z-index": "1"}),
                                        html.Div(ValueSchema(),
                                                 style={"color": "blue",
                                                        "font-size": "12px"})])]),
                      dbc.Row([dbc.Col([html.Img(src=app.get_asset_url('diagramme.png'),)],
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


"""

engine = create_engine("mysql://pierre:azerty@localhost/test")

source_connection = engine.connect()

df = pandas.read_sql("SELECT * FROM inventory", con=engine)
PASSTOKEN = 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
"""
