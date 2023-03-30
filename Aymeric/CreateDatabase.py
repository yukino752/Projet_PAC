import mysql.connector 

############ Création de la fonction pour se connecter à la bdd ############
def connectDB (): 
    db = mysql.connector.connect( 
        host="localhost", 
        user="root",
        database="BDD_PAC" )
    return db

#########################################################################################################
############ Création de la base de données avec ces différentes tables ############

def Create_Table ():
    conn = connectDB() #conn récupère les données pour se connecter à la base de donnée
    cursor = conn.cursor() #conn.cursor() permet de se connecter à la base de donnée 
                           #et de pouvoir effectuer les requêtes mysql
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS validite (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        Minimum FLOAT,
                        Maximum FLOAT
                    );""") #Requête pour créer la table validite
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS capteur (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        nom_Capteur VARCHAR(50),
                        point_mesure INTEGER,
                        unite VARCHAR(50),
                        fk_validite INTEGER,
                        FOREIGN KEY (fk_validite) REFERENCES validite (id)
                    );""") #Requête pour créer la table capteur
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS releve (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );""") #Requête pour créer la table releve
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS mesure (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        fk_id_releve INTEGER,
                        fk_id_capteur INTEGER,
                        valeur FLOAT,
                        FOREIGN KEY (fk_id_releve) REFERENCES releve (id),
                        FOREIGN KEY (fk_id_capteur) REFERENCES capteur (id)
                    );""") #Requête pour créer la table mesure
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS central_acquisition (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        periodicite INTEGER,
                        nb_tentative INTEGER,
                        delai_expiration INTEGER
                    );""") #Requête pour créer la table central_acquisition
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS pac (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        mode VARCHAR(50),
                        type_fluide VARCHAR(50)
                    );""") #Requête pour créer la table pac
    conn.commit() #Fonction commit() qui permet de valider les modifications apportées ci-dessus

#########################################################################################################