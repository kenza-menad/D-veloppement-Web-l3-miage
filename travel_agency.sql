-- Créer la base de données
CREATE DATABASE travel_agency;

-- Se connecter à la base de données
\c travel_agency;

-- Création des tables
CREATE TABLE utilisateurs (
    id_utilisateur SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    mot_de_passe VARCHAR(255) NOT NULL, -- Stockez les mots de passe hashés
    telephone VARCHAR(20),
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE destination (
    id_destination SERIAL PRIMARY KEY, -- Identifiant unique de chaque destination
    nom VARCHAR(100) NOT NULL,                    -- Nom de la destination
    description TEXT NOT NULL,                    -- Description de la destination
    image_url VARCHAR(255),                       -- Lien vers l'image principale de la destination
    prix_moyen NUMERIC(10, 2),                    -- Prix moyen par personne pour visiter cette destination
    duree_moyenne VARCHAR(50),                    -- Durée moyenne des séjours
    devise VARCHAR(50),                           -- Devise utilisée sur place
    temps_vol VARCHAR(50),                        -- Temps de vol moyen
    decalage_horaire VARCHAR(50),                 -- Décalage horaire
    attractions TEXT,                             -- Attractions principales ou raisons de visiter
    guide_pratique TEXT,                          -- Conseils pratiques
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de création de l'enregistrement
);

CREATE TABLE sejours (
    id_sejour SERIAL PRIMARY KEY,                -- Identifiant unique du séjour
    id_destination INT NOT NULL REFERENCES destination(id_destination), -- Référence à la destination
    nom VARCHAR(255) NOT NULL,                   -- Nom du séjour ou de l'hôtel
    location VARCHAR(255) NOT NULL,              -- Localisation du séjour
    image_url VARCHAR(255),                      -- URL de l'image associée
    categorie VARCHAR(50),                       -- Catégorie du séjour
    lien_detail VARCHAR(255),                    -- Lien vers la page de détails
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de création de l'enregistrement
);

CREATE TABLE hotel (
    id_hotel SERIAL PRIMARY KEY,                -- Identifiant unique pour chaque hôtel
    id_destination INT NOT NULL REFERENCES destination(id_destination), -- Référence à la destination
    nom VARCHAR(255) NOT NULL,                  -- Nom de l'hôtel
    localisation VARCHAR(255) NOT NULL,         -- Localisation détaillée de l'hôtel
    meilleures_periodes VARCHAR(255),           -- Meilleures périodes pour visiter
    aeroport_proche VARCHAR(255),               -- Aéroport le plus proche
    transfert VARCHAR(255),                     -- Détails du transfert
    description TEXT,                           -- Description détaillée de l'hôtel
    prix_min NUMERIC(10, 2),                    -- Prix minimum
    prix_max NUMERIC(10, 2),                    -- Prix maximum
    lien_reservation VARCHAR(255),             -- Lien vers la page de réservation
    image_video VARCHAR(255),                  -- Lien vers l'image ou la vidéo de fond
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de création de l'enregistrement
);

CREATE TABLE voyage (
    id_voyage SERIAL PRIMARY KEY,
    id_destination INT NOT NULL REFERENCES destination(id_destination),
    titre VARCHAR(255) NOT NULL,
    localisation VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    lien_reservation VARCHAR(255) NOT NULL
);

CREATE TABLE reservation (
    id_reservation SERIAL PRIMARY KEY,           -- Identifiant unique pour chaque réservation
    id_utilisateur INT REFERENCES utilisateurs(id_utilisateur), -- Référence à l'utilisateur
    id_voyage INT REFERENCES voyage(id_voyage),  -- Référence au voyage réservé
    nom VARCHAR(100) NOT NULL,                   -- Nom de la personne réservant
    prenom VARCHAR(100) NOT NULL,                -- Prénom de la personne réservant
    email VARCHAR(150) NOT NULL,                 -- Email de contact
    telephone VARCHAR(20),                       -- Numéro de téléphone
    pays_residence VARCHAR(100),                 -- Pays de résidence
    code_postal VARCHAR(20),                     -- Code postal
    type_rendez_vous VARCHAR(50) CHECK (type_rendez_vous IN ('Téléphone', 'Vidéo')), -- Type de rendez-vous
    date_rendez_vous DATE,                       -- Date du rendez-vous
    heure_rendez_vous TIME,                      -- Heure du rendez-vous
    date_depart DATE NOT NULL,                   -- Date de départ
    date_retour DATE,                            -- Date de retour
    nb_adultes INT NOT NULL,                     -- Nombre d'adultes
    nb_enfants INT NOT NULL,                     -- Nombre d'enfants
    nb_bebes INT NOT NULL,                       -- Nombre de bébés
    classe VARCHAR(50) NOT NULL,                 -- Classe choisie
    bagages_main INT NOT NULL,                   -- Nombre de bagages à main
    bagages_soute INT NOT NULL,                  -- Nombre de bagages en soute
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de création de la réservation
);

CREATE TABLE paiement (
    id_paiement SERIAL PRIMARY KEY,             -- Identifiant unique pour chaque paiement
    id_reservation INT NOT NULL REFERENCES reservation(id_reservation), -- Référence à la réservation associée
    montant NUMERIC(10, 2) NOT NULL,            -- Montant total du paiement
    method_paiement VARCHAR(50) NOT NULL,       -- Méthode de paiement
    numero_carte VARCHAR(16) NOT NULL,          -- Numéro de carte
    nom_titulaire VARCHAR(255) NOT NULL,        -- Nom du titulaire de la carte
    date_expiration VARCHAR(7) NOT NULL,        -- Date d'expiration de la carte
    cvc VARCHAR(3) NOT NULL,                    -- CVC
    adresse_facturation_ligne1 VARCHAR(255) NOT NULL, -- Adresse de facturation ligne 1
    adresse_facturation_ligne2 VARCHAR(255),    -- Adresse de facturation ligne 2
    code_postal VARCHAR(20) NOT NULL,           -- Code postal
    ville VARCHAR(100) NOT NULL,                -- Ville
    pays VARCHAR(100) NOT NULL,                 -- Pays
    email_contact VARCHAR(150) NOT NULL,        -- Email de contact
    telephone_contact VARCHAR(20),              -- Téléphone de contact
    statut VARCHAR(50) CHECK (statut IN ('En attente', 'Validé', 'Échoué')) DEFAULT 'En attente' -- Statut du paiement
);

CREATE TABLE contact (
    id_contact SERIAL PRIMARY KEY,              -- Identifiant unique pour chaque contact
    nom VARCHAR(100) NOT NULL,                  -- Nom de l'utilisateur
    email VARCHAR(150) NOT NULL,                -- Adresse email
    probleme TEXT NOT NULL                      -- Problème ou demande soumis par l'utilisateur
);

CREATE TABLE avis (
    id_avis SERIAL PRIMARY KEY,                 -- Identifiant unique pour chaque avis
    nom VARCHAR(100) NOT NULL,                  -- Nom de l'utilisateur
    prenom VARCHAR(100) NOT NULL,               -- Prénom de l'utilisateur
    adresse VARCHAR(255) NOT NULL,              -- Adresse postale
    email VARCHAR(150) NOT NULL,                -- Email de l'utilisateur
    pays VARCHAR(100) NOT NULL,                 -- Pays d'origine
    departement VARCHAR(100) NOT NULL,          -- Département de domicile
    code_postal VARCHAR(20) NOT NULL,           -- Code postal
    avis TEXT NOT NULL,                         -- Texte de l'avis
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de soumission de l'avis
);
