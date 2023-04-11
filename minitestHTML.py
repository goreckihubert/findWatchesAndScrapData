import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.zegarek.net/zegarki-tommy-hilfiger/zegarek-1792024"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

panel_attr = soup.find_all('div', {'class': 'atr'})
# print(panel_attr)

data = {}
for el in panel_attr:
    nazwy_gr = el.find_all('span', {'class': 'nazwa_grupy'})
    nazwa = el.find_all('span', {'class': 'nazwa'})
    for nazwa_gr, nazwa_el in zip(nazwy_gr, nazwa):
        data[nazwa_gr.text.strip()] = nazwa_el.text.strip()

print(data)