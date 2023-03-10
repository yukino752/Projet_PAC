#include "max6675.h"
#include <math.h>
#include <Adafruit_MAX31856.h>


//THERMOCOUPLE
int thermoSO = 4;
int thermoCS = 5;
int thermoSCK = 6;



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



MAX6675 thermocouple(thermoSCK, thermoCS, thermoSO);
Adafruit_MAX31856 maxthermo = Adafruit_MAX31856(10, 11, 12, 13);


void setup() {
  Serial.begin(9600);
  maxthermo.begin();
  maxthermo.setThermocoupleType(MAX31856_TCTYPE_K);
  maxthermo.setConversionMode(MAX31856_ONESHOT_NOWAIT);
  delay(500);
}

void loop() {
  //THERMOCOUPLE MAX6675
  Serial.print("MAX6675 : "); 
  Serial.println(thermocouple.readCelsius());
  Serial.println();
  delay(1000);

  //THERMOCOUPLE MAX31856
  maxthermo.triggerOneShot();
  Serial.print("MAX31856 : ");
  Serial.println(maxthermo.readThermocoupleTemperature());

  /*THERMISTANCE
  int a = analogRead(pinTempSensor);
  float R = 1023.0/a-1.0;
  R = R0*R;
  float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15;
  Serial.print("temperature = ");
  Serial.println(temperature);
  delay(100);*/


  //THERMISTANCEv20
  float VRT0 = analogRead(A0);              //Acquisition analog value of VRT
  VRT0 = (5.00 / 1023.00) * VRT0;      //Conversion to voltage
  float VR0 = 5 - VRT0;
  float RT0 = VRT0 / (VR0 / 10000);               //Resistance of RT
  float ln0 = log(RT0 / R0v2);
  float TX0 = (1 / ((ln0 / B) + (1 / T0))); //Temperature from thermistor
  TX0 = TX0 - 273.15;                 //Conversion to Celsius
  Serial.print("Temperature : ");
  Serial.println(TX0);


  //THERMISTANCEv21
  float VRT1 = analogRead(A1);              //Acquisition analog value of VRT
  VRT1 = (5.00 / 1023.00) * VRT1;      //Conversion to voltage
  float VR1 = 5 - VRT1;
  float RT1 = VRT1 / (VR1 / 10000);               //Resistance of RT
  float ln1 = log(RT1 / R0v2);
  float TX1 = (1 / ((ln1 / B) + (1 / T0))); //Temperature from thermistor
  TX1 = TX1 - 273.15;                 //Conversion to Celsius
  Serial.print("Temperature : ");
  Serial.println(TX1);


  //THERMISTANCEv22
  float VRT2 = analogRead(A2);              //Acquisition analog value of VRT
  VRT2 = (5.00 / 1023.00) * VRT2;      //Conversion to voltage
  float VR2 = 5 - VRT2;
  float RT2 = VRT2 / (VR2 / 10000);               //Resistance of RT
  float ln2 = log(RT2 / R0v2);
  float TX2 = (1 / ((ln2 / B) + (1 / T0))); //Temperature from thermistor
  TX2 = TX2 - 273.15;                 //Conversion to Celsius
  Serial.print("Temperature : ");
  Serial.println(TX2);


}




