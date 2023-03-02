import time 
import serial
if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
    time.sleep(0.1) #wait for serial to open
arduino.open()
try:
    while True:
                answer=str(arduino.readline().decode("utf8", errors="replace"))
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
                    
                    arduino.flushInput() #remove data after reading
except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught.")
