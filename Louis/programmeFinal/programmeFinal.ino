#include <max6675.h>
#include <Adafruit_MAX31865_PT100.h>

//Pour sonde PT100
#define RREF      430.0  //Résistance de référence
#define RNOMINAL  100.0  //Résistance nominale

/*
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
*/

enum{
  thermoSO1 = 22, thermoCS1, thermoSCK1,     //THERMOCOUPLE ENTREE DETENDEUR
  thermoSO2, thermoCS2, thermoSCK2,          //THERMOCOUPLE SORTIE DETENDEUR
  thermoSO3, thermoCS3, thermoSCK3,          //THERMOCOUPLE ENTREE COMPRESSEUR
  thermoSO4, thermoCS4, thermoSCK4,          //THERMOCOUPLE SORTIE COMPRESSEUR
  thermoSO5, thermoCS5, thermoSCK5,          //THERMOCOUPLE ENTREE CONDENSEUR
  thermoSO6, thermoCS6, thermoSCK6,          //THERMOCOUPLE SORTIE CONDENSEUR
  thermoSO7, thermoCS7, thermoSCK7,          //THERMOCOUPLE SORTIE EVAPORATEUR
  pt100CS = 4, pt100SDI, pt100SDO, pt100CLK  //PT100 EAU
};



//CAPTEURS PRESSION
const int capteurBassePression = A14;
const int capteurHautePression = A15;


//Initialisation des amplificateurs MAX6675 pour les thermocouples
MAX6675 thermocoupleEntreeDetendeur(thermoSCK1, thermoCS1, thermoSO1);
MAX6675 thermocoupleSortieDetendeur(thermoSCK2, thermoCS2, thermoSO2);
MAX6675 thermocoupleEntreeCompresseur(thermoSCK3, thermoCS3, thermoSO3);
MAX6675 thermocoupleSortieCompresseur(thermoSCK4, thermoCS4, thermoSO4);
MAX6675 thermocoupleEntreeCondenseur(thermoSCK5, thermoCS5, thermoSO5);
MAX6675 thermocoupleSortieCondenseur(thermoSCK6, thermoCS6, thermoSO6);
MAX6675 thermocoupleSortieEvaporateur(thermoSCK7, thermoCS7, thermoSO7);

//Initialisation des amplificateurs MAX31865 pour la sonde PT100
MAX31865 pt100 = MAX31865(pt100CS, pt100SDI, pt100SDO, pt100CLK);


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
      Serial.print("temperatureEau"); 
      Serial.println(pt100.temperature(RNOMINAL, RREF));
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
      Serial.print("bassePression");
      Serial.println(BassePression);
      delay(1000);

      float rawHautePression = analogRead(capteurHautePression);
      float HautePression = (34.5/818.4)*(rawHautePression-(1023*0.5/5));
      //Serial.println(rawHautePression);
      Serial.print("hautePression");
      Serial.println(HautePression);
      delay(1000);
   }

};

void setup() {
  Serial.begin(9600);
  pt100.begin(MAX31865_2WIRE);
  delay(500);
  
}

temperatureThermocouples T;
temperaturePT100 PT;
pressionCapteurs P;

void loop() {
  T.readTemperature();
  PT.readPT100();
  P.readPression();
  Serial.flush();

}