import time
import serial
import signal
#from MinuteurV2 import minuteur

def signal_handler(sig, frame):
    print('Exiting...')
    arduino.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def read_capteur(arduino, point_de_mesure):
    answer = str(arduino.readline().decode("utf8", errors="replace"))
    if 'temperatureEntreeDetendeur' in answer:
        print(answer)
        temperatureEntreeDetendeur = answer.split("temperatureEntreeDetendeur")
        print(temperatureEntreeDetendeur[1])

    elif 'temperatureSortieDetendeur' in answer:
        print(answer)
        temperatureSortieDetendeur = answer.split("temperatureSortieDetendeur")
        print(temperatureSortieDetendeur[1])

    elif 'temperatureEntreeCompresseur' in answer:
        print(answer)
        temperatureEntreeCompresseur = answer.split("temperatureEntreeCompresseur")
        print(temperatureEntreeCompresseur[1])

    elif 'temperatureSortieCompresseur' in answer:
        print(answer)
        temperatureSortieCompresseur = answer.split("temperatureSortieCompresseur")
        print(temperatureSortieCompresseur[1])

    elif 'temperatureEntreeCondenseur' in answer:
        print(answer)
        temperatureEntreeCondenseur = answer.split("temperatureEntreeCondenseur")
        print(temperatureEntreeCondenseur[1])

    elif 'temperatureSortieCondenseur' in answer:
        print(answer)
        temperatureSortieCondenseur = answer.split("temperatureSortieCondenseur")
        print(temperatureSortieCondenseur[1])

    elif 'temperatureSortieEvaporateur' in answer:
        print(answer)
        temperatureSortieEvaporateur = answer.split("temperatureSortieEvaporateur")
        print(temperatureSortieEvaporateur[1])
        
    elif 'temperatureEau' in answer:
        print(answer)
        temperatureEau = answer.split("temperatureEau")
        print(temperatureEau[1])
        
    elif 'hautePression' in answer:
        print(answer)
        hautePression = answer.split("hautePression")
        print(hautePression[1])
        
    elif 'bassePression' in answer:
        print(answer)
        bassePression = answer.split("bassePression")
        print(bassePression[1])


    arduino.flushInput() #remove data after reading

if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        
        arduino.close()
