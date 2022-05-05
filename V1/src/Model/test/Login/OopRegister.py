#coding:utf-8
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
from click import password_option
from matplotlib.pyplot import text
#from isort import file #pip install Pillow
import pymysql # pip install pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Bg Image
        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # Left Image
        self.left = ImageTk.PhotoImage(file="images/side.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roamn", 20, "blod"), bg="white", fg="black")

        # Row1
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # Row2
        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # Row3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        self.comb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.comb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Fr")
        self.comb_quest.place(x=50, y=270, width=250)
        self.comb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # Row2
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)

        # Terms #! fin coupé
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue="KakaBoudin")

        self.btn_img = ImageTk.PhotoImage(file="images/register.png")
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data)
        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman", 15), bg=0, cursor="hand2")

    def login_window(self):
        self.root.destroy()
        import OopLoginFormSelf

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)

    def register_data(self): #! fin coupé
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree our terms & condition", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=%s", self.txt_email.get())
                row = cur.fetchone()
                #print(row)
                if row != None:
                    messagebox.showerror("Error", "User Already Exist, Please try with another email", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (f_name, l_name, contact, email, question, answer)",
                                self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(), self.txt_email.get(), self.txt_answer.get())
                    #messagebox.showerror("Success", "Welcome", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due To: {str(es)}", parent=self.root)

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

        btn_reg = Button(login_frame, cursor="hand2", text="Register new Account ?", font=("times new roman", 18, "bold"), bg="white")
        btn_login = Button(login_frame, text="login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="black")

        # Clock
        self.lbl = Label(self.root, text="\nWebCode Clock", font=("Book Antiqua", 25, "bold"), fg="white")
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()

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
                else:
                    messagebox.showerror("Success", "Welcome", parent=self.root)

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

        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data)
        btn_login = Button(self.root, text="Sign In", font=("times new roman", 20), bd=0, cursor="hand2", command=self.register_data)
    

    def register_data(self):
        pass




root = Tk()
app = Register(root)
app.mainloop() #! app => root
