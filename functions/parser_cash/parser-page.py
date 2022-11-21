from datetime import datetime
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from config import page, driver_path
from selenium import webdriver


def get_data_with_selenium(page_url, d_path):
    options = webdriver.ChromeOptions()

    try:
        driver = webdriver.Chrome(
            service=Service(d_path),
            # executable_path=driver_path,
            options=options
        )
        driver.get(url=page_url)
        sleep(5)

        with open('index.html', 'w', encoding="utf-8") as file:
            file.write(driver.page_source)

        driver.close()
        driver.quit()

    except Exception as ex:
        print(ex)


get_data_with_selenium(page_url=page, d_path=driver_path)

with open('index.html', 'r', encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

punkt_open_list = soup.find_all('tr', class_='punkt-open')

objects = []
for el in punkt_open_list:
    if el.find('span', class_='kurs-warning') == None:
        name = el.find('a', class_='tab').text
        addres = el.find('address').text
        time_update = el.find('div', class_='relativeTime').text
        rate = float(el.find('span', {'title': 'RUB - покупка'}).text)
        phone = el.find('a', class_='phone').text
        el_object = {
            'name': name,
            'address': addres,
            'time_update': time_update,
            'rate': rate,
            'phone': phone,
        }

        objects.append(el_object)

df = pd.DataFrame(objects)

max_rate = max(df['rate'])

df_max = df[df['rate'] == max_rate]
mean = df['rate'].mean()

print(mean)


with open('max_rate.txt', 'w', encoding='utf-8') as file:
    file.write(
        f'Отчет составлен: {datetime.now()} \nСредний курс: {round(mean, 2)}\n\n{df_max.to_string()}'
    )
