import mysql.connector 

def connectDB (): 
    db = mysql.connector.connect( 
        host="localhost", 
        user="root",
        database="BDD_PAC" )
    return db

"""
def Compresseur (TempEntree=None, TempSortie=None, HautePression=None, BassePression=None):
    cur = connectDB()
    curso = cur.cursor()
    #if HautePression is None:
       #traitement défaut de haute pression
    curso.execute ("INSERT INTO donnees_recu (Temperature_Entree, Temperature_Sortie, Haute_Pression, Basse_Pression, Capteur_nom) VALUES (%s, %s, %s, %s, 'Compresseur');", (TempEntree, TempSortie, HautePression, BassePression))
    cur.commit()
"""
    
def Detendeur (Valeur, id_capteur, id_releve):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO mesure (fk_id_releve, fk_id_capteur, valeur) VALUES (1, %s, %s);", (id_capteur, Valeur))
    conn.commit()

"""
def Condenseur (cur, TempEntree, TempSortie):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Temperature_Entree, Temperature_Sortie, Capteur_nom) VALUES (%s, %s, 'Condenseur');", (TempEntree, TempSortie))
    cur.commit()

def Evaporateur (cur, TempEntree, TempSortie, nom_Capteur):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Temperature_Entree, Temperature_Sortie, Capteur_nom) VALUES (%s, %s, %s);", (TempEntree, TempSortie, nom_Capteur))
    cur.commit()

def Eau (cur, TempAvant, TempApres):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Temperature_Avant, Temperature_Apres, Capteur_nom) VALUES (%s, %s, 'Eau');", (TempAvant, TempApres))
    cur.commit()

def Tension (cur, Volt1, nom_Capteur):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Volt, Capteur_nom) VALUES (%s, %s);", (Volt1, nom_Capteur))
    cur.commit()

def Intensite (cur, Ampere1):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Ampere, Capteur_nom) VALUES ('" + str(Ampere1) + "', 'Intensite');")
    cur.commit()
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
id_capteur = 1
id_releve = 2

Detendeur(Valeur, id_capteur, id_releve)


"""
if nom_Capteur == 'Compresseur':
    Compresseur(TempEntree, TempSortie, HautePression, BassePression)
elif nom_Capteur == 'Detendeur':
    Detendeur(cur, TempEntree, TempSortie)
elif nom_Capteur == 'Condenseur':
    Condenseur(cur, TempEntree, TempSortie, nom_Capteur)
elif nom_Capteur == 'Evaporateur':
    Evaporateur(cur, TempEntree, TempSortie, nom_Capteur)
elif nom_Capteur == 'Eau':
    Eau(cur, TempAvant, TempApres)
elif nom_Capteur == 'Tension':
    Tension(cur, Volt1, nom_Capteur)
else :
    Intensite(cur, Ampere1)
"""

"""
if nom_Capteur == 'Compresseur' :
    Temperature(cur, TempEntree, TempSortie, nom_Capteur)
    Pression(cur, HautePression, BassePression, nom_Capteur)
elif nom_Capteur == 'Condenseur' or nom_Capteur == 'Detendeur' or nom_Capteur == 'Evaporateur':
    Temperature(cur, TempEntree, TempSortie, nom_Capteur)
else :
    print("Fin")
"""

""""
def Temperature (cur, TempEntree, TempSortie, nom_Capteur):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Temperature_Entree, Temperature_Sortie, Capteur_nom) VALUES (%s, %s, %s);", (TempEntree, TempSortie, nom_Capteur))
    cur.commit()

def Pression (cur, HautePression, BassePression, nom_capteur):
    curso = cur.cursor()
    curso.execute ("INSERT INTO donnees_recu (Haute_Pression, Basse_Pression, Capteur_nom) VALUES (%s, %s, %s);", (HautePression, BassePression, nom_Capteur))
    cur.commit()
"""

"""
def recupCourant(cur, Intensit):
     curso = cur.cursor()
     requete = "INSERT INTO Courant (Intensite) VALUES  ('" + str(Intensit) + "');"
     curso.execute (requete)
     cur.commit()

def recupTension (cur, Volt):
     curso = cur.cursor()
     requete = "INSERT INTO Tension (Volt) VALUES  ('" + str(Volt) + "');"
     curso.execute (requete)
     cur.commit()
"""