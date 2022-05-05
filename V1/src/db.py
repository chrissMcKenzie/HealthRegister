# coding: UTF-8
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector


def connexion():
    try:
        connexionMySQL = mysql.connector.connect(
            host="localhost", user="root", password="", database="test_DeskApp")
        print("Connexion à la base de donnée...")
        return connexionMySQL
    except:
        print("Echec #=> Connexion DB !!")


def Ajouter(Personne):
    connexionMySQL = connexion()
    curseur = connexionMySQL.cursor()

    valeurs = (Personne.prenom, Personne.nom, Personne.photo)

    # id = txtNumero.get()
    # nom = txtnom.get()
    # prenom = txtprenom.get()
    # datenaissance = valeurSexe.get()
    # telephone = comboClasse.get()

    curseur.execute("""INSERT INTO Personne(prenom, nom, photo)
                       VALUES(%s, %s, %s)""", valeurs)

    connexionMySQL.close()

def Parcourrir():
    connexionMySQL = connexion()
    curseur = connexionMySQL.cursor()

    curseur.execute("""SELECT * FROM Personne""")
    rows = curseur.fetchall()
    return rows

    #connexionMySQL.close()

def Supprimer(id):
    connexionMySQL = connexion()
    curseur = connexionMySQL.cursor()

    curseur.execute(f"""DELETE FROM Personne WHERE id = {id})""")

    connexionMySQL.close()
