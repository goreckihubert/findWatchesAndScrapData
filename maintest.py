import requests
import csv
from bs4 import BeautifulSoup

url = input("Enter the URL of the watch: ")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Get the brand
brand = soup.find('span', {'class': 'nazwa_grupy'}).text.strip()
print(brand)

# Get the model
model = soup.find('span', {'class': 'model'}).text.strip()
print(model)

# Get the price
price = soup.find('span', {'class': 'productspecialprice'}).find('span', {'data-product_cart_info_controller-target': 'detail_price'})
price(price)

# Get the case diameter
tag = soup.find('div', {'class': 'sing-1'}, string='Szerokość koperty')
case_diameter = tag.find('span', {'class': 'nazwa inline'}).text.strip()
print(case_diameter)

# Get the case thickness
case_thickness = soup.find('div', {'class': 'sing-2'}).find('span', {'class': 'nazwa inline'})

# Get the case material
case_material = soup.find('th', text='Materiał koperty').find_next_sibling('td').text.strip()

# Get the strap material
strap_material = soup.find('th', text='Materiał paska / bransolety').find_next_sibling('td').text.strip()

# Get the movement
movement = soup.find('th', text='Mechanizm').find_next_sibling('td').text.strip()

# Get the water resistance
water_resistance = soup.find('th', text='Wodoodporność').find_next_sibling('td').text.strip()

# Get the glass
glass = soup.find('th', text='Szkło').find_next_sibling('td').text.strip()

# Get the functions
functions = [tag.text.strip() for tag in soup.find_all('div', {'class': 'feature_line'})]

# Write the data to a CSV file
# with open('watch_attributes.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Brand', 'Model', 'Price', 'Case Diameter', 'Case Thickness', 'Case Material', 'Strap Material',
#                      'Movement', 'Water Resistance', 'Glass', 'Functions'])
#     writer.writerow([brand, model, price, case_diameter, case_thickness, case_material, strap_material,
#                      movement, water_resistance, glass, ', '.join(functions)])
