from bs4 import BeautifulSoup
import requests
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.04951.54 Safari/537.36'}
#url = "https://www2.hm.com/en_gb/ladies/shop-by-product/dresses.html"
url = "https://m.shein.co.uk/Women-Dresses-c-1727.html?adp=10303912&src_module=women&src_identifier=on%3DIMAGE_CAROUSEL_COMPONENT%60cn%3Dshopbycate%60hz%3D0%60ps%3D3_1_1%60jc%3Dreal_1727&src_tab_page_id=page_home1689062287308&ici=CCCSN%3Dwomen_ON%3DIMAGE_CAROUSEL_COMPONENT_OI%3D5930847_CN%3DITEM_IMAGE_FOUR_COLS_CAROUSEL_TI%3D50001_aod%3D0_PS%3D3-1_1_ABT%3D0"

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, "lxml")

name = soup.find_all("h3", class_="item-heading")
price = soup.find_all("strong", class_="item-price")
images = soup.find_all("img")

list_of_prices = [(x.text)[1:-1] for x in price]
list_of_names = [(x.text)[1:-1] for x in name]
for x in list_of_prices:
    print(x)

for x in list_of_names:
    print(x)

imageSources = []

for image in images:
    imageSources.append(image.get('src'))
    print(image.get('src'))