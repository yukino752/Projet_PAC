#include "max6675.h"
#include <math.h>
#include <Adafruit_MAX31856.h>


//THERMOCOUPLE
int thermoSO1 = 4;
int thermoCS1 = 5;
int thermoSCK1 = 6;

//THERMOCOUPLE 1
int thermoSO2 = 29;
int thermoCS2 = 30;
int thermoSCK2 = 31;

//CAPTEURS PRESSION
const int capteurPression1 = A14;
const int capteurPression2 = A15;


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



MAX6675 thermocouple1(thermoSCK1, thermoCS1, thermoSO1);
MAX6675 thermocouple2(thermoSCK2, thermoCS2, thermoSO2);


class temperature
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
};

class temperatureThermocouple
{
    public:

    float TempVentilateur(){
        Serial.print("temperatureEntreeDetendeur");
        Serial.println(thermocouple1.readCelsius());
        delay(1000);

        Serial.print("temperatureSortieDetendeur"); 
        Serial.println(thermocouple2.readCelsius());
        delay(1000);

        /*Serial.print("temperatureEntreeCompresseur"); 
        Serial.println(thermocouple3.readCelsius());
        delay(1000);

        Serial.print("temperatureSortieCompresseur"); 
        Serial.println(thermocouple4.readCelsius());
        delay(1000);

        Serial.print("temperatureEntreeCondenseur"); 
        Serial.println(thermocouple5.readCelsius());
        delay(1000);

        Serial.print("temperatureSortieCondenseur"); 
        Serial.println(thermocouple6.readCelsius());
        delay(1000);

        Serial.print("temperatureSortieEvaporateur"); 
        Serial.println(thermocouple7.readCelsius());
        delay(1000);*/

        
    }

};

void setup() {
  Serial.begin(9600);
  delay(500);
}

temperature T;
temperatureThermocouple TT;

void loop() {
  TT.TempVentilateur();
  delay(500);

  float pression1 = analogRead(capteurPression1);
  Serial.print("Pression1 (V) : ");
  Serial.println(pression1*5/1023);

  float pression2 = analogRead(capteurPression2);
  Serial.print("Pression2 (V) : ");
  Serial.println(pression2*5/552);



  /*//THERMOCOUPLE MAX6675
  //Serial.print("x"); 
  Serial.print(thermocouple.readCelsius());
  Serial.print("x");
  delay(1000);

  //THERMOCOUPLE MAX31856
  maxthermo.triggerOneShot();
  
  Serial.print(maxthermo.readThermocoupleTemperature()); Serial.print("x");

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




