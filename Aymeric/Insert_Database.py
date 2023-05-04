import mysql.connector
from CreateDatabase import connectDB

def Compresseur(Valeur, id_capteur, id_releve):
    """
    Cette fonction ajoute une mesure de la valeur d'un capteur associé à un relevé dans la table 'mesure' de la base de données.
    :param Valeur: la valeur du capteur à ajouter
    :param id_capteur: l'ID du capteur
    :param id_releve: l'ID du relevé associé
    """
    conn = connectDB() # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur pour exécuter les requêtes SQL
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur)) # Exécution de la requête SQL pour ajouter une mesure
    conn.commit() # Validation des changements dans la base de données

def Condenseur (Valeur, id_capteur, id_releve):
    """
    Cette fonction ajoute une mesure de la valeur d'un capteur associé à un relevé dans la table 'mesure' de la base de données.
    :param Valeur: la valeur du capteur à ajouter
    :param id_capteur: l'ID du capteur
    :param id_releve: l'ID du relevé associé
    """
    conn = connectDB() # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur pour exécuter les requêtes SQL
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur)) # Exécution de la requête SQL pour ajouter une mesure
    conn.commit() # Validation des changements dans la base de données

def Detendeur (Valeur, id_capteur, id_releve):
    """
    Cette fonction ajoute une mesure de la valeur d'un capteur associé à un relevé dans la table 'mesure' de la base de données.
    :param Valeur: la valeur du capteur à ajouter
    :param id_capteur: l'ID du capteur
    :param id_releve: l'ID du relevé associé
    """
    conn = connectDB() # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur pour exécuter les requêtes SQL
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (%s, %s, %s);", (id_releve, id_capteur, Valeur)) # Exécution de la requête SQL pour ajouter une mesure
    conn.commit() # Validation des changements dans la base de données

def Evaporateur (Valeur, id_capteur, id_releve):
    """
    Cette fonction ajoute une mesure de la valeur d'un capteur associé à un relevé dans la table 'mesure' de la base de données.
    :param Valeur: la valeur du capteur à ajouter
    :param id_capteur:


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