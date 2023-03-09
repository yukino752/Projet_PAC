import sqlalchemy
import pandas
import dash
from sqlalchemy import create_engine
from dash import Dash, dash_table, dcc, html
import mysql.connector
import pandas as pd
from dash import Dash, dash_table
from mysql.connector import errorcode
from collections import OrderedDict


app = Dash(__name__)

app.title = "PAC_Dashboard"


def connectDB():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty123",
            database="test"
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
    return cursor, conn


cur, conn = connectDB()

# CREATION DU FICHIER CSV

num = OrderedDict(
    [
        ("N°", ["1", "2", "3", "4", "5", "6", "7"]),
    ]
)


dfNum = pd.DataFrame(num)

Capteur = OrderedDict([("capteur",
                        ["Compresseur",
                         "Condensateur",
                         "Eau",
                         "Ventilateur",
                         "Détendeur",
                         "Courant",
                         "Tension"]),
                       ])

dfCapteur = pd.DataFrame(Capteur)

FusiondfNumdfCapteur = pd.concat([dfNum, dfCapteur], axis=1)


def sql_query(query, conn):
    return pd.read_sql_query(query, conn)


query = "SELECT p.HautePression as 'Haute Pression' , p.BassePression as 'Basse Pression' , t.Entree as 'Temperature Entrée' , t.Sortie as 'Temperature Sortie'  FROM pressioncompresseur p INNER JOIN tempcompresseur t ORDER BY idPC DESC LIMIT 1; "
query2 = "SELECT Entree as 'Temperature Entrée' , Sortie as 'Temperature Sortie'  FROM tempcondenseur ORDER BY idTCD DESC LIMIT 1;"
query3 = "SELECT Entree as 'Temperature Entrée' , Sortie as 'Temperature Sortie'  FROM tempdetendeur ORDER BY idTD DESC LIMIT 1;"
query4 = "SELECT Entree as 'Temperature Entrée' , Sortie as 'Temperature Sortie'  FROM tempeau ORDER BY idTE DESC LIMIT 1;"
query5 = "SELECT Entree as 'Temperature Entrée' , Sortie as 'Temperature Sortie'  FROM tempventilateur ORDER BY idTV DESC LIMIT 1;"
query6 = "SELECT Volt  FROM Tension ORDER BY idT DESC LIMIT 1;"
query7 = "SELECT Intensite as 'Intensité'  FROM Courant ORDER BY idC DESC LIMIT 1;"

concatAllSQL = pd.concat(
    [
        sql_query(
            query, conn), sql_query(
                query2, conn), sql_query(
                    query3, conn), sql_query(
                        query4, conn), sql_query(
                            query5, conn), sql_query(
                                query6, conn), sql_query(
                                    query7, conn)])

concatAllSQL = concatAllSQL.reset_index(drop=True)

concatAllData = pd.concat([FusiondfNumdfCapteur, concatAllSQL], axis=1)

concatAllData.to_csv(r'C:\Users\kuro\PycharmProjects\pythonProject\file.csv')

df = pd.read_csv(

    r'C:\Users\kuro\PycharmProjects\pythonProject\file.csv',

    index_col=[0])


# Cleanup

conn.commit()

cur.close()

conn.close()


app.layout = html.Div([

    dash_table.DataTable(

        id='table',

        columns=[{"name": i, "id": i} for i in df.columns],

        data=df.to_dict('records')

    )



])


if __name__ == '__main__':

    app.run_server(debug=True)


"""

engine = create_engine("mysql://pierre:azerty@localhost/test")

source_connection = engine.connect()

df = pandas.read_sql("SELECT * FROM inventory", con=engine)

"""
