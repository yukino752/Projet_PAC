import mysql.connector 

############ Connection à la bdd ############
def connectDB (): 
    db = mysql.connector.connect( 
        host="localhost", 
        user="root",
        database="BDD_PAC" )
    return db

#########################################################################################################
############ Selection de l'id du capteur qui permettra de remplir la table mesure de la bdd ############

def Select_id_Capteur(nom_Donnees):
    conn = connectDB()
    cursor = conn.cursor(buffered=True) #La raison en est que sans curseur tamponné, 
                                        #les résultats sont chargés "paresseusement", 
                                        # ce qui signifie que "fetchone" ne récupère en fait qu'une seule 
                                        # ligne de l'ensemble des résultats de la requête. 
                                        # Lorsque vous utiliserez à nouveau le même curseur, 
                                        # il se plaindra que vous avez encore n-1 résultats 
                                        # (où n est le nombre de résultats) en attente d'être récupérés. 
                                        # Cependant, lorsque vous utilisez un curseur tamponné, le 
                                        # connecteur récupère TOUTES les lignes en arrière-plan et 
                                        # vous n'en prenez qu'une du connecteur, 
                                        # de sorte que la base de données mysql ne se plaindra pas.
    cursor.execute ('SELECT id FROM Capteur WHERE nom_Capteur LIKE \'%' + nom_Donnees + '%\'');
    result = cursor.fetchone()
    id = result[0]
    conn.commit
    return id

#########################################################################################################
############ Selection de la validite pour que la central d'acquisition sache si la valeur est correct ############

def Select_validite(nom_Donnees):
    conn = connectDB()
    cursor = conn.cursor(buffered=True)
    cursor.execute ('SELECT validite.minimum, validite.maximum, capteur.nom_Capteur \
                   FROM validite \
                   INNER JOIN capteur ON validite.id = capteur.fk_validite WHERE nom_Capteur LIKE\'%' + nom_Donnees + '%\'');
    result = cursor.fetchall() # retourne un tableau contenant toutes les lignes du jeu d'enregistrements
    validite = result[0] # On facilite la recuperation de l'information pour l'eleve 2
    conn.commit
    return validite

#########################################################################################################
############ Selection du mode de la pac ############

def Select_mode (id_mode):
    conn = connectDB()
    cursor = conn.cursor(buffered=True)
    cursor.execute ('SELECT mode FROM pac WHERE id LIKE \'%' + str(id_mode) + '%\'');
    result = cursor.fetchone()
    mode = result[0]
    conn.commit
    return mode

#########################################################################################################

id_mode = 2
nom_Donnees = 'temperatureEntreeCompresseur'
id = Select_id_Capteur(nom_Donnees)
validite = Select_validite(nom_Donnees)
mode = Select_mode(id_mode)

print(id)
print(validite)
print(mode)