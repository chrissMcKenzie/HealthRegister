#coding:utf-8
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App:
    window = tk.Tk()
    # configure the window window
    window.title("Python DeskApp Poo")
    window.geometry("500x100")
    
    # title = 
    def __init__(this):
        #window = tk.Tk()  # !window = tk()

        this.Body()
        this.window.mainloop()

    def Body(this):
        # label
        this.label = ttk.Label(this.window, text="Hello, Tkinter!")
        this.label.pack()

    #     # button
    #     this.button = ttk.Button(this, text='Click Me')
    #     this.button['command'] = this.button_clicked
    #     this.button.pack()
    
    # #
    #     """tkinter methodes"""
    # #
    # def button_clicked(self):
    #     showinfo(title='Information', message="Hello, Tkinter!")

app = App()
# app.mainloop()
