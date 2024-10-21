import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://www.divan.ru/category/divany-i-kresla"

driver.get(url)

time.sleep(15)

products = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

print(f"Найдено товаров: {len(products)}")

parsed_data = []

for product in products:
    try:
        # Получаем название товара
        title = product.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        # Получаем цену товара
        price = product.find_element(By.CSS_SELECTOR, 'div.pY3d2').text
        # Получаем ссылку на товар
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("products.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)

print("Данные успешно записаны в products.csv")
