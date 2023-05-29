// Inclusion des bibliothèques pour les capteurs MAX6675 et PT100
#include <max6675.h>
#include <Adafruit_MAX31865_PT100.h>

//Pour sonde PT100
#define RREF      430.0  //Résistance de référence
#define RNOMINAL  100.0  //Résistance nominale

//Temps en minute pour l'état stable
#define tempsEtatStable 10

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


// Assignation des broches pour les thermocouples et la sonde PT100 avec une énumération
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

// Définition de la classe pour le temps écoulé
class tempsEcoule
{
  public:
    float temps, tempsSecondes, tempsMinutes;
    float affichageTemps(){
      temps = millis();
      tempsSecondes = temps/1000;
      Serial.print("tempsSecondes");
      Serial.println(tempsSecondes, 0);
      delay(1000);

      tempsMinutes = temps/1000/60;
      Serial.print("tempsMinutes");
      Serial.println(tempsMinutes);
      delay(1000);
    }

};


// Définition de la classe pour les températures des thermocouples
class temperatureThermocouples
{
  public:
    float readTemperature(){
      const int numThermocouples = 7;
      int thermoSO[] = {thermoSO1, thermoSO2, thermoSO3, thermoSO4, thermoSO5, thermoSO6, thermoSO7};
      int thermoCS[] = {thermoCS1, thermoCS2, thermoCS3, thermoCS4, thermoCS5, thermoCS6, thermoCS7};
      int thermoSCK[] = {thermoSCK1, thermoSCK2, thermoSCK3, thermoSCK4, thermoSCK5, thermoSCK6, thermoSCK7};
      MAX6675 *thermocouples[] = {&thermocoupleEntreeDetendeur, &thermocoupleSortieDetendeur, 
                                  &thermocoupleEntreeCompresseur, &thermocoupleSortieCompresseur, 
                                  &thermocoupleEntreeCondenseur, &thermocoupleSortieCondenseur, 
                                  &thermocoupleSortieEvaporateur};
      const char *thermocoupleNames[] = {"temperatureEntreeDetendeur", "temperatureSortieDetendeur", 
                                         "temperatureEntreeCompresseur", "temperatureSortieCompresseur",
                                         "temperatureEntreeCondenseur", "temperatureSortieCondenseur", 
                                         "temperatureSortieEvaporateur"};
      for (int i = 0; i < numThermocouples; i++) {
        Serial.print(thermocoupleNames[i]);
        Serial.println(thermocouples[i]->readCelsius());
        delay(1000);
      }
    }
};

// Définition de la classe pour les température de la sonde PT100
class temperaturePT100
{
  public:
    bool valeurAjoutee1 = false, valeurAjoutee2 = false;
    float tempInitiale, tempFinale;
    // Lecture de la température pour la sonde PT100
    float readTemperaturePT100(tempsEcoule tempsPT100){
      float tempEau = pt100.temperature(RNOMINAL, RREF);
      Serial.print("temperatureEau"); 
      Serial.println(tempEau);
      delay(1000);

      // Assignation à une variable tempInitiale de la température de l'eau à 0min
      if(tempsPT100.tempsMinutes >= 0 && !valeurAjoutee1){
        tempInitiale = tempEau;
        valeurAjoutee1 = true;
      }

      // Assignation à une variable tempFinale de la température de l'eau à l'état stable, et calcul et affichage du COP réel
      if(tempsPT100.tempsMinutes >= tempsEtatStable && !valeurAjoutee2){
        tempFinale = tempEau;
        valeurAjoutee2 = true;
        Serial.print("copReel");
        Serial.println((18*4185*(tempFinale-tempInitiale))/(29.8*tempsEtatStable));
        delay(1000);
      }
    
    }

};

// Définition de la classe pour les basses et hautes pressions des capteurs de pressions
class pressionCapteurs
{
  public :
    // Lecture et conversion des valeurs brutes de capteurs de pressions 
    float readPression(){
      float rawBassePression = analogRead(capteurBassePression);
      float BassePression = (7.3/818.4)*(rawBassePression-(1023*0.5/5));
      //Serial.println(rawBassePression);
      Serial.print("bassePression");
      Serial.println(BassePression+1);
      delay(1000);

      float rawHautePression = analogRead(capteurHautePression);
      float HautePression = (34.5/818.4)*(rawHautePression-(1023*0.5/5));
      //Serial.println(rawHautePression);
      Serial.print("hautePression");
      Serial.println(HautePression+1);
      delay(1000);
   }

};


void setup() {
  Serial.begin(9600);
  //Initialisation de l'amplificateur MAX31865 pour la sonde PT100 (2 fils)
  pt100.begin(MAX31865_2WIRE);
  delay(500);
  
}

tempsEcoule temps;
temperatureThermocouples thermocouples;
temperaturePT100 temperatureEau;
pressionCapteurs pression;

void loop() {
  thermocouples.readTemperature();
  temperatureEau.readTemperaturePT100(temps);
  pression.readPression();
  temps.affichageTemps();
  
}
