import mysql.connector
from CreateDatabase import connectDB

#########################################################################################################
############ Fonction pour insérer les valeurs reçu de l'elève 2 avec le capteur Compresseur ############

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
############ Trigger ############

#def Trigger():
#    conn = connectDB()
#    cursor = conn.cursor()
#    cursor.execute ("""
#                    CREATE TRIGGER test_trigger 
#                    ON Mesure AFTER INSERT
#                    AS BEGIN
#                    print ("réussi") ; """)
#    conn.commit()

#Trigger()
"""
Valeur = 18
id_capteur = 4
id_releve = 2

Detendeur(Valeur, id_capteur, id_releve)
Releve()


if id_capteur == 4:
    Compresseur(None, id_capteur, id_releve)
"""