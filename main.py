from database.database import *
from sqlalchemy import select

from di_containers.di_containers import Repositories, Configs, Services
from ui.login_register_window import LoginSignUpWindow
from tkinter import *
if __name__ == '__main__':

    # test_db = Database(SQLITE, dbname='fitness_db.sqlite')
    Configs.dbname.override('fitness_db.sqlite')
    Configs.dbtype.override(SQLITE)

    window = Tk()
    window.geometry("400x300")
    LoginSignUpWindow(window, Services.user_service())
    window.mainloop()