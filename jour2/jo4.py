import mysql.connector

# coding=utf-8
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="brahimab9",
    database="LaPlateforme"
)
cursor = conn.cursor()

cursor.execute('SELECT SUM(capacite) AS capacite_totale FROM salle')
result = cursor.fetchone()
capacite_totale = result[0]

# Affichage du résultat en console
print(f"La capacité totale des salles est de {capacite_totale}")

# Fermeture de la connexion à la base de données
conn.close()