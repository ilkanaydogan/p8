#PROJECT - 8
import customtkinter
import tkinter as tk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

#////////////////////////////////////////////////////////////////////////////////////////////#

r3 = customtkinter.CTk()
r3.title("RECIPE APP")

r2 = customtkinter.CTk()
r2.title("LOGIN")

r1 = customtkinter.CTk()
r1.title("REGISTER")

#////////////////////////////////////////////////////////////////////////////////////////////#

conn = sqlite3.connect("data8.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

#////////////////////////////////////////////////////////////////////////////////////////////#

def entry_to_recipe_app():
        
        r2.destroy()
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

        # Create a frame for the recipe app
        recipe_app_frame = customtkinter.CTkFrame(master=r2)
        recipe_app_frame.pack(pady=20, padx=20, fill="both", expand=True, side="left")

        # Create a listbox to display the recipes
        recipe_app_listbox = tk.Listbox(master=recipe_app_frame, height=30, width=100, bg=r3.cget('bg'), fg='white', font="bold")
        recipe_app_listbox.grid(row=1, column=0, rowspan=5, padx=10)

        # Create a label and entry for the recipe name
        recipe_app_name_label = customtkinter.CTkLabel(master=recipe_app_frame, text="Recipe Name:")
        recipe_app_name_label.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        recipe_name_entry = customtkinter.CTkEntry(master=recipe_app_frame, placeholder_text="Enter Recipe Name")
        recipe_name_entry.grid(row=1, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        # Create a label and entry for the ingredient name
        recipe_app_link_label = customtkinter.CTkLabel(master=recipe_app_frame, text="Ingredient Name:")
        recipe_app_link_label.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        ingredient_name_entry = customtkinter.CTkEntry(master=recipe_app_frame, placeholder_text="Enter Ingredient Name")
        ingredient_name_entry.grid(row=2, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        # Create a label and entry for the ingredient piece
        recipe_app_director_label = customtkinter.CTkLabel(master=recipe_app_frame, text="Ingredient Piece:")
        recipe_app_director_label.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        ingredient_piece_entry = customtkinter.CTkEntry(master=recipe_app_frame, placeholder_text="Enter Ingredient Piece")
        ingredient_piece_entry.grid(row=3, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        # Create a function to add the recipe to the listbox
        def add_recipe():
            recipe_name = recipe_name_entry.get()
            ingredient_name = ingredient_name_entry.get()
            ingredient_piece = ingredient_piece_entry.get()

            recipe_list = f"{recipe_name} - {ingredient_name} - {ingredient_piece}"
            recipe_app_listbox.insert("end", recipe_list)

        def delete_item():
            selected_index = recipe_app_listbox.curselection()
            if selected_index:
                recipe_app_listbox.delete(selected_index)


        # Create a button to add the recipe
        add_recipe_button = customtkinter.CTkButton(master=recipe_app_frame, text="Add Recipe", command=add_recipe)
        add_recipe_button.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        delete_recipe_button = customtkinter.CTkButton(master=recipe_app_frame, text="Delete Recipe", command=delete_item)
        delete_recipe_button.grid(row=4, column=2, pady=10, padx=10, sticky="w")

        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

        r3.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#

def login():

    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#
  
def signup():
    username = username_entry_register.get()
    password = password_entry_register.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if(cursor.fetchone() is not None):
            messagebox.showerror("Error","Username already exists!")
        else:
            encodedpassword = password.encode("utf-8")
            hashedpassword = bcrypt.hashpw(encodedpassword, bcrypt.gensalt())
            print(hashedpassword)
            cursor.execute("INSERT into users VALUES(?, ?)", [username, hashedpassword])
            conn.commit()
            messagebox.showinfo("Sucsess!","Account has been created")
            register_to_login_page_button = customtkinter.CTkButton(master=r1,
                                                                    text="Go to Login Page",
                                                                    command=login,)
            register_to_login_page_button.place(relx=0.5, rely=0.6, anchor = tk.CENTER)
    else:
        messagebox.showerror("Error","Enter all data.")

#////////////////////////////////////////////////////////////////////////////////////////////#

def register_to_login_page():
    
    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#

def loginaccount():
    username = username_entry_login.get()
    password = password_entry_login.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                messagebox.showinfo("Success", f"Logged in successfully, Welcome {username}")
                r2.destroy()

#////////////////////////////////////////////////////////////////////////////////////////////#

                # Create a connection to the database
                connn = sqlite3.connect('products.db')
                c = connn.cursor()

                # Create the products table if it doesn't exist
                c.execute('''CREATE TABLE IF NOT EXISTS products
                            (product_id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

                # Create the orders table if it doesn't exist
                c.execute('''CREATE TABLE IF NOT EXISTS orders
                            (order_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER)''')

                c.execute('''CREATE TABLE IF NOT EXISTS stock_changes
                            (id INTEGER PRIMARY KEY, product_name TEXT, quantity INTEGER)''')

                def add_product():
                    name = product_entry.get()
                    if not name:
                        messagebox.showerror("Error", "Product name cannot be empty.")
                        return
                    if get_product_name(name) is not None:
                        messagebox.showerror("Error", "Product already exists.")
                        return
                    c.execute("INSERT INTO products (name, quantity) VALUES (?, 0)", (name,))
                    connn.commit()
                    messagebox.showinfo("Success", "Product added successfully.")

                def get_product_name(product_name):
                    if not product_name:
                        return None
                    c.execute("SELECT name FROM products WHERE name=?", (product_name,))
                    product = c.fetchone()
                    return product[0] if product else None

                def delete_product():
                    name = product_entry.get()
                    if not name:
                        messagebox.showerror("Error", "Product name cannot be empty.")
                        return
                    product_id = get_product_id(name)
                    if product_id is None:
                        messagebox.showerror("Error", "Product not found.")
                        return
                    c.execute("DELETE FROM products WHERE product_id=?", (product_id,))
                    connn.commit()
                    messagebox.showinfo("Success", "Product deleted successfully.")

                def add_order():
                    product_name = product_entry.get()
                    order_quantity = int(order_entry.get())
                    if not product_name or order_quantity <= 0:
                        messagebox.showerror("Error", "Invalid product name or order quantity.")
                        return
                    product_id = get_product_id(product_name)
                    existing_order_quantity = get_order_quantity(product_id)
                    if existing_order_quantity is not None:
                        messagebox.showerror("Error", "Product already ordered.")
                        return
                    c.execute("INSERT INTO orders (product_id, quantity) VALUES (?, ?)", (product_id, order_quantity))
                    connn.commit()
                    messagebox.showinfo("Success", "Order added successfully.")

                def delete_order():
                    product_name = product_entry.get()
                    order_quantity = int(order_entry.get())
                    if not product_name or order_quantity <= 0:
                        messagebox.showerror("Error", "Invalid product name or order quantity.")
                        return
                    product_id = get_product_id(product_name)
                    existing_order_quantity = get_order_quantity_by_product_id(product_id)
                    if existing_order_quantity is None:
                        messagebox.showerror("Error", "Order not found.")
                        return
                    if existing_order_quantity < order_quantity:
                        messagebox.showerror("Error", "Order quantity is greater than the existing order.")
                        return
                    c.execute("DELETE FROM orders WHERE product_id=? AND quantity=?", (product_id, order_quantity))
                    connn.commit()
                    messagebox.showinfo("Success", "Order deleted successfully.")

                def get_order_quantity(product_id):
                    c.execute("SELECT SUM(quantity) FROM orders WHERE product_id=?", (product_id,))
                    order_quantity = c.fetchone()[0]
                    return order_quantity

                def get_order_quantity_by_product_id(product_id):
                    c.execute("SELECT quantity FROM orders WHERE product_id=?", (product_id,))
                    order_quantity = c.fetchone()
                    return order_quantity[0] if order_quantity else None

                def add_stock():
                    product_name = product_entry.get()
                    stock_quantity = stocks_entry.get()

                    if not product_name:
                        messagebox.showerror("Error", "Please enter a product name.")
                        return
                    if not stock_quantity:
                        messagebox.showerror("Error", "Please enter a stock quantity.")
                        return

                    try:
                        stock_quantity = int(stock_quantity)
                        if stock_quantity <= 0:
                            messagebox.showerror("Error", "Stock quantity must be a positive integer.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Stock quantity must be a valid integer.")
                        return

                    current_quantity = get_product_quantity(product_name)
                    if current_quantity is None:
                        messagebox.showerror("Error", "Product not found.")
                        return

                    c.execute("UPDATE products SET quantity=quantity+? WHERE name=?", (stock_quantity, product_name))
                    connn.commit()
                    messagebox.showinfo("Success", "Stock added successfully.")

                def delete_stock():
                    product_name = product_entry.get()
                    if not product_name:
                        messagebox.showerror("Error", "Please enter a product name.")
                        return

                    current_quantity = get_product_quantity(product_name)
                    if current_quantity is None:
                        messagebox.showerror("Error", "Product not found.")
                        return

                    stock_quantity = current_quantity  # Silinecek stok miktarı, mevcut stok miktarı kadar olmalı
                    if stock_quantity <= 0:
                        messagebox.showerror("Error", "Stock is already deleted.")
                        return

                    c.execute("UPDATE products SET quantity=quantity-? WHERE name=?", (stock_quantity, product_name))
                    connn.commit()
                    messagebox.showinfo("Success", "Stock deleted successfully.")

                def get_product_quantity(product_name):
                    c.execute("SELECT quantity FROM products WHERE name=?", (product_name,))
                    product_quantity = c.fetchone()
                    return product_quantity[0] if product_quantity else None

                def get_stock_change_quantity(product_name):
                    c.execute("SELECT COALESCE(SUM(quantity), 0) FROM stock_changes WHERE product_name=?", (product_name,))
                    stock_change_quantity = c.fetchone()[0]
                    return stock_change_quantity

                def view_stock():
                    product_name = product_entry.get()
                    if not product_name:
                        messagebox.showerror("Error", "Product name cannot be empty.")
                        return
                    for row in c.execute('SELECT * FROM products WHERE name=?', (product_name,)):
                        messagebox.showinfo("Stock", f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}")

                def view_orders():
                    product_name = product_entry.get()
                    if not product_name:
                        messagebox.showerror("Error", "Product name cannot be empty.")
                        return

                    c.execute("SELECT * FROM orders WHERE product_id=(SELECT product_id FROM products WHERE name=?)", (product_name,))
                    orders = c.fetchall()
                    if not orders:
                        messagebox.showerror("Error", "There are no orders for this product.")
                        return

                    for row in orders:
                        messagebox.showinfo("Order", f"ID: {row[0]}, Product ID: {row[1]}, Quantity: {row[2]}")

                def get_product_id(product_name):
                    if not product_name:
                        messagebox.showerror("Error", "Product name cannot be empty.")
                        return None
                    c.execute("SELECT product_id FROM products WHERE name=?", (product_name,))
                    product = c.fetchone()
                    return product[0] if product else None


#////////////////////////////////////////////////////////////////////////////////////////////#

                main_frame = customtkinter.CTkFrame(master=r3, height=600, width=800)
                main_frame.pack(padx=20, pady=20)

                left_frame = customtkinter.CTkFrame(master=main_frame, height=550, width=500)
                left_frame.pack(padx=20, pady=20)

                # Product section
                product_label = customtkinter.CTkLabel(master=left_frame, text="Enter Product:")
                product_label.place(relx=0.15, rely=0.05)

                product_entry = customtkinter.CTkEntry(master=left_frame)
                product_entry.place(relx=0.4, rely=0.05)

                product_add_button = customtkinter.CTkButton(master=left_frame, text="Add Product", command=add_product)
                product_add_button.place(relx=0.1, rely=0.15)

                product_delete_button = customtkinter.CTkButton(master=left_frame, text="Delete Product", command=delete_product)
                product_delete_button.place(relx=0.4, rely=0.15)

                # Order section
                order_label = customtkinter.CTkLabel(master=left_frame, text="Enter Your Order:")
                order_label.place(relx=0.15, rely=0.25)

                order_entry = customtkinter.CTkEntry(master=left_frame)
                order_entry.place(relx=0.4, rely=0.25)

                order_add_button = customtkinter.CTkButton(master=left_frame, text="Order", command=add_order)
                order_add_button.place(relx=0.1, rely=0.35)

                order_delete_button = customtkinter.CTkButton(master=left_frame, text="Remove Order", command=delete_order)
                order_delete_button.place(relx=0.4, rely=0.35)

                # Stock section
                stocks_label = customtkinter.CTkLabel(master=left_frame, text="Enter Stock:")
                stocks_label.place(relx=0.15, rely=0.45)

                stocks_entry = customtkinter.CTkEntry(master=left_frame)
                stocks_entry.place(relx=0.4, rely=0.45)

                stocks_add_button = customtkinter.CTkButton(master=left_frame, text="Add Stock", command=add_stock)
                stocks_add_button.place(relx=0.1, rely=0.55)

                stocks_delete_button = customtkinter.CTkButton(master=left_frame, text="Delete Stock", command=delete_stock)
                stocks_delete_button.place(relx=0.4, rely=0.55)

                # Show stock and orders
                show_stock_button = customtkinter.CTkButton(master=left_frame, text="Show Stock", command=view_stock, width=300)
                show_stock_button.place(relx=0.095, rely=0.7)

                show_order_button = customtkinter.CTkButton(master=left_frame, text="Show Order", command=view_orders, width=300)
                show_order_button.place(relx=0.095, rely=0.8)

                r3.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#

frame1 = customtkinter.CTkFrame(master=r1,
                                width=350,
                                height=350)
frame1.pack(padx=20,pady=20)

username_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Username",
                                     width=150,
                                     height=40)
username_entry_register.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

password_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
password_entry_register.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

register_button = customtkinter.CTkButton(master=frame1,
                                          text="Create Your account!",
                                          command=signup)
register_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

register_to_login_label = customtkinter.CTkLabel(master=frame1, 
                                                 text="Already have an account?")
register_to_login_label.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

register_to_login_button = customtkinter.CTkButton(master=frame1,
                                          text="Login!",
                                          command=register_to_login_page)
register_to_login_button.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#////////////////////////////////////////////////////////////////////////////////////////////#

r1.mainloop()    