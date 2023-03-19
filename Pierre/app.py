import dash
import dash_bootstrap_components as dbc
from dash import html, Dash, dcc, Input, Output
import mysql.connector
import pandas as pd
from mysql.connector import errorcode

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "PAC_Dashboard"

try:
    conn = mysql.connector.connect(
        host="host_name",
        user="username",
        password="password",
        database="database_name"
    )
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()


def QueryRequest(cursor, ID):
    cursor.execute(
        "SELECT m.valeur FROM  mesure m LEFT JOIN capteur c ON m.fk_id_capteur = c.id where m.fk_id_capteur = " +
        str(ID) +
        " ORDER BY m.id DESC LIMIT 1;")
    res = cursor.fetchone()
    return res


def TupleToInt(QueryRequest):
    res = QueryRequest
    res = float(res[0])
    return res


def ValueSchema():
    values = [
        html.P(str(TupleToInt(QueryRequest(cursor, 1))) + "bar",
               style={"z-index": "2", "position": "absolute", "right": "400px", "top": "363px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 2))) + "bar",
               style={"z-index": "2", "position": "absolute", "right": "463px", "top": "363px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 3))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "460px", "top": "249px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 4))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "403px", "top": "220px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 5))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "130px", "top": "130px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 6))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "275px", "top": "140px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 7))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "397px", "top": "530px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 8))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "475px", "top": "530px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 9))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "560px", "top": "313px"}),
        html.P(str(TupleToInt(QueryRequest(cursor, 10))) + "°C",
               style={"z-index": "2", "position": "absolute", "right": "112px", "top": "470px"}),
    ]

    return values


def generateTable():
    table_header = [html.Thead(html.Tr([html.Th("Désignation"), html.Th(
        "Point de mesures"), html.Th("Valeur"), html.Th("Unité")]))]

    row8 = html.Tr([html.Td("Sortie du detenteur (T6)"), html.Td(
        "6"), html.Td(QueryRequest(cursor, 8)), html.Td("°C")])
    row1 = html.Tr([html.Td("Haute Pression (HP)"), html.Td(
        "1"), html.Td(QueryRequest(cursor, 1)), html.Td("Bar")])
    row2 = html.Tr([html.Td("Basse Pression (BP)"), html.Td(
        "2"), html.Td(QueryRequest(cursor, 2)), html.Td("Bar")])
    row3 = html.Tr([html.Td("Entrée du compresseur (T1)"), html.Td(
        "1"), html.Td(QueryRequest(cursor, 3)), html.Td("°C")])
    row4 = html.Tr([html.Td("Sortie du compresseur (T2)"), html.Td(
        "2"), html.Td(QueryRequest(cursor, 4)), html.Td("°C")])
    row5 = html.Tr([html.Td("Entrée du condenseur (T3)"), html.Td(
        "3"), html.Td(QueryRequest(cursor, 5)), html.Td("°C")])
    row6 = html.Tr([html.Td("Sortie du condenseur (T4)"), html.Td(
        "4"), html.Td(QueryRequest(cursor, 6)), html.Td("°C")])
    row7 = html.Tr([html.Td("Entrée du detenteur (T5)"), html.Td(
        "5"), html.Td(QueryRequest(cursor, 7)), html.Td("°C")])
    row9 = html.Tr([html.Td("Sortie d'évaporateur (T7)"), html.Td(
        "7"), html.Td(QueryRequest(cursor, 9)), html.Td("°C")])
    row10 = html.Tr([html.Td("Bac d'eau (T8)"), html.Td(
        "8"), html.Td(QueryRequest(cursor, 10)), html.Td("°C")])

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
                      ])
app.layout = html.Div([body, dcc.Interval(
    id='interval-component', interval=1 * 10000, n_intervals=0), ])


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
"""
