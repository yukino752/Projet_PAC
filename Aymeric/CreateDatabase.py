import mysql.connector 

############ Connection à la bdd ############

def connectDB (): 
    db = mysql.connector.connect( 
        host="localhost", 
        user="root",
        database="BDD_PAC" )
    return db

#########################################################################################################
############ Création de la base de données avec ces différentes tables ############

def Create_Table ():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS Validite (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        Minimum FLOAT,
                        Maximum FLOAT
                    );""")
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS Capteur (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        nom_Capteur VARCHAR(50),
                        point_mesure INTEGER,
                        unite VARCHAR(50),
                        fk_validite INTEGER,
                        FOREIGN KEY (fk_validite) REFERENCES Validite (id)
                    );""")
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS Releve (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );""")
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS Mesure (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        fk_id_releve INTEGER,
                        fk_id_capteur INTEGER,
                        valeur FLOAT,
                        FOREIGN KEY (fk_id_releve) REFERENCES Releve (id),
                        FOREIGN KEY (fk_id_capteur) REFERENCES Capteur (id)
                    );""")
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS Central_Acquisition (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        periodicite INTEGER,
                        nb_tentative INTEGER,
                        delai_expiration INTEGER
                    );""")
    cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS PAC (
                        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                        mode VARCHAR(50),
                        type_fluide VARCHAR(50)
                    );""")
    
    conn.commit()

#########################################################################################################

"""
Create_Table()
"""