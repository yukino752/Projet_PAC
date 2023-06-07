import time
import serial
import signal
import re
from CreateDatabase import *
from Insert_Database import *
from Select_Database import *

connectDB()  # Établir une connexion à la base de données
Create_Table()  # Créer une table dans la base de données

def signal_handler(sig, frame):
    print('Exiting...')
    arduino.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  # Gérer la signalisation de sortie du programme

def read_capteur(liaison_serie):
    # Lire les données du capteur depuis la liaison série
    message = liaison_serie.readline().decode('utf-8', errors="replace")

    assert message != "", "le message recu est vide" + message

    print("DEBUG 1 : message recu sur la ligne série = "  + message)

    dispositif_switcher = {
        "Compresseur"  : Compresseur,
        "Detendeur"  : Detendeur,
        "Condenseur"  : Condenseur,
        "Evaporateur"  : Evaporateur,
        "Eau" : Eau,
        "Pression"  : Compresseur
    }

    # Vérifier si la valeur de mesure est valide en utilisant une expression régulière
    match = re.search(r'[0-9]+(\.[0-9]+)?\r?\n?$', message)
    assert match is not None, "valeur de mesure invalide"
    valeur_mesure = float(match.group(0))

    # Extraire le nom du capteur à partir du message
    for reponse in [r'[0-9]+(\.[0-9]+)?\r?\n$']:
        capteur = re.sub(reponse, '', message)

    # Extraire la clé du capteur à partir du message
    clef = message
    for motif in [r'[0-9]+(\.[0-9]+)?\r?\n$', '^(temperature|basse|haute)', 'Entree|Sortie']:
        clef = re.sub(motif, '', clef)

    assert clef in dispositif_switcher, "clef invalide, message reçu incomplet ?"
    print("DEBUG 2 : clef = "+ clef +", answer = "+ message +", valeur_mesure = "+ str(valeur_mesure))

    dispositif_func = dispositif_switcher[clef]

    # Sélectionner les limites de validité pour le capteur à partir de la base de données
    validite_min, validite_max = Select_validite(capteur)
    print(validite_min)
    print(validite_max)

    # Sélectionner l'ID du capteur à partir de la base de données
    id_capteur = Select_id_Capteur(capteur)

    id_releve = 1

    # Vérifier si la valeur de mesure est dans les limites de validité
    if valeur_mesure > validite_min and valeur_mesure < validite_max:
        dispositif_func(valeur_mesure, id_capteur, id_releve)
    else:
        dispositif_func(None, id_capteur, id_releve)

if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')

