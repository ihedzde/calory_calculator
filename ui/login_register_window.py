from tkinter import *

from di_containers.di_containers import Services, Configs
from models.user_model import User
from tkinter import messagebox

from ui.main_window import MainWindow


class LoginSignUpWindow:
    def __init__(self, window, auth_service):
        self.window = window
        self.auth_service = auth_service
        self.set_up(window)
    def set_up(self, window):
        window.geometry("400x300")
        label = Label(text="Login")
        label.pack()
        self.login = Entry()
        self.login.pack()
        label2 = Label(text="Password")
        label2.pack()
        self.password = Entry()
        self.password['show'] = '*'
        self.password.pack()

        self.log_btn = Button(text="Sign_in", command=lambda: self.sign_in(self.login.get(), self.password.get()))
        self.log_btn.pack()
        self.reg_btn = Button(text="Sign_up", command=self.sign_up_input)
        self.reg_btn.pack()

    def sign_up_input(self):
        self.reg_btn.destroy()
        self.log_btn.destroy()
        self.name_label = Label(text="Fullname")
        self.name_label.pack()
        self.name = Entry()
        self.name.pack()
        self.reg_btn = Button(text = "Sign_up", command=lambda:self.sign_up(self.login.get(), self.password.get(),
                                                                            self.name.get()))
        self.reg_btn.pack()

        self.back_btn = Button(text="Back to login.", command=self.back_to_login)
        self.back_btn.pack()

    def back_to_login(self):
        self.log_btn = Button(text="Sign_in", command=lambda: self.sign_in(self.login.get(), self.password.get()))
        self.log_btn.pack()
        self.name.destroy()
        self.name_label.destroy()
        self.back_btn.destroy()
        self.reg_btn.destroy()
        self.reg_btn = Button(text="Sign_up", command=self.sign_up_input)
        self.reg_btn.pack()
    def sign_up(self, login, password, name):
        user = User(login = login, password=password, fullname = str(name))
        try:
            self.auth_service.create_new_user(user)
            messagebox.showinfo(message="User created.")
            self.window.destroy()
            self.window = Tk()
            MainWindow(self.window, user.id, Services.product_service(), Services.user_service(),
                       Services.physical_stats_service())
        except:
            messagebox.showinfo(message="User with that login already exists.")

    def sign_in(self, login, password):
        user = User(login = login, password = password)
        try:
            user_from_db = self.auth_service.verify_user(user)

            self.window.destroy()
            self.window = Tk()
            MainWindow(self.window, user_from_db.id, Services.product_service(), Services.user_service(),
                       Services.physical_stats_service())

        except Exception as e:
            messagebox.showinfo(message="Wrong login or password.")

