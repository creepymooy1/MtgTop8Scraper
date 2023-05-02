import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://www.mtgtop8.com'

formatted_url_main = "https://www.mtgtop8.com/search?current_page="
formatted_url_params = "&event_titre=&deck_titre=&player=&format=cEDH&archetype_sel%5BVI%5D=&archetype_sel%5BLE%5D=&archetype_sel%5BMO%5D=&archetype_sel%5BPI%5D=&archetype_sel%5BEX%5D=&archetype_sel%5BHI%5D=&archetype_sel%5BST%5D=&archetype_sel%5BBL%5D=&archetype_sel%5BPAU%5D=&archetype_sel%5BEDH%5D=&archetype_sel%5BHIGH%5D=&archetype_sel%5BEDHP%5D=&archetype_sel%5BCHL%5D=&archetype_sel%5BPEA%5D=&archetype_sel%5BEDHM%5D=&archetype_sel%5BALCH%5D=&archetype_sel%5BcEDH%5D=&archetype_sel%5BEXP%5D=&archetype_sel%5BPREM%5D=&compet_check%5BP%5D=1&compet_check%5BM%5D=1&compet_check%5BC%5D=1&compet_check%5BR%5D=1&MD_check=1&cards=&date_start=&date_end="

current_page = 1

page_url = formatted_url_main + str(current_page) + formatted_url_params


def get_links(soup):
	links = []

	table_rows = soup.select(".hover_tr")

	for row in table_rows:
		link_tag = row.find_all("td")[1].find("a")
		card_name = link_tag.contents[0]
		links.append(link_tag.get("href"))

	return links


def download_decklist(url, counter):
	response = requests.get(url)
	with open(f'decklist_{counter}.txt', 'wb') as f:
		f.write(response.content)


def scrape_decklists(url, num_pages=5):
	decks = []

	current_page = 1

	item_page_links = []

	counter = 1

	while (True):
		# Fetch the web page content
		response = requests.get(formatted_url_main + str(current_page) +
		                        formatted_url_params)
		content = response.content

		# Parse the content using BeautifulSoup
		soup = BeautifulSoup(content, 'html.parser')

		# Extract deck data
		item_page_links += get_links(soup)

		for link in item_page_links:
			full_url = base_url + "/mtgo" + link[5:]
			download_decklist(full_url, counter)
			counter += 1

		next_button = soup.select(".Nav_PN_no")
		if (next_button and next_button[0].contents[0] == "Next"):
			break

		current_page += 1

	print("we done")

	return decks


# Scrape decklists from the first few pages
url = 'https://www.mtgtop8.com/search?format=cedh'
decks = scrape_decklists(page_url)
