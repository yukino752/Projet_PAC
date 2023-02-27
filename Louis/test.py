import time
import serial
if __name__ == '__main__':
	print('Running. Press CTRL-C to exit.')
with serial.Serial("COM9", 9600, timeout=1) as arduino:
	time.sleep(0.1) #wait for serial to open
arduino.open()
try:
	while True:   
                answer=str(arduino.readline().decode("utf8", errors="replace"))
                if 'test' in answer :  
                        print(answer)
                        nombre = answer.split("test")
                        print(nombre[1])
                elif 're' in answer :  
                        print(answer)
                        nombreRe = answer.split("re")
                        print(nombreRe[1])
                arduino.flushInput() #remove data after reading
                
except KeyboardInterrupt:
	print("KeyboardInterrupt has been caught.")
