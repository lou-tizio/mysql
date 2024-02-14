import mysql.connector

# coding=utf-8
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="brahimab9",
    database="LaPlateforme"
)
cursor = conn.cursor()

query = "SELECT nom, capacite FROM salle"
cursor.execute(query)
resultats = cursor.fetchall()

for resultat in resultats:
    [nom, capacite] = resultat
    print(f"Nom de la salle: {nom}, Capacité: {capacite}")
   

cursor.close()
conn.close()
