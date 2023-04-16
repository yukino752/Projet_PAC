import time
import serial
import signal
import sys
from RecupValeurV3 import read_capteur


# ISR de fermeture d'application
def fermer_application(sig, frame):
    global vivant
    
    # arrêter le minuteur
    signal.alarm(0)
    vivant = False
    
# ISR de déclenchement de relevé   
def relever_mesure(sig, frame):
    global periode
    global declenchement_mesure
    
    # commande acquisition relevé...
    declenchement_mesure = True
    
    # réarmement du minuteur...'
    signal.alarm(periode)


def initialiser_minuteur():
    global periode
    
    periode = int(input("Entrez la période du relevé : "))
    signal.alarm(periode)



if __name__ == '__main__':
    global vivant
    global declenchement_mesure
    capteur = {"EntreeDetendeur" : None, "SortieDetendeur" : None,
               "EntreeCompresseur" : None, "SortieCompresseur" : None,
               "EntreeCondenseur" : None, "SortieCondenseur" : None,
               "SortieEvaporateur" : None, "temperatureEau" : None,
               "bassePression" : None, "hautePression" : None
            }
    
    vivant = True
    declenchement_mesure = False
    
    print('Running. Press CTRL-C to exit.')
    signal.signal(signal.SIGINT, fermer_application)
    signal.signal(signal.SIGALRM, relever_mesure)

    initialiser_minuteur()
    
    """
    
        time.sleep(0.1) #wait for serial to open
    """

    while(vivant):
        if(declenchement_mesure):
            with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
                for point_de_mesure in capteur:
                    capteur[point_de_mesure]  = read_capteur(arduino, point_de_mesure)
            
    print("Au revoir !")


