import requests
from bs4 import BeautifulSoup

def webscrapping(url):
    url = url
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')

    table = soup.find('title')

    return table.text
    # for row in table:
    #     print(row.text)
