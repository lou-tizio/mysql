INSERT INTO ETAGE (id, nom, numero, superficie) values
	(1, 'RDC', 0, 500),
    (2, 'R+1', 1, 500);
    
INSERT INTO salle (id, nom, id_etage, capacite) VALUES
	(1, 'Loungeé', 1, 100),
    (2, 'Studio Son', 1, 5),
    (3, 'Broadcasting', 2, 50),
    (4, 'Bocal Peda', 2, 4),
    (5, 'Coworking', 2, 80),
    (6, 'Studio Video', 2, 5);
    
    use LaPlateforme;