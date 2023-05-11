import mysql.connector


def connectDB():
    """
        Connecte à la base de données MySQL en utilisant les informations d'identification fournies.

        Returns:
            db (mysql.connector.connection_cext.CMySQLConnection): la connexion à la base de données.
        """
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="BDD_PAC")
    return db


def QueryRequest(ID):
    """
        Exécute une requête SELECT dans la base de données pour récupérer la valeur de la dernière mesure d'un capteur
        spécifié par son ID.

        Args:
            ID (int): l'ID du capteur.

        Returns:
            res (tuple): un tuple contenant la valeur de la dernière mesure récupérée.
        """
    conn = connectDB()  # conn récupère les données pour se connecter à la base de donnée
    cursor = conn.cursor()  # conn.cursor() permet de se connecter à la base de donnée
    cursor.execute(
        "SELECT m.valeur FROM  mesure m LEFT JOIN capteur c ON m.fk_id_capteur = c.id where m.fk_id_capteur = " +
        str(ID) +
        " ORDER BY m.id DESC LIMIT 1;")
    # Cette méthode récupère la ligne suivante d'un ensemble de résultats de
    # requête et renvoie une séquence unique.Par défaut, le tuple retourné est
    # constitué de données renvoyées par le serveur MySQL, converties en
    # objets Python.
    res = cursor.fetchone()
    return res


def TupleToFloat(QueryRequest):
    """
        Convertit la valeur de la dernière mesure récupérée (stockée dans un tuple) en un float.

        Args:
            QueryRequest (tuple): le tuple contenant la valeur de la dernière mesure.

        Returns:
            res (float): la valeur de la dernière mesure sous forme de float.
        """
    res = QueryRequest
    res = float(res[0])
    return res


