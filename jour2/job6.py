import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
   host="127.0.0.1",
    user="root",
    password="brahimab9",
    database="LaPlateforme"
)
cursor = conn.cursor()

# Exécution de la requête SQL pour calculer la superficie totale des étages
cursor.execute('SELECT SUM(superficie) AS superficie_totale FROM etage')

# Récupération du résultat
result = cursor.fetchone()
superficie_totale = result[0]

# Affichage du résultat en console
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermeture de la connexion à la base de données
conn.close()
