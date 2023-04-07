import requests
from bs4 import BeautifulSoup

# Step 1: Get the highest page number
url = input("Enter the URL of the website: ")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
pagination = soup.find('div', {'class': 'pagination'})
page_links = pagination.find_all('a')
max_page_num = int(page_links[-2]['data-page'])

# Step 2: Create a list of links
base_url = url.split('?')[0]
page_links = [f"{base_url}?page={i}" for i in range(1, max_page_num+1)]

# Step 3: Get the list of watch codes from the user
watch_codes = input("Enter the watch codes separated by commas: ").split(',')

# Step 4: Scrape the data for each watch code
for page_link in page_links:
    r = requests.get(page_link)
    soup = BeautifulSoup(r.content, 'html.parser')
    for watch_code in watch_codes:
        watch_div = soup.find('a', {'href': f"/zegarki-tommy-hilfiger/zegarek-{watch_code.strip()}"})
        if watch_div:
            model = watch_div['title'].split(' - ')[1]
            price = watch_div.find('span', {'class': 'new-price-black'}).text
            img_url = watch_div.find('img')['src']
            product_url = 'https://www.zegarek.net/' + watch_div['href']
            print(f"Watch code: {watch_code.strip()}\nModel: {model}\nPrice: {price}\nImage URL: {img_url}\nProduct URL: {product_url}\n")
