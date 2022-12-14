from bs4 import BeautifulSoup
import requests

url = ''

page = requests.get(url)

#soup = BeautifulSoup(page.content, 'html.parser')

# Soup is another name for the data being scraped in this context
soup = BeautifulSoup(url.text, 'html.parser')