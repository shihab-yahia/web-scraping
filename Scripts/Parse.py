from bs4 import BeautifulSoup
import os
import pandas as pd

d = {"Title": [], "Price": [], "Link": []}

for file in os.listdir("Data"):
    try:
        with open(f"Data/{file}", "r", encoding="utf-8") as f:
            doc = f.read()
        soup = BeautifulSoup(doc, "html.parser")
        product_blocks = soup.find_all('div', attrs={'class': '....'}) # Replace with the actual class name
        for block in product_blocks:
            title = block.get_text(strip=True)


            link_tag = block.find('a')
            link = "https://www.daraz.pk/" + link_tag['href']


            price_tag = block.find_next('div', attrs={'class': '....'}) # Replace with the actual class name
            price = price_tag.get_text(strip=True)


            d["Title"].append(title)
            d["Price"].append(price)
            d["Link"].append(link)

    except Exception as e:
        print(f"Error in {file}: {e}")

df = pd.DataFrame(d)
df.to_csv('result2.csv', index=False)
