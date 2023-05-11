import mysql.connector  # importer le module mysql.connector

def connectDB ():  # définir la fonction pour se connecter à la base de données
    db = mysql.connector.connect(  # se connecter à la base de données
        host="localhost",  # nom de l'hôte
        user="root",  # nom d'utilisateur de la base de données
        database="BDD_PAC"  # nom de la base de données
    )
    return db  # renvoyer la connexion

def Create_Table ():  # définir la fonction pour créer les tables dans la base de données
    conn = connectDB()  # se connecter à la base de données
    cursor = conn.cursor()  # obtenir un objet curseur pour exécuter des requêtes SQL
    cursor.execute ("""  # créer la table "validite" si elle n'existe pas déjà
                    CREATE TABLE IF NOT EXISTS validite (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        Minimum FLOAT,
                        Maximum FLOAT
                    );""") 
    cursor.execute ("""  # créer la table "capteur" si elle n'existe pas déjà
                    CREATE TABLE IF NOT EXISTS capteur (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        nom_Capteur VARCHAR(50),
                        point_mesure INTEGER,
                        unite VARCHAR(50),
                        fk_validite INTEGER,
                        FOREIGN KEY (fk_validite) REFERENCES validite (id)
                    );""") 
    cursor.execute ("""  # créer la table "releve" si elle n'existe pas déjà
                    CREATE TABLE IF NOT EXISTS releve (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );""") 
    cursor.execute ("""  # créer la table "mesure" si elle n'existe pas déjà
                    CREATE TABLE IF NOT EXISTS mesure (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        fk_id_releve INTEGER,
                        fk_id_capteur INTEGER,
                        valeur FLOAT,
                        FOREIGN KEY (fk_id_releve) REFERENCES releve (id),
                        FOREIGN KEY (fk_id_capteur) REFERENCES capteur (id)
                    );""") 
    cursor.execute ("""  # créer la table "central_acquisition" si elle n'existe pas déjà
                    CREATE TABLE IF NOT EXISTS central_acquisition (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        periodicite INTEGER,
                        nb_tentative INTEGER,
                        delai_expiration INTEGER
                    );""") 
    cursor.execute ("""  # créer la table "pac" si elle n'existe pas déjà
                    CREATE TABLE IF NOT EXISTS pac (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        mode VARCHAR(50),
                        type_fluide VARCHAR(50)
                    );""") 
    conn.commit()  # valider les modifications apportées à la base de données


#########################################################################################################