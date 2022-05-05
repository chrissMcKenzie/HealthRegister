# coding: UTF-8
#from logging import root
from subprocess import call
import tkinter as tk
from tkinter import ttk
#from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import messagebox
import mysql.connector
#from theardTkinter import Seconnecter

# - private (attribut de private)
# + public (attribut de public)
# # protected (attribut de protected)
# $ classe (attribut de class)


class App:
    window = tk.Tk()
    # title =

    def __init__(this):
        #window = tk.Tk()  # !window = tk()

        this.window_Config()
        this.Body()

        this.window.mainloop()

    def window_Config(this):
        #this.window
        # configure the window
        this.window.title("Python DeskApp Poo")
        this.window.geometry("500x100")
        this.window.configure(background="#091821")

    def Body(this):

        # label
        this.label = ttk.Label(this.window, text="Hello, Tkinter!")
        this.label.pack()

        # button
        this.button = ttk.Button(this.window, text='Click Me')
        this.button['command'] = this.window.button_clicked
        this.button.pack()

    #
        """tkinter methodes"""
    #
    def button_clicked(self):
        showinfo(title='Information', message="Hello, Tkinter!")


app = App()





#Fonction Connecter
# def Seconnecter():
#     surnom = Patient_Entry.get()
#     mdp = ModeDePasse_Entry.get()
#     if (surnom == "" and mdp == ""):
#         messagebox.showerror("", "il faut rentrer les Données")
#         ModeDePasse_Entry.delete("0", "end")
#         Patient_Entry.delete("0", "end")
#     elif (surnom == "admin" and mdp == "admin"):
#         messagebox.showinfo("", "Bienvenue")
#         Patient_Entry.delete("0", "end")
#         ModeDePasse_Entry.delete("0", "end")
#         root.destroy()
#         call(["python", "./Registre.py"])
#     else:
#         messagebox.showwarning("", "Erreur de Connexion")
#         ModeDePasse_Entry.delete("0", "end")
#         Patient_Entry.delete("0", "end")


# #Ma fenetre
# root = Tk()

# root.title("FENÊTRE DE CONNECTION")
# root.geometry("400x300+450+200")
# root.resizable(False, False)
# root.configure(background="#091821")

# #Ajouter le titre
# Titre_Label = Label(root, borderwidth=3, relief=SUNKEN, text="Formulaire de connexion", font=(
#     "Sans Serif", 25), background="#091821", foreground="white")
# Titre_Label.place(x=0, y=0, width=400)

# Patient_Label = Label(root, text="Nom Utilisateur :", font=("Arial", 14), bg="#091821", fg="white")
# Patient_Label.place(x=10, y=100, width=150)
# Patient_Entry = Entry(root, bd=4, font=("Arial", 13))
# Patient_Entry.place(x=150, y=100, width=200, height=30)

# lblmdp = Label(root, text="Mot de Passe :", font=("Arial", 14), bg="#091821", fg="white")
# lblmdp.place(x=10, y=150, width=150)
# ModeDePasse_Entry = Entry(root, show="*", bd=4, font=("Arial", 13))
# ModeDePasse_Entry.place(x=150, y=150, width=200, height=30)

# #Bouton Connecter
# btnenregistrer = Button(root, text="Connexion", font=(
#     "Arial", 16), bg="white", fg="#FF4500", command=Seconnecter)
# btnenregistrer.place(x=150, y=200, width=200)


# #Execution
# root.mainloop()
