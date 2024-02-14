import tkinter as tk
from tkinter import Tk, ttk
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="brahimab9",
    database="store"
)
mycursor = mydb.cursor()

# Fonctions pour interagir avec la base de données
def insert_product(name, description, price, quantity, category_id):
    sql = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
    val = (name, description, price, quantity, category_id)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Product added successfully")

def delete_product(id):
    sql = "DELETE FROM product WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Product deleted successfully")

def update_product(id, quantity, price):
    sql = "UPDATE product SET quantity = %s, price = %s WHERE id = %s"
    val = (quantity, price, id)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Product updated successfully")

def display_products():
    mycursor.execute("SELECT * FROM product")
    products = mycursor.fetchall()
    for product in products:
        print(product)


class Produit:
         # Fonction pour valider l'ajout de produit
    def ajout(libelle: str, description:str, prix:str, quantite:str):
        # Vérifier que tous les champs sont remplis
        if not libelle or not prix or not quantite:
            return "error"
        
        # Vérifier que le prix et la quantité sont des nombres valides
        try:
            prix = float(prix)
            quantite = int(quantite)
        except ValueError:
            return "error"
        
        # Insérer le code pour ajouter le produit à la base de données
        print("Libellé produit:", libelle)
        print("Description:", description)
        print("Prix:", prix)
        print("Quantité:", quantite)
        
# Fonction pour ajouter un produit
def ajouter_produit():
    fenetre_ajout = tk.Toplevel(root)
    fenetre_ajout.title("Ajouter produit")
    fenetre_ajout.geometry("400x180") 
    fenetre_ajout.resizable(False, False)
        # Fonction pour valider l'ajout de produit
    def valider_ajout():
        libelle = libelle_entry.get()
        description = description_entry.get()
        prix = prix_entry.get()
        quantite = quantite_entry.get()
        #  tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        
        produit = Produit()
        produit.ajout(libelle,description,prix,quantite)
        
        # Fermer la fenêtre d'ajout de produit
        fenetre_ajout.destroy()

    # Créer les widgets du formulaire d'ajout de produit
    tk.Label(fenetre_ajout, text="Libellé produit:").grid(row=0, column=0, padx=10, pady=10)
    libelle_entry = tk.Entry(fenetre_ajout, width=42)
    libelle_entry.grid(row=0, column=1, padx=20, pady=5)

    tk.Label(fenetre_ajout, text="Description:").grid(row=1, column=0, padx=10, pady=5)
    description_entry = tk.Entry(fenetre_ajout, width=42)
    description_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(fenetre_ajout, text="Prix:").grid(row=2, column=0, padx=10, pady=5)
    prix_entry = tk.Entry(fenetre_ajout, width=42)
    prix_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(fenetre_ajout, text="Quantité:").grid(row=3, column=0, padx=10, pady=5)
    quantite_entry = tk.Entry(fenetre_ajout, width=42)
    quantite_entry.grid(row=3, column=1, padx=10, pady=5)

    # Boutons "Valider" et "Annuler"
    btn_valider = tk.Button(fenetre_ajout, text="Valider", command=valider_ajout)
    btn_valider.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    btn_annuler = tk.Button(fenetre_ajout, text="Annuler", command=fenetre_ajout.destroy)
    btn_annuler.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
    pass
 
 # Fonction pour modifier un produit

def modifier_produit():
    # Insérer le code pour modifier un produit dans la base de données
    
    fenetre_update = tk.Toplevel(root)
    fenetre_update.title("modifier produit")
    fenetre_update.geometry("400x180") 
    fenetre_update.resizable(False, False)

# Fonction pour valider l'ajout de produit
    def valider_update():
        id = id_entry.get()
        quantite = quantity_entry.get()
        prix = price_entry.get()
        
         #  tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        
        produit = Produit()
        produit.ajout(id,prix,quantite)
        
        # Fermer la fenêtre d'ajout de produit
        fenetre_update.destroy()

    tk.Label(fenetre_update, text="ID").grid(row=0, column=0)
    tk.Label(fenetre_update, text="Quantité").grid(row=1, column=0)
    tk.Label(fenetre_update, text="Prix").grid(row=2, column=0)

    id_entry = tk.Entry(fenetre_update, width=42)
    id_entry.grid(row=0, column=1)
    quantity_entry = tk.Entry(fenetre_update, width=42)
    quantity_entry.grid(row=1, column=1)
    price_entry = tk.Entry(fenetre_update, width=42)
    price_entry.grid(row=2, column=1)

    def valider_modifier():
        update_product(int(id_entry.get()), int(quantity_entry.get()), int(price_entry.get()))
        fenetre_update.destroy()

    btn_valider = tk.Button(fenetre_update, text="Valider", command=valider_update)
    btn_valider.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    pass
 
# Fonction pour supprimer un produit
def supprimer_produit():
    # Insérer le code pour supprimer un produit de la base de données
    fenetre_supprimer = tk.Toplevel(root)
    fenetre_supprimer.title("supprimer produit")
    fenetre_supprimer.geometry("400x180") 
    fenetre_supprimer.resizable(False, False)

    Tk.Label(fenetre_supprimer, text="Product ID").grid(row=0, column=0)
    id_entry = tk.Entry(fenetre_supprimer)
    id_entry.grid(row=0, column=1)

    def submit():
        delete_product(int(id_entry.get()))
        fenetre_supprimer.destroy()

    tk.Button(fenetre_supprimer, text="Submit", command=submit).grid(row=1, columnspan=2)

    pass


# Créer une fenêtre principale
root = tk.Tk()
root.title("Gestion des stocks")

# Créer une zone pour afficher la liste des produits
tree = ttk.Treeview(root, columns=('Nom', 'Description', 'Prix', 'Quantité'))
tree.heading('#0', text='ID')
tree.heading('Nom', text='Nom')
tree.heading('Description', text='Description')
tree.heading('Prix', text='Prix')
tree.heading('Quantité', text='Quantité')
tree.pack()

# Boutons pour ajouter, supprimer et modifier un produit
btn_ajouter = tk.Button(root, text="Ajouter produit", command=ajouter_produit)
btn_ajouter.pack()
btn_modifier = tk.Button(root, text="Modifier produit", command=modifier_produit)
btn_modifier.pack()
btn_supprimer = tk.Button(root, text="Supprimer produit", command=supprimer_produit)
btn_supprimer.pack()


# Exécuter la boucle principale
root.mainloop()
