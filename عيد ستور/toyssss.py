import requests
from bs4 import BeautifulSoup
from itertools import zip_longest

page = 1
Toys = []
price = []
while True:
    result = requests.get(f"https://3eedstore.com/%d8%a7%d9%84%d8%a3%d9%84%d8%b9%d8%a7%d8%a8/?p={page}")
    soup = BeautifulSoup(result.content, "html.parser")
    Toy = soup.find_all("h3", {"class": "woosc-product-title"})
    prices = soup.find_all("span", {"class": "woocommerce-Price-amount amount"})

    for i in range(len(Toy)):
        Toys.append(Toy[i].text.strip().replace("\n", ""))
        price.append(prices[i].text.strip().replace("\xa0", ""))
    if page > 15:
        break
    print(f"page {page} is switched")
    page += 1
print(Toys, price)
filelist = [Toy, price]
exported: zip_longest = zip_longest(*filelist)
