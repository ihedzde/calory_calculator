from tkinter import *

from models.physical_stats import PhysicalStats
from models.product import Product
from models.user_model import User
from tkinter import messagebox
from tkinter import ttk
class MainWindow:
    def __init__(self, window, user_id, product_service, user_service, physical_stats_service):
        self.window = window
        self.product_service = product_service
        self.user_id = user_id
        self.user_service = user_service
        self.physical_stats_service = physical_stats_service
        try:
            self.set_up(window)
        except Exception as e:
            print(e,"Main window.")
    def set_up(self, window):
        window.geometry("600x450")
        nb = ttk.Notebook(window)
        self.page1 = ttk.Frame(nb)
        self.page2 = ttk.Frame(nb)
        nb.add(self.page1, text="Physical stats.")
        nb.add(self.page2, text="Food catalog.")
        nb.pack(expand=1, fill="both")
        self.physical_stats_page()
        self.product_page()
    def product_page(self):
        self.print_products()
        self.input_product()
    def print_products(self):
        self.catalog = Canvas(self.page2)
        Label(self.page2, text="Name").grid(row=0, column = 0)
        Label(self.page2, text="Carbs").grid(row=0, column = 1)
        Label(self.page2, text="Protein").grid(row=0, column = 2)
        Label(self.page2, text="Fats").grid(row=0, column = 3)
        Label(self.page2, text="Delete").grid(row=0, column = 4)
        products = self.product_service.get_all_product()
        for i, product in enumerate(products):
                Label(self.page2, text= product.name).grid(row=i+1, column = 0)
                Label(self.page2, text= round(product.carb,2)).grid(row=i+1, column = 1)
                Label(self.page2, text= round(product.protein)).grid(row=i+1, column = 2)
                Label(self.page2, text= round(product.fat)).grid(row=i+1, column = 3)
                Button(self.page2, text= "❌").grid(row=i+1, column = 4)
        last_row = len(products)+1
        product_name = Entry(self.page2)
        product_name.grid(row=last_row, column=0)
        carbs = Entry(self.page2)
        carbs.grid(row=last_row, column=1)
        proteins = Entry(self.page2)
        proteins.grid(row=last_row, column=2)
        fats = Entry(self.page2)
        fats.grid(row=last_row, column=3)
        Button(self.page2, text="+", command=lambda: self.create_product(product_name.get(),
                                                                         carbs.get(),
                                                                         proteins.get(),
                                                                         fats.get())).grid(row=last_row, column=4)

    def input_product(self):
        page = self.page2
        # Button(page, text="Create Product.", command=self.create_product()).pack()
        # if True:
        #     self.product_name = Label(page, "Name").pack()
        #     self.product_name = Entry(page)
        #     self.product_name.pack()
        #     Label(page, "Carbs").pack()
        #     self.carbs = Entry(page)
        #     self.carbs.pack()
        #     Label(page, "Proteins").pack()
        #     self.proteins = Entry(page)
        #     self.proteins.pack()
        #     Label(page, "Fats").pack()
        #     self.fats = Entry(page)
        #     self.fats.pack()
    def create_product(self, product_name, carbs, proteins, fats):
        product = Product(
            name = product_name,
            carb = carbs,
            protein = proteins,
            fat = fats
            )
        self.product_service.create_new_product(product)
        self.clear_page(self.page2)
        self.print_products()

    def update_product(self, product_id):
        product = self.product_service.get_product_by_id(product_id)
        # product.name = self.product_name.get()
        # product.carb = self.carbs.get()
        # product.fat = self.fats.get()
        # product.protein = self.proteins.get()
        self.product_service.update_products()


    def physical_stats_page(self):

        self.stats = self.physical_stats_service.get_physical_stats_by_user_id(self.user_id)
        if self.stats is None:
            self.stats_input(self.page1)
        else:
            self.print_stats(self.stats)
    def print_stats(self, stats):
        self.clear_page(self.page1)
        page = self.page1
        Label(page, text="Height: " + str(stats.height)).pack()
        Label(page, text="Weight: " + str(stats.weight)).pack()
        Label(page, text="Age: " + str(stats.age)).pack()
        Label(page, text="Level of activity: " + str(stats.level_of_activity)).pack()
        Label(page, text="Gender: " + str(stats.gender)).pack()
        Label(page, text=str("BMI: " + str(round(stats.bmi(),2)))).pack()
        Label(page, text=str("BMR: " + str(round(stats.bmr(),2)))).pack()
        Button(page, text="Update.", command=lambda :self.stats_input(page, stats)).pack()
    def stats_input(self, page, prev_stats=None):
        self.clear_page(self.page1)
        Label(page,text="Please fill out stats").pack()
        levels=['Average','Low','High']
        genders = ['male', 'female']
        Label(page, text="Weight:").pack()
        if prev_stats is not None:
            self.weight = Entry(page)
            self.weight.insert(END, prev_stats.weight)
            self.weight.pack()
            Label(page,text="Height").pack()
            self.height = Entry(page)
            self.height.insert(END, prev_stats.height)
            self.height.pack()
            Label(page,text="Age").pack()
            self.age = Entry(page)
            self.age.insert(END, prev_stats.age)
            self.age.pack()
            Label(page, text="Level of activity").pack()
            var = StringVar(self.window)
            var.set(prev_stats.level_of_activity)
            w = OptionMenu(page, var, *levels)
            w.pack()
            self.level = var
            Label(page, text="Gender").pack()
            var2 = StringVar(self.window)
            var2.set(prev_stats.gender)
            w2 = OptionMenu(page, var2, *genders)
            w2.pack()
            self.gender = var2
            Button(page, text="Update", command=self.update_stats).pack()
        else:
            self.weight = Entry(page)
            self.weight.pack()
            Label(page, text="Height").pack()
            self.height = Entry(page)
            self.height.pack()
            Label(page, text="Age").pack()
            self.age = Entry(page)
            self.age.pack()
            Label(page, text="Level of activity").pack()
            var = StringVar(self.window)
            var.set(levels[0])
            w = OptionMenu(page, var, *levels)
            w.pack()
            self.level = var
            Label(page, text="Gender").pack()
            var2 = StringVar(self.window)
            var2.set(genders[0])
            w2 = OptionMenu(page, var2, *genders)
            w2.pack()
            self.gender = var2
            Button(page, text="Create.", command = self.create_stats).pack()
    def create_stats(self):
        physical_stats = PhysicalStats(
            user_id=self.user_id, weight = self.weight.get(),
            height = self.height.get(), age = self.age.get(),
            level_of_activity=str(self.level.get()),
            gender = str(self.gender.get())
        )
        self.physical_stats_service.create_new_physical_stats(physical_stats)
        self.print_stats(physical_stats)
    def update_stats(self):
        physical_stats = self.physical_stats_service.get_physical_stats_by_user_id(self.user_id)
        physical_stats.weight=self.weight.get()
        physical_stats.height=self.height.get()
        physical_stats.age=self.age.get()
        physical_stats.level_of_activity = str(self.level.get())
        physical_stats.gender = str(self.gender.get())
        self.physical_stats_service.update_physical_stats()
        self.print_stats(physical_stats)
    def clear_page(self, page):
        for w in page.winfo_children():
            w.destroy()