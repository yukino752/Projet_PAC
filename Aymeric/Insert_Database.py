import mysql.connector 

############ Fonction pour la connexion à la base de données ############

"""
connectDB(): mysql.connector.connect()
"""

def connectDB (): 
    db = mysql.connector.connect( 
        host="localhost", 
        user="root",
        database="BDD_PAC" )
    return db

#########################################################################################################
############ Fonction pour insérer les valeurs reçu de l'elève 2 avec le capteur Compresseur ############

"""
Compresseur(V): mysql.connector.connect()
"""

def Compresseur(Valeur, id_capteur, id_releve):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur))
    conn.commit()

#########################################################################################################
############ Fonction pour insérer les valeurs reçu de l'elève 2 avec le capteur Condenseur ############

def Condenseur (Valeur, id_capteur, id_releve):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur))
    conn.commit()

#########################################################################################################
############ Fonction pour insérer les valeurs reçu de l'elève 2 avec le capteur Detendeur ############

def Detendeur (Valeur, id_capteur, id_releve):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur))
    conn.commit()

#########################################################################################################
############ Fonction pour insérer les valeurs reçu de l'elève 2 avec le capteur Evaporateur ############

def Evaporateur (Valeur, id_capteur, id_releve):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur))
    conn.commit()

#########################################################################################################
############ Fonction pour insérer les valeurs reçu de l'elève 2 avec le capteur de l'eau ############

def Eau (Valeur, id_capteur, id_releve):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur))
    conn.commit()

#########################################################################################################
############ Fonction pour insérer le releve avec la date ############

def Releve():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO releve (date) VALUES (CURRENT_TIMESTAMP);")
    conn.commit()

#########################################################################################################

"""
TempEntree = 10.2
TempSortie = 10.1
TempAvant = 10.6
TempApres = 18
HautePression = 18
BassePression = 9
Volt1 = 8
Ampere1 = 6

Valeur = 18
id_capteur = 4
id_releve = 2

Detendeur(Valeur, id_capteur, id_releve)
Releve()


if id_capteur == 4:
    Compresseur(Valeur, id_capteur, id_releve)
"""