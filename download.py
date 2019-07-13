import os
import requests
from bs4 import BeautifulSoup

URL1 = 'https://www.physicsandmathstutor.com/maths-revision/solutionbanks/edexcel-pure-maths-year-1/'
URL2 = 'https://www.physicsandmathstutor.com/maths-revision/solutionbanks/edexcel-pure-maths-year-2/'
urls = [URL1, URL2]

# pass a list of URLs

def request(urls):
    pages = []
    for url in urls:
        r = requests.get(url)
        pages.append(r.content)
    
    return pages

def beautifyPage(request_list):
    soups = []
    for request in request_list:
        soup = BeautifulSoup(request, 'html.parser')
        soups.append(soup)
    
    return soups

def find(page):

    print(page.findall('a'))

result = beautifyPage(request(urls))
find(result[0])