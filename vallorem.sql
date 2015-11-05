DROP TABLE IF EXISTS personne;
CREATE TABLE personne (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nom TEXT NOT NULL,
	prenom TEXT NOT NULL,
	mail TEXT NOT NULL,
	statut INTEGER NOT NULL,
	equipe INTEGER NOT NULL,
	date_recrutement NUMERIC NOT NULL,
	permanent NUMERIC NOT NULL,
	FOREIGN KEY(statut) REFERENCES statut(id),
	FOREIGN KEY(equipe) REFERENCES equipe(id)
);

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	email TEXT NOT NULL,
	password TEXT NOT NULL
);

DROP TABLE IF EXISTS statut;
CREATE TABLE statut (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL
);

DROP TABLE IF EXISTS equipe;
CREATE TABLE equipe (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nom TEXT NOT NULL,
	axe TEXT NOT NULL,
	localisation TEXT NOT NULL
);


DROP TABLE IF EXISTS production;
CREATE TABLE production (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL,
	annee NUMERIC NOT NULL,
	type INTEGER NOT NULL,
	FOREIGN KEY(type) REFERENCES type_production(id)
);


DROP TABLE IF EXISTS directeur_these;
CREATE TABLE directeur_these (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	doctorant INTEGER NOT NULL,
	directeur INTEGER NOT NULL,
	FOREIGN KEY(doctorant) REFERENCES personne(id),
	FOREIGN KEY(directeur) REFERENCES personne(id)
);

DROP TABLE IF EXISTS doctorant;
CREATE TABLE doctorant (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	personne INTEGER NOT NULL,
	type_financement INTEGER NOT NULL,
	sujet_these TEXT NOT NULL,
	nombre_ia INTEGER,
	annee_soutenance NUMERIC,
	observation INTEGER NOT NULL,
	FOREIGN KEY(personne) REFERENCES personne(id),
	FOREIGN KEY(type_financement) REFERENCES type_financement(id),
	FOREIGN KEY(observation) REFERENCES observation(id)
);

DROP TABLE IF EXISTS observation;
CREATE TABLE observation (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL
);

DROP TABLE IF EXISTS type_financement;
CREATE TABLE type_financement (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL
);


DROP TABLE IF EXISTS type_production;
CREATE TABLE type_production (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL,
	publication NUMERIC NOT NULL
);

DROP TABLE IF EXISTS production_personne;
CREATE TABLE production_personne (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	production INTEGER NOT NULL,
	personne INTEGER NOT NULL,
	FOREIGN KEY(production) REFERENCES production(id),
	FOREIGN KEY(personne) REFERENCES personne(id)
);

DROP TABLE IF EXISTS user_personne;
CREATE TABLE user_personne (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user INTEGER NOT NULL,
	personne INTEGER NOT NULL,
	FOREIGN KEY(user) REFERENCES user(id),
	FOREIGN KEY(personne) REFERENCES personne(id)
);

DROP TABLE IF EXISTS categorie;
CREATE TABLE categorie (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL
);

DROP TABLE IF EXISTS page;
CREATE TABLE page (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	titre TEXT NOT NULL,
	categorie INTEGER NOT NULL,
	content TEXT NOT NULL,
	FOREIGN KEY(categorie) REFERENCES categorie(id)
);

DROP TABLE IF EXISTS HIST_personne_statut;
CREATE TABLE HIST_personne_statut (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_personne INTEGER NOT NULL,
	statut INTEGER NOT NULL,
	date_modification NUMERIC NOT NULL,
	FOREIGN KEY(id_personne) REFERENCES personne(id),
	FOREIGN KEY(statut) REFERENCES statut(id)
);

DROP TABLE IF EXISTS HIST_personne_equipe;
CREATE TABLE HIST_personne_equipe (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_personne INTEGER NOT NULL,
	equipe INTEGER NOT NULL,
	date_modification NUMERIC NOT NULL,
	FOREIGN KEY(id_personne) REFERENCES personne(id),
	FOREIGN KEY(equipe) REFERENCES equipe(id)
);