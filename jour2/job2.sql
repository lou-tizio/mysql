CREATE TABLE etage ( 
id int primary key auto_increment, 
nom varchar(255),
numero int,
superficie int);

CREATE TABLE salle(
 id int primary key auto_increment, 
 nom varchar(255), 
 id_etage int, 
 capacite int);
