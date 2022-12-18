from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def get_data(page_url, d_path):
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  driver = webdriver.Chrome(
      service=Service(d_path),
      options=options
    )
  try:
    driver.get(url=page_url)
    sleep(3)

    with open('index.html', 'w', encoding="utf-8") as file:
      file.write(driver.page_source)
    
    return None

  except Exception as ex:
    print(ex)
  finally:
    driver.close()
    driver.quit()