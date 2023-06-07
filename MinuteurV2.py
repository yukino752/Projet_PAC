import time
import serial
import signal
import traceback
from RecupValeurV5 import read_capteur


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
               "bassePression" : None, "hautePression" : None,
               "copReel" : None
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
            with serial.Serial("/dev/ttyACM0", 1000000, timeout=1) as liaison_serie:
                time.sleep(0.01) # https://github.com/pyserial/pyserial/issues/329
                for point_de_mesure in capteur:
                    try :
                        capteur[point_de_mesure]  = read_capteur(liaison_serie)
                    except BaseException as error:
                        print("Erreur : " + str(error))
                        print(traceback.format_exc())
            
    print("Au revoir !")


