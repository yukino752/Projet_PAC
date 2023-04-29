import mysql.connector

def connectDB ():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="BDD_PAC" )
    return db

def QueryRequest(ID):
    conn = connectDB()  # conn récupère les données pour se connecter à la base de donnée
    cursor = conn.cursor()  # conn.cursor() permet de se connecter à la base de donnée
    cursor.execute(
        "SELECT m.valeur FROM  mesure m LEFT JOIN capteur c ON m.fk_id_capteur = c.id where m.fk_id_capteur = " +
        str(ID) +
        " ORDER BY m.id DESC LIMIT 1;")
    #Cette méthode récupère la ligne suivante d'un ensemble de résultats de requête et renvoie une séquence unique.Par défaut, le tuple retourné est constitué de données renvoyées par le serveur MySQL, converties en objets Python.
    res = cursor.fetchone()
    return res

def TupleToFloat(QueryRequest):
    res = QueryRequest
    res = float(res[0])
    return res

