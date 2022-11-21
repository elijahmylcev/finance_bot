from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from config import executable_path, url
from fake_useragent import UserAgent
from create_file_layout import create_html
from out_float import out_float
import random
import time

useragent = UserAgent()
receiving = 10000

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(
    executable_path=executable_path,
    options=options
)

try:
    driver.get(url=url)
    time.sleep(2)

    select_table = driver.find_element(By.CLASS_NAME, 'goog-inline-block grid4-inner-container')
    print(select_table)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
