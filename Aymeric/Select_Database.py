from CreateDatabase import connectDB

def Select_id_Capteur(Capteur):
    """
    Renvoie l'ID d'un capteur en fonction de son nom.
    Paramètres :
    -------------
    Capteur : str
        Nom du capteur dont on veut récupérer l'ID.
    Retour :
    --------
    id : int
        ID du capteur.
    """
    # Connexion à la base de données.
    conn = connectDB()
    cursor = conn.cursor(buffered=True)
    # Exécution de la requête SQL pour récupérer l'ID du capteur.
    cursor.execute ('SELECT id FROM Capteur WHERE nom_Capteur LIKE \'%' + Capteur + '%\'')
    result = cursor.fetchone()
    # Récupération de l'ID du capteur.
    id = result[0] 
    # Commit de la transaction et retour de l'ID du capteur.
    conn.commit()
    return id 



def Select_validite(Capteur):
    """
    Renvoie les limites de validité d'un capteur en fonction de son nom.
    Paramètres :
    -------------
    Capteur : str
        Nom du capteur dont on veut récupérer les limites de validité.
    Retour :
    --------
    validite_min : float
        Valeur minimale de validité du capteur.
    validite_max : float
        Valeur maximale de validité du capteur.
    """
    # Connexion à la base de données.
    conn = connectDB()
    cursor = conn.cursor(buffered=True)
    # Exécution de la requête SQL pour récupérer les limites de validité du capteur.
    cursor.execute ('SELECT validite.minimum, validite.maximum, capteur.nom_Capteur \
                   FROM validite \
                   INNER JOIN capteur ON validite.id = capteur.fk_validite WHERE nom_Capteur LIKE\'%' + Capteur + '%\'')
    result = cursor.fetchone()
    # Récupération des limites de validité du capteur.
    validite_min = result[0]
    validite_max = result[1] 
    # Commit de la transaction et retour des limites de validité du capteur.
    conn.commit()
    return validite_min, validite_max 



def Select_mode(id_mode):
    """
    Renvoie le mode d'un PAC en fonction de son ID.
    Paramètres :
    -------------
    id_mode : int
        ID du PAC dont on veut récupérer le mode.
    Retour :
    --------
    mode : str
        Mode du PAC.
    """
    # Connexion à la base de données.
    conn = connectDB()
    cursor = conn.cursor(buffered=True)
    # Exécution de la requête SQL pour récupérer le mode du PAC.
    cursor.execute ('SELECT mode FROM pac WHERE id LIKE \'%' + str(id_mode) + '%\'')
    result = cursor.fetchone() 
    # Récupération du mode du PAC.
    mode = result[0]
    # Commit de la transaction et retour du mode du PAC.
    conn.commit()
    return mode

def Select_periodicite():
    """
    Cette fonction sélectionne la périodicité depuis la table 'central_acquisition'.

    Returns:
        str: La périodicité récupérée depuis la base de données.
    """
    conn = connectDB()  # Établir la connexion à la base de données
    cursor = conn.cursor(buffered=True)  # Créer un curseur pour exécuter des requêtes SQL
    cursor.execute('SELECT periodicite FROM central_acquisition')  # Exécuter la requête SQL 
                                                                   #pour récupérer la périodicité
    result = cursor.fetchone()  # Récupérer le premier résultat de la requête
    periodicite = result[0]  # Extraire la périodicité de la première colonne du résultat
    conn.commit()  # Valider les modifications effectuées dans la base de données
    return periodicite  # Retourner la périodicité récupérée


#########################################################################################################





id_mode = 1
nom_Donnees = 'test'
id_capteur = Select_id_Capteur(nom_Donnees)
validite_min, validite_max = Select_validite(nom_Donnees)
mode = Select_mode(id_mode)

print(id_capteur)
print(validite_min)
print(validite_max)
print(mode)
