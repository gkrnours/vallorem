drop table if exists personne;
create table personne (
	id integer primary key autoincrement,
	nom text not null,
	prenom text not null,
	statut integer not null,
	equipe integer not null,
	date_recrutement numeric not null,
	permanent numeric not null
);

drop table if exists statut;
create table statut (
	id integer primary key autoincrement,
	description text not null
);

drop table if exists equipe;
create table statut (
	id integer primary key autoincrement,
	nom text not null,
	axe text not null
);

drop table if exists PRV;
create table PRV (
	id integer primary key autoincrement,
	description text not null,
	annee numeric not null,
	type integer not null
);

drop table if exists publication;
create table publication (
	id integer primary key autoincrement,
	description text not null,
	annee numeric not null,
	type integer not null
);

drop table if exists type_publication;
create table type (
	id integer primary key autoincrement,
	description text not null
);

drop table if exists type_PRV;
create table type (
	id integer primary key autoincrement,
	description text not null
);



drop table if exists HIST_personne;
create table HIST_personne (
	id integer primary key autoincrement,
	id_personne integer not null,
	nom text not null,
	prenom text not null,
	statut integer not null,
	equipe integer not null,
	date_recrutement numeric not null,
	permanent numeric not null,
	date_modification numeric not null
);

drop table if exists HIST_PRV;
create table PRV (
	id integer primary key autoincrement,
	id_PRV integer not null,
	description text not null,
	annee numeric not null,
	type integer not null,
	date_modification numeric not null
);

drop table if exists HIST_publication;
create table publication (
	id integer primary key autoincrement,
	id_publication integer not null,
	description text not null,
	annee numeric not null,
	type integer not null,
	personne integer not null,
	date_modification numeric not null
);

drop table if exists publication_personne;
create table publication_personne (
	id integer primary key autoincrement,
	id_publication integer not null,
	id_personne integer not null
);

drop table if exists PRV_personne;
create table publication_personne (
	id integer primary key autoincrement,
	id_PRV integer not null,
	id_personne integer not null
);

drop table if exists HIST_publication_personne;
create table publication_personne (
	id integer primary key autoincrement,
	id_publication_personne integer not null,
	id_publication integer not null,
	id_personne integer not null,
	date_modification numeric not null
);

drop table if exists HIST_PRV_personne;
create table publication_personne (
	id integer primary key autoincrement,
	id_PRV_personne integer not null,
	id_PRV integer not null,
	id_personne integer not null,
	date_modification numeric not null
);