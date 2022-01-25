import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.unilorin.edu.ng/')
bSoup = BeautifulSoup(page.content, 'html.parser')

links_list = bSoup.find_all('a')

for link in links_list:
    if 'href' in link.attrs:
        print(str(link.attrs['href'])+ "\n")