#coding:utf-8
import tkinter as tk

"""ERREUR"""
# class App(tk.Tk):
#      def __init__(this):
#         super().__init__()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


class App:
    def __init__(self):
        window = tk.Tk()  # !window = tk()

        # configure the window window
        window.title("Python DeskApp Poo")
        window.geometry("500x100")

        window.mainloop()


app = App()
#! app.mainloop()
