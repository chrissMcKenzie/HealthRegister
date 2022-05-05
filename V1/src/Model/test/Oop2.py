#coding:utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo


"""tkinter methodes"""
# class App(tk.Tk):
#      def __init__(this):
#         super().__init__()

#         # configure the window window
#         this.title('My Awesome App')
#         this.geometry('300x50')

#         # label
#         this.label = ttk.Label(this, text='Hello, Tkinter!')
#         this.label.pack()

#         # button
#         this.button = ttk.Button(this, text='Click Me')
#         this.button['command'] = this.button_clicked
#         this.button.pack()

#      def button_clicked(this):
#         showinfo(title='Information', message='Hello, Tkinter!')


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

class App:
    window = tk.Tk()
    # title = 
    def __init__(this):
        #window = tk.Tk()  # !window = tk()

        this.Configuration()
        this.Body()
        this.window.mainloop()

    def Configuration(this):
        #this.window
        # configure the window
        this.window.title("Python DeskApp Poo")
        this.window.geometry("1350x500+450+200")
        this.window.configure(background="#091821")


    def Body(this):
        # label
        this.label = ttk.Label(this.window, relief=SUNKEN, text="Formulaire de connexion")
        this.label.place(x=0, y=0, width=400)
        this.label.pack()

        # Patient_Label
        # , font="Arial 14", background="#091821", foreground="white"
        this.Patient_Label = ttk.Label(
            this.window, text="Nom Utilisateur :", font="Arial 14", background="white", foreground="#091821")
        this.Patient_Label.place(x=10, y=100, width=150)

        # button
        this.button = ttk.Button(this.window, text='Connexion', foreground="#00FF00", command=this.button_clicked)
        # this.button['command'] = this.button_clicked()
        this.button.place(x=500, y=350, width=200)
        # this.button.pack()
    
    #! """tkinter methodes"""
    def button_clicked(self):
        showinfo(title='Information', message="Hello, Tkinter!")

app = App()
# app.mainloop()
