#include <time.h>


class temperature
{
    public:

    float TempVentilateur(){
        float TempEntree = 18 + rand()/float((RAND_MAX)) * 1;
        float TempSortie = 15 + rand()/float((RAND_MAX)) * 1;
        Serial.print("Temperatures ventilateur :");
        Serial.println();
        Serial.print(TempEntree); Serial.print("°C");
        Serial.println();
        Serial.print(TempSortie); Serial.print("°C");
        Serial.println();
        float TempEntreeVentilateur = TempEntree;
        float TempSortieVentilateur = TempSortie;
        return 0;
    }
    
    float TempEau(){
        float TempEntree = 27 + rand()/float((RAND_MAX)) * 1;
        float TempSortie = 30 + rand()/float((RAND_MAX)) * 1;
        Serial.print("Temperatures eau :");
        Serial.println();
        Serial.print(TempEntree); Serial.print("°C");
        Serial.println();
        Serial.print(TempSortie); Serial.print("°C");
        Serial.println();
        float TempEntreeEau = TempEntree;
        float TempSortieEau = TempSortie;
        return 0;
    }

    float TempCompresseur(){
        float TempEntree = 9 + rand()/float((RAND_MAX)) * 1;
        float TempSortie = 33 + rand()/float((RAND_MAX)) * 1;
        Serial.print("Temperatures compresseur :");
        Serial.println();
        Serial.print(TempEntree); Serial.print("°C");
        Serial.println();
        Serial.print(TempSortie); Serial.print("°C");
        Serial.println();
        float TempEntreeCompresseur = TempEntree;
        float TempSortieCompresseur = TempSortie;
        return 0;
    }

    float TempDetendeur(){
        float TempEntree = 24 + rand()/float((RAND_MAX)) * 1;
        float TempSortie = 8 + rand()/float((RAND_MAX)) * 1;
        Serial.print("Temperatures detendeur :");
        Serial.println();
        Serial.print(TempEntree); Serial.print("°C");
        Serial.println();
        Serial.print(TempSortie); Serial.print("°C");
        Serial.println();
        float TempEntreeDetendeur = TempEntree;
        float TempSortieDetendeur = TempSortie;
        return 0;
    }

};



class pression
{
    public:

    float PressionCompresseur(){
        float BassePression = 2 + rand()/float((RAND_MAX)) * 1;
        float HautePression = 7 + rand()/float((RAND_MAX)) * 1;
        Serial.print("Pressions compresseur :");
        Serial.println();
        Serial.print(BassePression); Serial.print("Pa");
        Serial.println();
        Serial.print(HautePression); Serial.print("Pa");
        Serial.println();
        return 0;
    }

};



class intensite_tension
{
    public:

    float IntensiteTension(){
        float Intensite = 2 + rand()/float((RAND_MAX)) * 2;
        float Tension = 5 + rand()/float((RAND_MAX)) * 5;
        Serial.print("Intensite :");
        Serial.println();
        Serial.print(Intensite); Serial.print("A");
        Serial.println();
        Serial.print("Tension :");
        Serial.println();
        Serial.print(Tension); Serial.print("V");
        Serial.println();
        return 0;
    }

};


temperature T;
pression P;
intensite_tension IT;

void setup() {
    Serial.begin(9600);
    srand(time(NULL));
}

void loop() {
    T.TempVentilateur();
    delay(2000);
    T.TempEau();
    delay(2000);
    T.TempCompresseur();
    delay(2000);
    T.TempDetendeur();
    delay(2000);
    P.PressionCompresseur();
    delay(2000);
    IT.IntensiteTension();
    delay(2000);
}

