#include "max6675.h"
#include <math.h>
#include <Adafruit_MAX31865_PT100.h>

#define RREF      430.0
#define RNOMINAL  100.0


//THERMOCOUPLE ENTREE DETENDEUR
int thermoSO1 = 22;
int thermoCS1 = 23;
int thermoSCK1 = 24;

//THERMOCOUPLE SORTIE DETENDEUR
int thermoSO2 = 25;
int thermoCS2 = 26;
int thermoSCK2 = 27;

//THERMOCOUPLE ENTREE COMPRESSEUR
int thermoSO3 = 28;
int thermoCS3 = 29;
int thermoSCK3 = 30;

//THERMOCOUPLE SORTIE COMPRESSEUR
int thermoSO4 = 31;
int thermoCS4 = 32;
int thermoSCK4 = 33;

//THERMOCOUPLE ENTREE CONDENSEUR
int thermoSO5 = 34;
int thermoCS5 = 35;
int thermoSCK5 = 36;

//THERMOCOUPLE SORTIE CONDENSEUR
int thermoSO6 = 37;
int thermoCS6 = 38;
int thermoSCK6 = 39;

//THERMOCOUPLE SORTIE EVAPORATEUR
int thermoSO7 = 40;
int thermoCS7 = 41;
int thermoSCK7 = 42;


//CAPTEURS PRESSION
const int capteurBassePression = A14;
const int capteurHautePression = A15;


//THERMISTANCE
const int B = 4275;
const int R0 = 100000;
const int pinTempSensor = A2;

//THERMISTANCEv2
const int pinTempSensorv20 = A0;
const int pinTempSensorv21 = A1;
const int pinTempSensorv22 = A2;
const int R0v2 = 10000;
const int Bv2 = 4275;
const float T0 = 269.15;


MAX6675 thermocoupleEntreeDetendeur(thermoSCK1, thermoCS1, thermoSO1);
MAX6675 thermocoupleSortieDetendeur(thermoSCK2, thermoCS2, thermoSO2);
MAX6675 thermocoupleEntreeCompresseur(thermoSCK3, thermoCS3, thermoSO3);
MAX6675 thermocoupleSortieCompresseur(thermoSCK4, thermoCS4, thermoSO4);
MAX6675 thermocoupleEntreeCondenseur(thermoSCK5, thermoCS5, thermoSO5);
MAX6675 thermocoupleSortieCondenseur(thermoSCK6, thermoCS6, thermoSO6);
MAX6675 thermocoupleSortieEvaporateur(thermoSCK7, thermoCS7, thermoSO7);

Adafruit_MAX31865 max = Adafruit_MAX31865(4, 5, 6, 7);

/*class temperature
{
    public:

    float TempVentilateur(){
        float VRT0 = analogRead(A0);             
        VRT0 = (5.00 / 1023.00) * VRT0;      
        float VR0 = 5 - VRT0;
        float RT0 = VRT0 / (VR0 / 10000);             
        float ln0 = log(RT0 / R0v2);
        float TX0 = (1 / ((ln0 / B) + (1 / T0))); 
        TX0 = TX0 - 273.15;    

        float VRT1 = analogRead(A1);          
        VRT1 = (5.00 / 1023.00) * VRT1;      
        float VR1 = 5 - VRT1;
        float RT1 = VRT1 / (VR1 / 10000);             
        float ln1 = log(RT1 / R0v2);
        float TX1 = (1 / ((ln1 / B) + (1 / T0))); 
        TX1 = TX1 - 273.15;

        Serial.print("re");
        Serial.println(TX0);
        delay(1000);
        Serial.print("test"); 
        Serial.println(TX1);
        delay(1000);
    }
};*/

class temperatureThermocouples
{
  public:

    float readTemperature(){
      Serial.print("temperatureEntreeDetendeur");
      Serial.println(thermocoupleEntreeDetendeur.readCelsius());
      delay(1000);

      Serial.print("temperatureSortieDetendeur"); 
      Serial.println(thermocoupleSortieDetendeur.readCelsius());
      delay(1000);

      Serial.print("temperatureEntreeCompresseur"); 
      Serial.println(thermocoupleEntreeCompresseur.readCelsius());
      delay(1000);

      Serial.print("temperatureSortieCompresseur"); 
      Serial.println(thermocoupleSortieCompresseur.readCelsius());
      delay(1000);

      Serial.print("temperatureEntreeCondenseur"); 
      Serial.println(thermocoupleEntreeCondenseur.readCelsius());
      delay(1000);

      Serial.print("temperatureSortieCondenseur"); 
      Serial.println(thermocoupleSortieCondenseur.readCelsius());
      delay(1000);

      Serial.print("temperatureSortieEvaporateur"); 
      Serial.println(thermocoupleSortieEvaporateur.readCelsius());
      delay(1000);
   }

};

class temperaturePT100
{
  public:

    float readPT100(){
      uint16_t rtd = max.readRTD();
      Serial.print("temperatureEau"); 
      Serial.println(max.temperature(RNOMINAL, RREF));
      delay(1000);
   }

};

class pressionCapteurs
{
  public :

    float readPression(){
      float rawBassePression = analogRead(capteurBassePression);
      float BassePression = (7.3/818.4)*(rawBassePression-(1023*0.5/5));
      //Serial.println(rawBassePression);
      Serial.println(BassePression);

      float rawHautePression = analogRead(capteurHautePression);
      float HautePression = (34.5/818.4)*(rawHautePression-(1023*0.5/5));
      //Serial.println(rawHautePression);
      Serial.println(HautePression);
   }


};

void setup() {
  Serial.begin(9600);
  max.begin(MAX31865_2WIRE);
  delay(500);
}

//temperature T;
temperatureThermocouples T;
temperaturePT100 PT;
pressionCapteurs P;

void loop() {
  T.readTemperature();
  P.readPression();
  PT.readPT100();
  delay(500);

  /*float rawBassePression = analogRead(capteurBassePression);
  Serial.print("Basse Pression (V) : ");
  float voltageBassePression = rawBassePression/1023*5;
  Serial.println(voltageBassePression);
  Serial.print("Basse Pression (Pa) : ");
  Serial.println(voltageBassePression*(10.3/5));
  float BassePression = (7.3/818.4)*(rawBassePression-(1023*0.5/5));
  Serial.println(rawBassePression);
  Serial.println(BassePression);*/

  /*float rawHautePression = analogRead(capteurHautePression);
  Serial.print("Haute Pression (V) : ");
  float voltageHautePression = rawHautePression/1023*5;
  Serial.println(voltageHautePression);
  Serial.print("Haute Pression (Pa) : ");
  Serial.println(voltageHautePression*(34.5/5));
  float HautePression = (34.5/818.4)*(rawHautePression-(1023*0.5/5));
  Serial.println(rawHautePression);
  Serial.println(HautePression);*/


  //Serial.println(max.temperature(100.0, 430.0));
  /*//THERMOCOUPLE MAX6675
  //Serial.print("x"); 
  Serial.print(thermocouple.readCelsius());
  Serial.print("x");
  delay(1000);

  //THERMOCOUPLE MAX31856
  maxthermo.triggerOneShot();
  Serial.print(maxthermo.readThermocoupleTemperature());

  THERMISTANCE
  int a = analogRead(pinTempSensor);
  float R = 1023.0/a-1.0;
  R = R0*R;
  float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15;
  Serial.print("temperature = ");
  Serial.println(temperature);
  delay(100);


  //THERMISTANCEv20
  float VRT0 = analogRead(A0);              //Acquisition analog value of VRT
  VRT0 = (5.00 / 1023.00) * VRT0;      //Conversion to voltage
  float VR0 = 5 - VRT0;
  float RT0 = VRT0 / (VR0 / 10000);               //Resistance of RT
  float ln0 = log(RT0 / R0v2);
  float TX0 = (1 / ((ln0 / B) + (1 / T0))); //Temperature from thermistor
  TX0 = TX0 - 273.15;                 //Conversion to Celsius
  Serial.print("x");
  Serial.print(TX0);


  //THERMISTANCEv21
  float VRT1 = analogRead(A1);              //Acquisition analog value of VRT
  VRT1 = (5.00 / 1023.00) * VRT1;      //Conversion to voltage
  float VR1 = 5 - VRT1;
  float RT1 = VRT1 / (VR1 / 10000);               //Resistance of RT
  float ln1 = log(RT1 / R0v2);
  float TX1 = (1 / ((ln1 / B) + (1 / T0))); //Temperature from thermistor
  TX1 = TX1 - 273.15;                 //Conversion to Celsius
  Serial.print("x");
  Serial.print(TX1);


  //THERMISTANCEv22
  float VRT2 = analogRead(A2);              //Acquisition analog value of VRT
  VRT2 = (5.00 / 1023.00) * VRT2;      //Conversion to voltage
  float VR2 = 5 - VRT2;
  float RT2 = VRT2 / (VR2 / 10000);               //Resistance of RT
  float ln2 = log(RT2 / R0v2);
  float TX2 = (1 / ((ln2 / B) + (1 / T0))); //Temperature from thermistor
  TX2 = TX2 - 273.15;                 //Conversion to Celsius
  Serial.print("x");
  Serial.print(TX2);*/

}




