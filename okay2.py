import tkinter as tk
from tkinter import ttk
import sqlite3
import sys

# Try to import the browser engine
try:
    from tkinterweb import HtmlFrame
except ImportError:
    print("CRITICAL ERROR: You must run 'pip install tkinterweb' in your terminal first!")
    sys.exit()

class SimpleBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("My Python Chrome")
        self.root.geometry("1000x800")

        # --- 1. SETUP DATABASE ---
        self.conn = sqlite3.connect("my_history.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS history (url TEXT)")
        self.conn.commit()

        # --- 2. TOP BAR ---
        bar = tk.Frame(root, bg="#ddd", height=50)
        bar.pack(side=tk.TOP, fill=tk.X)

        # Address Input
        self.url_input = tk.Entry(bar)
        self.url_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        self.url_input.bind('<Return>', self.load_site) # Press Enter to go

        # Go Button
        btn = tk.Button(bar, text="Go", command=self.load_site)
        btn.pack(side=tk.LEFT, padx=10)

        # History Button
        h_btn = tk.Button(bar, text="Show History", command=self.show_history)
        h_btn.pack(side=tk.LEFT, padx=10)

        # --- 3. BROWSER FRAME ---
        # This is the part that needs 'tkinterweb'
        self.browser = HtmlFrame(root) 
        self.browser.pack(fill=tk.BOTH, expand=True)

    def load_site(self, event=None):
        url = self.url_input.get()
        if not url.startswith("http"):
            url = "https://" + url
            
        print(f"Loading: {url}") # Debugging: Print to terminal
        self.browser.load_website(url)
        
        # Save to DB
        self.cursor.execute("INSERT INTO history (url) VALUES (?)", (url,))
        self.conn.commit()

    def show_history(self):
        # Print history to the black terminal window instead of a popup (easier to debug)
        print("\n--- BROWSING HISTORY ---")
        self.cursor.execute("SELECT * FROM history")
        for row in self.cursor.fetchall():
            print(row[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBrowser(root)
    root.mainloop()