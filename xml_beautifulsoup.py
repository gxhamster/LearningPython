from bs4 import BeautifulSoup

FILE_DIR = 'adwaita-timed.xml'

file = open(FILE_DIR, 'rb')

soup = BeautifulSoup(file, 'lxml-xml')
string = soup.decode(pretty_print=True)

print(soup.year  )

