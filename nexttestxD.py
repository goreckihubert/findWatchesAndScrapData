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
    nazwy = el.find_all('span', {'class': 'nazwa'})
    for nazwa_gr, nazwa in zip(nazwy_gr, nazwy):
        data[nazwa_gr.text.strip()] = nazwa.text.strip()
code = soup.find('span', {'class': 'model'}).text.strip()
gender = soup.find('span', {'class': 'main'}).text.strip()
if gender.__contains__("męski"):
    gender = "męski"
elif gender.__contains__("damski"):
    gender = "damski"
else:
    gender = None

filename = 'watch_info.csv'

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Kod", code])
    writer.writerow(["Dla kogo", gender])
    writer.writerows(data.items())

print('Data saved to', filename)
