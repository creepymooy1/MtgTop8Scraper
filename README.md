# MtgTop8Scraper
Python script to scrape EDH decklists from MTGTop8

Purpose:
This code is used for scraping decklists from the mtgtop8 website for the competitive Commander format (cEDH). It uses the BeautifulSoup and requests libraries to parse the HTML and download the decklist files.

Dependencies:

requests library - to make HTTP requests and download the decklist files.
BeautifulSoup library - to parse the HTML content and extract the relevant information.
Instructions:

Install the dependencies using pip or any other package manager.
Example: pip install requests, pip install beautifulsoup4

Run the script "scrape_decklists.py" in a Python environment.

The script will generate decklist files with the name "decklist_x.txt" where "x" is a number. The files will be saved in the same directory where the script is located.

The number of pages to scrape will automatically change based on available decklists. It does this by checking all pages until the ".Nav_PN_no" element is found, or the next button is blurred out.
