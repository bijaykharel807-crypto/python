import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime


FILE_NAME = "sales_data.csv"
COLUMNS = ("Date", "Product", "Quantity", "Price", "Total")

class DataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Descriptive Analysis Data Entry")
        self.root.geometry("600x450")

        
        self.check_file_exists()

        
        input_frame = ttk.LabelFrame(root, text="New Entry", padding=(10, 10))
        input_frame.pack(fill="x", padx=10, pady=5)

       
        ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(input_frame)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

       
        ttk.Label(input_frame, text="Product Name:").grid(row=0, column=2, padx=5, pady=5)
        self.product_entry = ttk.Entry(input_frame)
        self.product_entry.grid(row=0, column=3, padx=5, pady=5)

       
        ttk.Label(input_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.qty_entry = ttk.Entry(input_frame)
        self.qty_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Unit Price ($):").grid(row=1, column=2, padx=5, pady=5)
        self.price_entry = ttk.Entry(input_frame)
        self.price_entry.grid(row=1, column=3, padx=5, pady=5)

        
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        ttk.Button(btn_frame, text="Add Record", command=self.add_record).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=5)

        
        self.tree_frame = ttk.LabelFrame(root, text="Stored Data (CSV)", padding=(10, 10))
        self.tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(self.tree_frame, columns=COLUMNS, show="headings")
        
        # Define Headings
        for col in COLUMNS:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Load existing data on startup
        self.load_data()

    def check_file_exists(self):
        """Creates the CSV file with headers if it doesn't exist."""
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(COLUMNS)

    def add_record(self):
        """Gets data from inputs, calculates total, saves to CSV, and updates table."""
        date = self.date_entry.get()
        product = self.product_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()

        # Validation
        if not product or not qty or not price:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            total = float(qty) * float(price)
        except ValueError:
            messagebox.showerror("Error", "Quantity and Price must be numbers")
            return

        row_data = [date, product, qty, price, f"{total:.2f}"]

    
        with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row_data)

        
        self.tree.insert("", "end", values=row_data)
        self.clear_fields()
        messagebox.showinfo("Success", "Data Saved Successfully!")

    def load_data(self):
        """Reads CSV and populates the treeview."""
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    self.tree.insert("", "end", values=row)

    def clear_fields(self):
        self.product_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()