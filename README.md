# zara-mens-clearance-scraper

<p align="center">
<img src="https://i.imgur.com/GbFqZYa.png">
</p>
<h3 align="center">A Python program to scrape Facebook Marketplace using Playwright, BeautifulSoup, and SQLite.
</h3>
<h3 align="center">

### Overview
This open-source program uses a combination of Python and SQLite to scrape data from the Zara website and store it in a database. It scrapes information about clearance items, such as the product name, discount amount, link, and current and previous prices. It also has a GUI built with tkinter for the user to launch the program.

### Customization
This program can be customized to your personal/organizational needs. For more information please contact me via [LinkedIn](https://www.linkedin.com/in/harmindersinghnijjar/) or email at Harmindernijjar1996@gmail.com
  
### Frameworks:
- Tkinter
- Playwright
- BeautifulSoup 
- SQLite 
  
### Language: 
- [Python](https://www.python.org/)
  
### Flow diagrams:

### Requirements:
- Python 3.x
- Playwright
- PyQt5 
- BeautifulSoup 
- SQLite

### Modules:
- BeautifulSoup: BeautifulSoup is used to parse the HTML and extract the relevant data.
- SQLite: SQLite is used to store the scraped data in a database.
- Playwright:  Playwright is used to open a browser context and navigate to the URL of the website.
- Pytest: Pytest is used for unit testing.
- Re: Re is used for regex pattern matching.
- Tkinter: Tkinter is used to create a graphical user interface.
- Datetime: Datetime is used to get the current date and time.

 ### API:
  
 ### Classes:
 - MainWindow
 
 ### Functions:
 1. `scrape_clearance_items` - This function scrapes clearance items from the Zara website and stores them in a SQL database. It takes in a URL as the parameter and returns a list of dictionaries containing the product information.
2. `MainWindow` - This class creates a GUI window with a button to start the scraping process. When the button is clicked, it calls the `scrape_clearance_items` function.

### Procedure:
1. The `MainWindow` class is initialized with a label, button and logo.
2. When the button is clicked, it calls the `scrape_clearance_items` function with the URL as the parameter.
3. The function first opens a Playwright browser context and creates a new page. It then navigates to the URL and waits for the page to load completely.
4. Next, it gets the page source and parses it using BeautifulSoup.
5. It then finds all the product grid divs and initializes an empty list to store the extracted information.
6. It then connects to the database and creates the table if it doesn't exist.
7. In a loop, it extracts the product name, discounted amount, link, current price and previous price. It also stores the current date and time.
8. Finally, it creates a dictionary for the current item and appends it to the list. It then checks if the item already exists in the database and if it doesn't, inserts a new record.
9. The function then commits the changes, closes the connection and returns the list of dictionaries containing the product information.

