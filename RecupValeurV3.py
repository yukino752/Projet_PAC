# Import des modules nécessaires
import time # Pour les opérations liées au temps
import serial # Pour la communication série avec l'Arduino
import signal # Pour gérer les signaux (notamment le signal de fermeture)
# Import des fonctions pour créer, insérer et sélectionner des données dans une base de données
from CreateDatabase import *
from Insert_Database import *
from Select_Database import *
from MinuteurV2 import minuteur *# Import de la fonction minuteur depuis le fichier MinuteurV2.py (actuellement en commentaire)

connectDB()# Connexion à la base de données
Create_Table()# Création de la table de relevés si elle n'existe pas déjà

def signal_handler(sig, frame):# Fonction pour gérer le signal de fermeture (CTRL+C)
    print('Exiting...')
    arduino.close() # Fermeture de la connexion série avec l'Arduino
    sys.exit(0) # Fermeture du programme
signal.signal(signal.SIGINT, signal_handler)# Association de la fonction signal_handler au signal SIGINT (signal de fermeture)

def read_capteur(arduino, point_de_mesure):# Fonction pour lire les données des capteurs
    answer = str(arduino.readline().decode("utf8", errors="replace"))# Lecture d'une ligne de la sortie série de l'Arduino
    if 'temperatureEntreeDetendeur' in answer:# Si la ligne contient la chaîne "temperatureEntreeDetendeur"
        print(answer)
        temperatureEntreeDetendeur = answer.split("temperatureEntreeDetendeur")# Extraction de la température
        print(temperatureEntreeDetendeur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureEntreeDetendeur')# Récupération des limites de validité de la température pour ce capteur dans la base de données
        id_capteur = Select_id_Capteur('TemperatureEntreeDentendeur')# Récupération de l'identifiant du capteur correspondant à la température d'entrée du détendeur
        id_releve = 1        # Identifiant du relevé (ici fixé à 1)
        if temperatureEntreeDetendeur[1]>validite_min and temperatureEntreeDetendeur[1]<validite_max:# Si la température est valide (c'est-à-dire si elle est comprise entre les limites de validité)
            Detendeur(temperatureEntreeDetendeur[1], id_capteur, id_releve)# Insertion du relevé dans la base de données avec la température et l'identifiant du capteur

        else:
            Detendeur(None, id_capteur, id_releve)# Si la température n'est pas valide, on insère un relevé avec une valeur NULL


    elif 'temperatureSortieDetendeur' in answer:  # Si la réponse de l'Arduino contient 'temperatureSortieDetendeur'
        print(answer)
        temperatureSortieDetendeur = answer.split("temperatureSortieDetendeur")  # Sépare la chaîne de caractères en deux parties, avec 'temperatureSortieDetendeur' comme séparateur
        print(temperatureSortieDetendeur[1])  # Affiche la deuxième partie (après le séparateur) de la chaîne de caractères
        validite_min, validite_max = Select_id_Capteur('temperatureSortieDetendeur')  # Récupère les valeurs minimale et maximale pour ce capteur depuis la base de données
        id_capteur = Select_id_Capteur('TemperatureSortieDentendeur')  # Récupère l'identifiant de ce capteur depuis la base de données
        id_releve = 1  # Identifiant du relevé de capteur, à déterminer selon le contexte
        if temperatureSortieDetendeur[1]>validite_min and temperatureSortieDetendeur[1]<validite_max:  # Si la température relevée est valide (entre la valeur minimale et maximale)
            Detendeur(temperatureSortieDetendeur[1], id_capteur, id_releve)  # Effectue l'enregistrement dans la base de données avec les valeurs relevées et les identifiants correspondants
        else:  # Si la température relevée est invalide
            Detendeur(None, id_capteur, id_releve)  # Effectue l'enregistrement dans la base de données avec la valeur 'None' pour la température et les identifiants correspondants

    elif 'temperatureEntreeCompresseur' in answer:  # Si la réponse de l'Arduino contient 'temperatureEntreeCompresseur'
        print(answer)
        temperatureEntreeCompresseur = answer.split("temperatureEntreeCompresseur")  # Sépare la chaîne de caractères en deux parties, avec 'temperatureEntreeCompresseur' comme séparateur
        print(temperatureEntreeCompresseur[1])  # Affiche la deuxième partie (après le séparateur) de la chaîne de caractères
        validite_min, validite_max = Select_id_Capteur('temperatureEntreeCompresseur')  # Récupère les valeurs minimale et maximale pour ce capteur depuis la base de données
        id_capteur = Select_id_Capteur('TemperatureEntreeCompresseur')  # Récupère l'identifiant de ce capteur depuis la base de données
        id_releve = 1  # Identifiant du relevé de capteur, à déterminer selon le contexte
        if temperatureEntreeCompresseur[1]>validite_min and temperatureEntreeCompresseur[1]<validite_max:  # Si la température relevée est valide (entre la valeur minimale et maximale)
            Compresseur(temperatureEntreeCompresseur[1], id_capteur, id_releve)  # Effectue l'enregistrement dans la base de données avec les valeurs relevées et les identifiants correspondants
        else:  # Si la température relevée est invalide
                Compresseur(None, id_capteur, id_releve)
    
    elif 'temperatureSortieCompresseur' in answer:
        print(answer)# Afficher la réponse reçue
        temperatureSortieCompresseur = answer.split("temperatureSortieCompresseur")# Extraire la température à partir de la réponse
        print(temperatureSortieCompresseur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureSortieCompresseur')# Récupérer les limites de validité pour le capteur correspondant à la température de sortie du compresseur
        id_capteur = Select_id_Capteur('TemperatureSortieCompresseur')    # Récupérer l'identifiant du capteur correspondant à la température de sortie du compresseur
        id_releve = 1    # Définir l'identifiant de relevé à 1
        if temperatureSortieCompresseur[1]>validite_min and temperatureSortieCompresseur[1]<validite_max:# Vérifier si la température extraite est dans la plage de validité du capteur
            Compresseur(temperatureSortieCompresseur[1], id_capteur, id_releve)# Si oui, envoyer la température à la fonction Compresseur
        else:
            Compresseur(None, id_capteur, id_releve)# Sinon, envoyer None à la fonction Compresseur
    
    elif 'temperatureEntreeCondenseur' in answer:
        print(answer) # Afficher la réponse reçue
        temperatureEntreeCondenseur = answer.split("temperatureEntreeCondenseur")# Extraire la température à partir de la réponse
        print(temperatureEntreeCondenseur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureEntreeCondenseur')# Récupérer les limites de validité pour le capteur correspondant à la température d'entrée du condenseur
        id_capteur = Select_id_Capteur('TemperatureEntreeCondenseur')# Récupérer l'identifiant du capteur correspondant à la température d'entrée du condenseur
        id_releve = 1    # Définir l'identifiant de relevé à 1
        if temperatureEntreeCondenseur[1]>validite_min and temperatureEntreeCondenseur[1]<validite_max:# Vérifier si la température extraite est dans la plage de validité du capteur
            Condenseur(temperatureEntreeCondenseur[1], id_capteur, id_releve)# Si oui, envoyer la température à la fonction Condenseur
        else:
            Condenseur(None, id_capteur, id_releve)  # Sinon, envoyer None à la fonction Condenseur
    
    
    elif 'temperatureSortieCondenseur' in answer: # Vérifie si "temperatureSortieCondenseur" est présent dans la réponse
        print(answer) # Affiche la réponse
        temperatureSortieCondenseur = answer.split("temperatureSortieCondenseur") # Sépare la réponse en deux parties, en utilisant "temperatureSortieCondenseur" comme délimiteur
        print(temperatureSortieCondenseur[1]) # Affiche la deuxième partie de la réponse, qui doit contenir la valeur de la température
        validite_min, validite_max = Select_id_Capteur('temperatureSortieCondenseur') # Récupère les valeurs minimale et maximale autorisées pour cette mesure, en utilisant une fonction Select_id_Capteur()
        id_capteur = Select_id_Capteur('TemperatureSortieCondenseur') # Récupère l'identifiant du capteur associé à cette mesure, en utilisant une fonction Select_id_Capteur()
        id_releve = 1 # Fixe l'identifiant du relevé à 1 (à changer selon les besoins)
        if temperatureSortieCondenseur[1]>validite_min and temperatureSortieCondenseur[1]<validite_max: # Vérifie si la valeur de la température est comprise entre les limites autorisées
            Condenseur(temperatureSortieCondenseur[1], id_capteur, id_releve) # Si oui, appelle la fonction Condenseur() avec les valeurs appropriées
        else:
            Condenseur(None, id_capteur, id_releve) # Si non, appelle la fonction Condenseur() avec la valeur None pour la température
    
    elif 'temperatureSortieEvaporateur' in answer: # Même chose pour "temperatureSortieEvaporateur"
        print(answer)
        temperatureSortieEvaporateur = answer.split("temperatureSortieEvaporateur")
        print(temperatureSortieEvaporateur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureSortieEvaporateur')
        id_capteur = Select_id_Capteur('TemperatureSortieEvaporateur')
        id_releve = 1
        if temperatureSortieEvaporateur[1]>validite_min and temperatureSortieEvaporateur[1]<validite_max:
            Evaporateur(temperatureSortieEvaporateur[1], id_capteur, id_releve)
        else:
            Evaporateur(None, id_capteur, id_releve)
        
    elif 'temperatureEau' in answer: # Même chose pour "temperatureEau"
        print(answer)
        temperatureEau = answer.split("temperatureEau")
        print(temperatureEau[1])
        validite_min, validite_max = Select_id_Capteur('temperatureEau')
        id_capteur = Select_id_Capteur('TemperatureEau')
        id_releve = 1
        if temperatureEau[1]>validite_min and temperatureEau[1]<validite_max:
            Eau(temperatureEau[1], id_capteur, id_releve)
        else:
            Eau(None, id_capteur, id_releve)
    
    elif 'hautePression' in answer:# Même chose pour "hautePression"
            print(answer)
            hautePression = answer.split("hautePression")
            print(hautePression[1])
            validite_min, validite_max = Select_id_Capteur('hautePression')
            id_capteur = Select_id_Capteur('hautePression')
            id_releve = 1
            if hautePression[1]>validite_min and hautePression[1]<validite_max:
                Compresseur(hautePression[1], id_capteur, id_releve)
            else:
                Compresseur(None, id_capteur, id_releve)
            
    elif 'bassePression' in answer:# Même chose pour "bassePression"
            print(answer)
            bassePression = answer.split("bassePression")
            print(bassePression[1])
            validite_min, validite_max = Select_id_Capteur('bassePression')
            id_capteur = Select_id_Capteur('bassePression')
            id_releve = 1
            if bassePression[1]>validite_min and bassePression[1]<validite_max:
                Compresseur(bassePression[1], id_capteur, id_releve)
            else:
                Compresseur(None, id_capteur, id_releve)


    arduino.flushInput()# Vidage du buffer d'entrée de l'Arduino
    
if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("COM3", 9600, timeout=1) as arduino:# Ouverture de la connexion série avec l'Arduino
        time.sleep(0.1) # Attente de l'ouverture du port série
        arduino.close()        # Fermeture de la connexion série avec l'Arduino
