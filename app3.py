import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# --- Configuration ---
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ModernApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Window Setup
        self.title("My Professional Software")
        self.geometry("900x600")

        # 2. Database Setup (Auto-creates file)
        self.init_db()

        # 3. Layout Configuration (Grid)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 4. Create Sidebar (Left Panel)
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="My Software", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Sidebar Buttons
        self.btn_dashboard = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.show_dashboard)
        self.btn_dashboard.grid(row=1, column=0, padx=20, pady=10)
        
        self.btn_entry = ctk.CTkButton(self.sidebar_frame, text="Add Data", command=self.show_entry)
        self.btn_entry.grid(row=2, column=0, padx=20, pady=10)

        self.btn_settings = ctk.CTkButton(self.sidebar_frame, text="Settings", fg_color="transparent", border_width=2, command=self.close_app)
        self.btn_settings.grid(row=3, column=0, padx=20, pady=10)

        # 5. Create Main Area (Right Panel)
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Start at Dashboard
        self.show_dashboard()

    def init_db(self):
        """Creates a hidden database file."""
        self.conn = sqlite3.connect("app_data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT)")
        self.conn.commit()

    # --- Page Functions ---
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main_frame()
        
        # Title
        label = ctk.CTkLabel(self.main_frame, text="Welcome Back!", font=ctk.CTkFont(size=24, weight="bold"))
        label.pack(pady=20)

        # Example Statistic Card
        stat_card = ctk.CTkFrame(self.main_frame, width=200, height=100, fg_color="teal")
        stat_card.pack(pady=10)
        ctk.CTkLabel(stat_card, text="Total Users: 0", text_color="white").place(relx=0.5, rely=0.5, anchor="center")

    def show_entry(self):
        self.clear_main_frame()
        
        label = ctk.CTkLabel(self.main_frame, text="Add New User", font=ctk.CTkFont(size=20))
        label.pack(pady=20)

        # Input Fields
        self.entry_name = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Name")
        self.entry_name.pack(pady=10)
        
        self.entry_email = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Email")
        self.entry_email.pack(pady=10)

        # Save Button
        save_btn = ctk.CTkButton(self.main_frame, text="Save to DB", command=self.save_data)
        save_btn.pack(pady=20)

    def save_data(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        
        if name and email:
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (name, email))
            self.conn.commit()
            messagebox.showinfo("Success", "User Saved!")
            self.show_dashboard() # Go back to home
        else:
            messagebox.showerror("Error", "Fields cannot be empty")

    def close_app(self):
        self.conn.close()
        self.destroy()

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()