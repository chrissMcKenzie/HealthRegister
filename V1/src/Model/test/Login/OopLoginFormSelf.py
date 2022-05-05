#coding:utf-8
from email import message
from tkinter import *
from PIL import Image, ImageTk, ImageDraw #pip install Pillow
from datetime import *
import time
from math import *
from aem import con
#from matplotlib.pyplot import draw, text
import pymysql # pip install pymysql
from tkinter import messagebox

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        # Background Colors
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

#! fin coupé
        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="black")
        
        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white")
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white")
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=self.register_window, text="Register new Account ?", font=("times new roman", 18, "bold"), bg="white")
        btn_login = Button(login_frame, text="login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="black")

        # Clock
        self.lbl = Label(self.root, text="\nWebCode Clock", font=("Book Antiqua", 25, "bold"), fg="white")
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()

    def register_window(self):
        self.root.destroy()
        import OopRegister

    def login(self):
        # print(self.txt_email.get(), self.txt_pass_.get())
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=%s AND password=%s", (self.txt_email.get(), self.txt_pass.get()))
                row = cur.fetchone()
                print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
                    # self.root.destroy()
                    # import OopRegister
                else:
                    messagebox.showerror("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    import OopStudent_Management
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.root)


    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400,400), (8,25,35))
        draw = ImageDraw.Draw(clock)
        # For Clock Image
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        # Formula To Rotate the AntiClock
        # angle_in_radians = angle_in_degress * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)

        # Hour Line Image
        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="#DF0005E", width=4)
        # Min Line Image
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="white", width=4)
        # Sec Line Image
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="yellow", width=4)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")
    
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)




root = Tk()
app = Login_window(root)
root.mainloop() #! app => root
