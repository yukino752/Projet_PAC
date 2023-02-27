-- SQLite

PRAGMA foreign_key = ON;

DROP TABLE IF EXISTS Capteurs;
DROP TABLE IF EXISTS Donnees_recu;

CREATE TABLE IF NOT EXISTS Capteurs (
    id INTEGER   PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom_Capteur VARCHAR(150) NOT NULL
);
 
INSERT INTO Capteurs (nom_Capteur)
VALUES
    ('Compresseur'),
    ('Condenseur'),
    ('Detendeur'),
    ('Evaporateur'),
    ('Eau'),
    ('Tension'),
    ('Intensite');


CREATE TABLE IF NOT EXISTS Donnees_recu (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Temperature_Entree float,
    Temperature_Sortie float,
    Haute_Pression float,
    Basse_Pression float,
    Temperature_Avant float,
    Temperature_Apres float,
    Volt float,
    Ampere float,
    Capteur_nom VARCHAR(50),
    FOREIGN KEY (Capteur_nom) REFERENCES Capteurs (nom_Capteur)
);



INSERT INTO Donnees_recu (Temperature_Entree, Temperature_Sortie,
Haute_Pression, Basse_Pression, Temperature_Avant, Temperature_Apres, Volt, Ampere, Capteur_nom)
VALUES
    (10.5, 15.5, 8, 7, NULL, NULL, NULL, NULL, 'Compresseur'),
    (NULL, NULL, NULL, NULL, NULL, NULL, 10, NULL, 'Tension'),
    (10.5, 15.5, NULL, NULL, NULL, NULL, NULL, NULL, 'Detendeur');

SELECT d.id, d.Temperature_Entree, d.Temperature_Sortie,
d.Haute_Pression, d.Basse_Pression, 
d.Temperature_Avant, d.Temperature_Apres, d.Volt, d.Ampere, 
d.Capteur_nom AS Capteur
FROM Donnees_recu d 
LEFT JOIN Capteurs c ON d.Capteur_nom = c.nom_Capteur;

/*
DELETE FROM categories WHERE id = 2;

SELECT * FROM recipes;
SELECT * FROM categories;
/*
