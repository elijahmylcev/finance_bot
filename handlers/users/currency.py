import requests
from bs4 import BeautifulSoup

# delete
# from selenium import webdriver  # pip install selenium
# from selenium.webdriver.chrome.service import Service
# import webdriver_manager.chrome as wmc

RUB_TENGE = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&sxsrf=ALiCzsZYROkeMzw-lb7pSCnwUiVASykH7g%3A1666072417657&ei=YT9OY7LdJ4m53AOR046QAQ&ved=0ahUKEwjykf-0i-n6AhWJHHcKHZGpAxIQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzISCAAQgAQQhwIQsQMQFBBGEIICMg0IABCABBCHAhDJAxAUMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6DQgAEEcQ1gQQsAMQyQM6CAgAEJIDELADOhIILhDHARDRAxDIAxCwAxBDGAE6FQguEMcBENEDENQCEMgDELADEEMYAToHCAAQgAQQDToGCAAQBxAeOggIABAIEAcQHjoGCAAQCBAeOg0IABCABBCHAhCxAxAUOggIABCABBDJAzoGCAAQFhAeSgQIQRgASgQIRhgAUN0KWNI9YLBCaANwAXgAgAGeAYgB7w6SAQQwLjEzmAEAoAEByAEMwAEB2gEECAEYCA&sclient=gws-wiz-serp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


full_page = requests.get(RUB_TENGE, headers=headers)

soup = BeautifulSoup(full_page.text, 'lxml')

convert = soup.find('span', {"class": "DFlfde", "data-precision": 2})
print(convert)
# {"class": "DFlfde", "class": "SwHCTb", 'data-precision': 2}
# convert = soup.find_all('span', attrs={"class": "DFlfde SwHCTb"})
