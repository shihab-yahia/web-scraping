from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

if not os.path.exists("Data"):
    os.makedirs("Data")

driver = webdriver.Chrome()
query = "Condom"

for i in range(1, 11):
    driver.get(
        f"https://www........{i}{query}") # Replace with the actual URL pattern

    time.sleep(3)

    elems = driver.find_elements(By.CLASS_NAME, "Bm3ON")

    all_html = ""
    for elem in elems:
        all_html += elem.get_attribute("outerHTML") + "\n"

    with open(f"Data/{query}_page_{i}.html", "w", encoding="utf-8") as f:
        f.write(all_html)

    print(f"Saved {len(elems)} 'Bm3ON' elements from page {i}")
    time.sleep(2)

driver.quit()
