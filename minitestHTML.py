from bs4 import BeautifulSoup
import requests

# parse the HTML
url = "https://www.zegarek.net/zegarki-tommy-hilfiger/zegarek-1792024"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# find the element containing the required information
panel_attr = soup.find_all('div', {'class': 'atr'})
print(len(panel_attr))
for el in panel_attr:
    tag = el.find('strong', {'class': 'nazwa_interfejsu'})
    if tag is not None:
        print(tag.text.strip())
