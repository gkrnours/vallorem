DROP TABLE IF EXISTS personne;
CREATE TABLE personne (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nom TEXT NOT NULL,
	nom_jf TEXT,
	prenom TEXT NOT NULL,
	id_statut INTEGER NOT NULL,
	id_equipe INTEGER NOT NULL,
	date_naissance NUMERIC NOT NULL,
	date_recrutement NUMERIC NOT NULL,
	permanent NUMERIC NOT NULL,
	FOREIGN KEY(id_statut) REFERENCES statut(id),
	FOREIGN KEY(id_equipe) REFERENCES equipe(id)
);

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_mail TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	FOREIGN KEY(id_mail) REFERENCES mail(id)
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
	titre TEXT NOT NULL,
	description TEXT NOT NULL,
	extra TEXT,
	date NUMERIC NOT NULL,
	id_type INTEGER NOT NULL,
	FOREIGN KEY(id_type) REFERENCES type_production(id)
);


DROP TABLE IF EXISTS directeur_these;
CREATE TABLE directeur_these (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_doctorant INTEGER NOT NULL,
	id_directeur INTEGER NOT NULL,
	FOREIGN KEY(id_doctorant) REFERENCES personne(id),
	FOREIGN KEY(id_directeur) REFERENCES personne(id)
);

DROP TABLE IF EXISTS doctorant;
CREATE TABLE doctorant (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_personne INTEGER NOT NULL,
	id_type_financement INTEGER NOT NULL,
	sujet_these TEXT NOT NULL,
	nombre_ia INTEGER,
	date_soutenance NUMERIC,
	id_observation INTEGER NOT NULL,
	FOREIGN KEY(id_personne) REFERENCES personne(id),
	FOREIGN KEY(id_type_financement) REFERENCES type_financement(id),
	FOREIGN KEY(id_observation) REFERENCES observation(id)
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
	id_production INTEGER NOT NULL,
	id_personne INTEGER NOT NULL,
	FOREIGN KEY(id_production) REFERENCES production(id),
	FOREIGN KEY(id_personne) REFERENCES personne(id)
);

DROP TABLE IF EXISTS user_personne;
CREATE TABLE user_personne (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_user INTEGER NOT NULL,
	id_personne INTEGER NOT NULL,
	FOREIGN KEY(id_user) REFERENCES user(id),
	FOREIGN KEY(id_personne) REFERENCES personne(id)
);


DROP TABLE IF EXISTS date_promotion;
CREATE TABLE date_promotion (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_personne INTEGER NOT NULL,
	id_statut NUMERIC NOT NULL,
	date_promotion NUMERIC NOT NULL,
	FOREIGN KEY(id_personne) REFERENCES personne(id),
	FOREIGN KEY(id_statut) REFERENCES statut(id)
);

DROP TABLE IF EXISTS mail;
CREATE TABLE mail (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	mail TEXT NOT NULL
);

DROP TABLE IF EXISTS mail_personne;
CREATE TABLE mail_personne (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_personne INTEGER NOT NULL,
	id_mail INTEGER NOT NULL,
	FOREIGN KEY(id_personne) REFERENCES personne(id),
	FOREIGN KEY(id_mail) REFERENCES mail(id)
);

DROP TABLE IF EXISTS chg_equipe;
CREATE TABLE chg_equipe (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_personne INTEGER NOT NULL,
	id_equipe INTEGER NOT NULL,
	date_chg NUMERIC NOT NULL,
	FOREIGN KEY(id_personne) REFERENCES personne(id),
	FOREIGN KEY(id_equipe) REFERENCES equipe(id)
);

DROP TABLE IF EXISTS page;
CREATE TABLE page (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	titre TEXT NOT NULL,
	id_categorie INTEGER NOT NULL,
	content TEXT NOT NULL,
	FOREIGN KEY(id_categorie) REFERENCES categorie(id)
);

DROP TABLE IF EXISTS categorie;
CREATE TABLE categorie (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL
);
