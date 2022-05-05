# coding: UTF-8
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector

def Ajouter():
    id = Id_Entry.get()
    nom = Nom_Entry.get()
    prenom = Prenom_Entry.get()
    pathologie = comboClasse.get()
    date = Date_Entry.get()
    telephone = Tel_Entry.get()

    connexionMySQL = mysql.connector.connect(host="localhost", port='3306', database="test_DeskApp", user="root", password="")
    curseur = connexionMySQL.cursor()

    try:
        sql = """INSERT INTO Note(id, nom, prenom, date, pathologie, telephone)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (id, nom, prenom, date, pathologie, telephone)
        curseur.execute(sql, val)
        connexionMySQL.commit()
        derniereid = curseur.lastrowid
        messagebox.showinfo("information", "Note ajouter")
        root.destroy()
        call(["python", "Registre.py"]) #Réactualiser la page Chambre2

    except Exception as e:
        print(e)
        #retour
        connexionMySQL.rollback()
        connexionMySQL.close()

def Modifier():
    id = Id_Entry.get()
    nom = Nom_Entry.get()
    prenom = Prenom_Entry.get()
    pathologie = comboClasse.get()
    date = Date_Entry.get()
    telephone = Tel_Entry.get()

    connexionMySQL = mysql.connector.connect(
        host="localhost", user="root", password="", database="test_DeskApp")
    curseur = connexionMySQL.cursor()

    try:
        sql = "UPDATE Note set nom=%s, prenom=%s, date=%s, pathologie=%s, telephone=%s WHERE id=%s "
        val = (nom, prenom, date, pathologie, telephone, id)
        curseur.execute(sql, val)
        connexionMySQL.commit()
        derniereid = curseur.lastrowid
        messagebox.showinfo("information", "Note ajouter")
        root.destroy()
        call(["python", "Registre.py"])
    except Exception as e:
        print(e)
        #retour
        connexionMySQL.rollback()
        connexionMySQL.close()

def Supprimer():
    id = Id_Entry.get()

    connexionMySQL = mysql.connector.connect(
        host="localhost", user="root", password="", database="test_DeskApp")
    curseur = connexionMySQL.cursor()

    try:
        sql = "DELETE FROM Personne WHERE id=%s"
        val = (id,)
        curseur.execute(sql, val)
        connexionMySQL.commit()
        derniereid = curseur.lastrowid
        messagebox.showinfo("information", "Note Supprimer")
        root.destroy()
        call(["python", "Registre.py"])
    except Exception as e:
        print(e)
        #retour
        connexionMySQL.rollback()
        connexionMySQL.close()

#Ma fenetre
root = Tk()

root.title("MENU PRINCIPAL")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#091821")

#Ajouter le titre
Titre_Label = Label(root, borderwidth=3, relief=SUNKEN, text="REGISTRE DE SANTÉ DES PATIENTS", font=(
    "Sans Serif", 25), background="#2F4F4F", foreground="#FFFAFA")
Titre_Label.place(x=0, y=0, width=1350, height=100)

#ID
Id_Label = Label(root, text="ID", font=("Arial", 18), bg="#091821", fg="white")
Id_Label.place(x=70, y=150, width=150)
Id_Entry = Entry(root, bd=4, font=("Arial", 14))
Id_Entry.place(x=250, y=150, width=150)

#Nom
Nom_Label = Label(root, text="NOM", font=(
    "Arial", 18), bg="#091821", fg="white")
Nom_Label.place(x=70, y=200, width=150)
Nom_Entry = Entry(root, bd=4, font=("Arial", 14))
Nom_Entry.place(x=250, y=200, width=300)

#Prenom
Prenom_Label = Label(root, text="PRENOM", font=(
    "Arial", 18), bg="#091821", fg="white")
Prenom_Label.place(x=70, y=250, width=150)
Prenom_Entry = Entry(root, bd=4, font=("Arial", 14))
Prenom_Entry.place(x=250, y=250, width=300)


# datenaissance = valeurSexe.get()
# telephone = comboClasse.get()

#DATE
Date_Label = Label(root, text="DATE", font=("Arial", 18), bg="#091821", fg="white")
Date_Label.place(x=70, y=250, width=150, )
Date_Entry = Entry(root, bd=4, font=("Arial", 14))
Date_Entry.place(x=250, y=400, width=300)

#PATHOLOGIE
Pathologie_Label = Label(root, text="PATHOLOGIE", font=(
    "Arial", 18), bg="#091821", fg="white")
Pathologie_Label.place(x=70, y=300, width=150, )

comboClasse = ttk.Combobox(root, font=("arial", 14))
comboClasse['values'] = ['alzeihmzer', 'AVC', 'Autisme', 'Trisomie']
comboClasse.place(x=250, y=300, width=130)


#TEL
# Tel_Label = Label(root, text="TÉLEPHONE", font=("Arial", 18), bg="#091821", fg="white")
# Tel_Label.place(x=70, y=450, width=150)
# Tel_Entry = Entry(root, bd=4, font=("Arial", 14))
# Tel_Entry.place(x=250, y=450, width=300)


#Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font="Arial 16 bold",
                        bg="white", fg="#D2691E")  # , command=Ajouter)
btnenregistrer.place(x=250, y=500, width=200)

#modifier
btnmodifier = Button(root, text="Modifier", font="Arial 16 bold", bg="white", fg="#D2691E")  # , command=Modifier)
btnmodifier.place(x=250, y=550, width=200)

#Supprimer
btnSupprimer = Button(root, text="Supprimer", font="Arial 16 bold",
                      bg="white", fg="#D2691E")  # , command=Supprimer)
btnSupprimer.place(x=250, y=600, width=200)

#Table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), height=5, show="headings")
table.place(x=560, y=150, width=790, height=450)

#Entête
table.heading(1, text="ID")
table.heading(2, text="NOM")
table.heading(3, text="PRENOM")
table.heading(4, text="DATE")
table.heading(5, text="PATHOLOGIE")
table.heading(6, text="TEL")


#id_soignant	nom_soignant	prenom_soignant	datenaissance_soignant	motdepasse_soignant	poste_soignant	mail_soignant

#definir les dimentions des colonnes
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=100)


#afficher les informations de la table
# connexionMySQL = mysql.connector.connect(host="localhost", user="root", password="", database="test_DeskApp")
# curseur = connexionMySQL.cursor()
# curseur.execute("SELECT * FROM Personne")
# myResult = curseur.fetchall()
# for row in myResult:
#     table.insert('', END, value=row)
# connexionMySQL.close()

#Execution
root.mainloop()
