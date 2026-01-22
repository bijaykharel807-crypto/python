import sqlite3
import requests
from bs4 import BeautifulSoup

import csv
import json
import os


DB_NAME = "books_data.db"
CSV_FILE = "exported_books.csv"
JSON_FILE = "exported_books.json"
TARGET_URL = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"


def init_db():
    """Creates the database and table if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"[DB] Database '{DB_NAME}' initialized.")

def save_to_db(data_list):
    """Inserts a list of dictionaries into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    
    tuples = [(item['title'], item['price'], item['rating']) for item in data_list]
    
    cursor.executemany('INSERT INTO books (title, price, rating) VALUES (?, ?, ?)', tuples)
    conn.commit()
    conn.close()
    print(f"[DB] Saved {len(data_list)} records to SQL database.")


def scrape_website():
    """Scrapes book data from the target URL."""
    print(f"[Scrape] Fetching data from {TARGET_URL}...")
    response = requests.get(TARGET_URL)
    
    if response.status_code != 200:
        print("[Error] Failed to load page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    books_data = []


    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
      
        title = article.h3.a['title']
        
       
        price = article.find('p', class_='price_color').text.strip()
        
        rating_class = article.find('p', class_='star-rating')['class']
        rating = rating_class[1] if len(rating_class) > 1 else "Unknown"

        books_data.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    print(f"[Scrape] Successfully scraped {len(books_data)} items.")
    return books_data


def export_data():
    """Reads from DB and exports to CSV and JSON."""
    conn = sqlite3.connect(DB_NAME)
   
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    

    data = [dict(row) for row in rows]
    conn.close()

    if not data:
        print("[Export] No data to export.")
        return

    
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"[Export] Data exported to '{CSV_FILE}'")

   
    with open(JSON_FILE, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"[Export] Data exported to '{JSON_FILE}'")


if __name__ == "__main__":
 
    init_db()
    
 
    scraped_data = scrape_website()
    
    
    if scraped_data:
        save_to_db(scraped_data)
    

    export_data()
    
    print("\n--- Process Complete ---")
    print(f"Check your folder for {DB_NAME}, {CSV_FILE}, and {JSON_FILE}")