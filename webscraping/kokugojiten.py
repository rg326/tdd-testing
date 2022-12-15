# Imports
from bs4 import BeautifulSoup
import requests

#Initialize URL (and type)
url = ''

page = requests.url('')

soup = BeautifulSoup(url.text, 'html.parser')
