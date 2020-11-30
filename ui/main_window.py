from tkinter import *

from models.user_model import User
from tkinter import messagebox
from tkinter import ttk
class MainWindow:
    def __init__(self, window, user_id, product_service, user_service, physical_stats_service):
        self.product_service = product_service
        self.user_id = user_id
        self.user_service = user_service
        self.physical_stats_service = physical_stats_service
        try:
            self.set_up(window)
        except:
            print("Main window.")
    def set_up(self, window):
        window.geometry("600x450")
        nb = ttk.Notebook(window)
        self.page1 = ttk.Frame(nb)
        self.page2 = ttk.Frame(nb)
        self.page3 = ttk.Frame(nb)
        nb.add(self.page1, text="Physical stats.")
        nb.add(self.page2, text="Food catalog.")
        nb.add(self.page3, text="Profile settings.")
        nb.pack(expand=1, fill="both")