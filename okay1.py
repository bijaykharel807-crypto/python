import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


def setup_db():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

setup_db()


def add_product():
    name = entry_name.get()
    price = entry_price.get()
    stock = entry_stock.get()

    if name and price and stock:
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", 
                       (name, float(price), int(stock)))
        conn.commit()
        conn.close()
        refresh_list()
        messagebox.showinfo("Success", "Product Added!")
        
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_stock.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please fill all fields")

def sell_product():

    try:
        selected_item = tree.selection()[0]
        product_id = tree.item(selected_item)['values'][0]
        current_stock = tree.item(selected_item)['values'][3]
        
        if current_stock > 0:
            conn = sqlite3.connect("store.db")
            cursor = conn.cursor()
            new_stock = current_stock - 1
            cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
            conn.commit()
            conn.close()
            refresh_list()
            messagebox.showinfo("Sold", "Item Sold! Stock updated.")
        else:
            messagebox.showerror("Error", "Out of Stock!")
    except IndexError:
        messagebox.showwarning("Select", "Please select an item to sell")

def refresh_list():
    
    for row in tree.get_children():
        tree.delete(row)
    
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()


root = tk.Tk()
root.title("Python Store Manager")
root.geometry("600x500")


frame_input = tk.Frame(root, pady=10)
frame_input.pack()

tk.Label(frame_input, text="Product Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=0, column=1)

tk.Label(frame_input, text="Price:").grid(row=1, column=0)
entry_price = tk.Entry(frame_input)
entry_price.grid(row=1, column=1)

tk.Label(frame_input, text="Stock Qty:").grid(row=2, column=0)
entry_stock = tk.Entry(frame_input)
entry_stock.grid(row=2, column=1)

btn_add = tk.Button(frame_input, text="Add Product", command=add_product, bg="#4CAF50", fg="white")
btn_add.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")


tree = ttk.Treeview(root, columns=("ID", "Name", "Price", "Stock"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Price", text="Price")
tree.heading("Stock", text="Stock")
tree.pack(fill=tk.BOTH, expand=True, padx=10)


btn_sell = tk.Button(root, text="SELL SELECTED ITEM (-1 Stock)", command=sell_product, bg="#f44336", fg="white", height=2)
btn_sell.pack(fill=tk.X, padx=10, pady=10)


refresh_list()

root.mainloop()