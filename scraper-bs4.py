import requests
from bs4 import BeautifulSoup

URL = "https://www.mediamarkt.nl/nl/product/_legend-of-zelda-link-s-awakening-nintendo-switch-1623975.html"
page = requests.get(URL)
html = BeautifulSoup(page.content, "html.parser")
productData = html.find(id = "product-details")
price = productData.find(itemprop = "price")["content"]

if (price < 40) {
    print("Aanbieding!")
}
