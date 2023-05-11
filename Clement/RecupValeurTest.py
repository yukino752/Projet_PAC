import time
import serial
import signal
from CreateDatabase import *
from Insert_Database import *
from Select_Database import *

connectDB()
Create_Table()

def signal_handler(sig, frame):
    print('Exiting...')
    arduino.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def read_capteur(arduino, point_de_mesure):
    assert isinstance(point_de_mesure, str), type(point_de_mesure)
    answer = str(arduino.readline().decode("utf8", errors="replace"))
    
    """    
    dispositif_dict = {
        "Compresseur"  : Compresseur,
        "Detendeur"  : Detendeur,
        "Condenseur"  : Condenseur,
        "Evaporateur"  : Evaporateur,
        "Eau" : Eau			
    }
   
   
    dispositif_func = dispositif_dict[answer.replace("temperature", "").replace("Entree", "").replace("Sortie", "").replace("basse", "").replace("haute", "")]
        
    print(answer)
    plage_validite = answer.split(point_de_mesure)
    print(plage_validite[1])
    validite_min, validite_max = Select_id_Capteur(point_de_mesure)
    print(validite_min)
    id_capteur = Select_id_Capteur(point_de_mesure)
    id_releve = 1
    if plage_validite[1]>validite_min and plage_validite[1]<validite_max:
        dispositif_func(plage_validite[1], id_capteur, id_releve)
    else:
        dispositif_func(None, id_capteur, id_releve)
               
    """    
    if 'temperatureEntreeDetendeur' in answer:
        print(answer)
        temperatureEntreeDetendeur = answer.split("temperatureEntreeDetendeur")
        print(temperatureEntreeDetendeur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureEntreeDetendeur')
        print(validite_min)
        id_capteur = Select_id_Capteur('TemperatureEntreeDentendeur')
        id_releve = 1
        if temperatureEntreeDetendeur[1]>validite_min and temperatureEntreeDetendeur[1]<validite_max:
            Detendeur(temperatureEntreeDetendeur[1], id_capteur, id_releve)
        else:
            Detendeur(None, id_capteur, id_releve)

    elif 'temperatureSortieDetendeur' in answer:
        print(answer)
        temperatureSortieDetendeur = answer.split("temperatureSortieDetendeur")
        print(temperatureSortieDetendeur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureSortieDetendeur')
        id_capteur = Select_id_Capteur('TemperatureSortieDentendeur')
        id_releve = 1
        if temperatureSortieDetendeur[1]>validite_min and temperatureSortieDetendeur[1]<validite_max:
            Detendeur(temperatureSortieDetendeur[1], id_capteur, id_releve)
        else:
            Detendeur(None, id_capteur, id_releve)

    elif 'temperatureEntreeCompresseur' in answer:
        print(answer)
        temperatureEntreeCompresseur = answer.split("temperatureEntreeCompresseur")
        print(temperatureEntreeCompresseur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureEntreeCompresseur')
        id_capteur = Select_id_Capteur('TemperatureEntreeCompresseur')
        id_releve = 1
        if temperatureEntreeCompresseur[1]>validite_min and temperatureEntreeCompresseur[1]<validite_max:
            Compresseur(temperatureEntreeCompresseur[1], id_capteur, id_releve)
        else:
            Compresseur(None, id_capteur, id_releve)

    elif 'temperatureSortieCompresseur' in answer:
        print(answer)
        temperatureSortieCompresseur = answer.split("temperatureSortieCompresseur")
        print(temperatureSortieCompresseur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureSortieCompresseur')
        id_capteur = Select_id_Capteur('TemperatureSortieCompresseur')
        id_releve = 1
        if temperatureSortieCompresseur[1]>validite_min and temperatureSortieCompresseur[1]<validite_max:
            Compresseur(temperatureSortieCompresseur[1], id_capteur, id_releve)
        else:
            Compresseur(None, id_capteur, id_releve)

    elif 'temperatureEntreeCondenseur' in answer:
        print(answer)
        temperatureEntreeCondenseur = answer.split("temperatureEntreeCondenseur")
        print(temperatureEntreeCondenseur[1])
        print("Debug : " + str(type(Select_id_Capteur('temperatureEntreeCondenseur'))))
        validite_min, validite_max = Select_id_Capteur('temperatureEntreeCondenseur')
        id_capteur = Select_id_Capteur('TemperatureEntreeCondenseur')
        id_releve = 1
        if temperatureEntreeCondenseur[1]>validite_min and temperatureEntreeCondenseur[1]<validite_max:
            Condenseur(temperatureEntreeCondenseur[1], id_capteur, id_releve)
        else:
            Condenseur(None, id_capteur, id_releve)

    elif 'temperatureSortieCondenseur' in answer:
        print(answer)
        temperatureSortieCondenseur = answer.split("temperatureSortieCondenseur")
        print(temperatureSortieCondenseur[1])
        validite_min, validite_max = Select_id_Capteur('temperatureSortieCondenseur')
        id_capteur = Select_id_Capteur('TemperatureSortieCondenseur')
        id_releve = 1
        if temperatureSortieCondenseur[1]>validite_min and temperatureSortieCondenseur[1]<validite_max:
            Condenseur(temperatureSortieCondenseur[1], id_capteur, id_releve)
        else:
            Condenseur(None, id_capteur, id_releve)

    elif 'temperatureSortieEvaporateur' in answer:
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
        
    elif 'temperatureEau' in answer:
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
        
    elif 'hautePression' in answer:
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
        
    elif 'bassePression' in answer:
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

    arduino.flushInput() #remove data after reading

if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        
        arduino.close()
