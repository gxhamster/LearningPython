import requests
from bs4 import BeautifulSoup

URL = 'https://edition.mv/r_meedhoo'

headers = 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'


# Basic code to collect the page markup
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('title').get_text()


print(title)


