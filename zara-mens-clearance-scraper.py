from bs4 import BeautifulSoup
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright
import pytest
import re
import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Define the URL of the website
url = 'https://www.zara.com/us/en/man-special-prices-l806.html?v1=2203954'

# Define the name of the database and the name of the table
DATABASE_NAME = "clearance_items.db"
TABLE_NAME = "items"

# Define the SQL query to create the table
CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    name TEXT,
    discount TEXT,
    link TEXT,
    curr_price TEXT,
    prev_price TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""

# Method to scrape clearance items from Zara website
def scrape_clearance_items(url):
    # Open a Playwright browser context and create a new page
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        with browser.new_context() as context:
            page = context.new_page()

            # Navigate to the URL
            page.goto(url)

            # Wait for the page to load completely
            page.wait_for_load_state('networkidle')

            # Get the page source
            html = page.content()

            # Close the browser
            browser.close()

    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the product grid divs
    product_grids = soup.find_all('div', class_='product-grid-product-info__product-header')

    # Initialize a list to store the extracted information
    items = []

    # Connect to the database
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute(CREATE_TABLE_QUERY)

    for p in product_grids:
        # Get product name
        name = p.find('h3').text

        # Get discounted amount
        discount = p.find('span', class_='price-current__discount-percentage').text.strip()

        # Get link
        link = p.find('a', class_='product-link _item product-grid-product-info__name link')
        link = link.get('href')

        # Get current price
        curr_price = p.find('span', class_='price-current__amount').text.strip()

         # Get previous price
        prev_price = p.find('span', class_='price-old__amount').text.strip()

        # Current time and date
        now = datetime.now()
        # Print the extracted information
        print(f"Name: {name}")
        print(f"Discount: {discount}")
        print(f"Link: {link}")
        print(f"Current Price: {curr_price}")
        print(f"Previous Price: {prev_price}")
        print("----------------------")

        # Create a dictionary for the current item and append it to the list
        item = {
            'name': name,
            'discount': discount,
            'link': link,
            'curr_price': curr_price,
            'prev_price': prev_price
        }
        items.append(item)
        
        # Loop through the items in the database
        for item in items:
            # Check if the item already exists in the database
            c.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = ?", (item['name'],))
            result = c.fetchone()
            if result:
                # If the item exists skip it
                continue
            else:
                # If the item doesn't exist, insert a new record
                c.execute(f"INSERT INTO {TABLE_NAME} (name, discount, link, curr_price, prev_price) VALUES (?, ?, ?, ?, ?)", (item['name'], item['discount'], item['link'], item['curr_price'], item['prev_price']))

        


    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    return items


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title and size.
        self.title("Zara Men's Clearance Scraper")
        self.geometry("350x200")
        
        # Add a label to the window.
        self.label = tk.Label(self, text="Click the button to start scraping Zara.")
        self.label.pack(pady=10)

        # Add a button to the window.
        self.button = tk.Button(self, text="Scrape Marketplace", command=self.scrape)
        self.button.pack(pady=10)
        
        # Add a label to write "Developed by" to the window.
        self.label = tk.Label(self, text="Developed by:")
        self.label.pack(pady=2)
        
        
        # Add Logo to the window.
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo = self.logo.subsample(2, 2)
        self.label = tk.Label(self, image=self.logo)
        self.label.pack(pady=10)
    
    def scrape(self):
        # Call the function and print the results
        items = scrape_clearance_items(url)
        scrape_count = len(items)
        print(f"Scraped {scrape_count} items.")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
    


