from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = 'https://bracketteam.com/events'
driver.get(url)

input("Manual Intervention")


# //div[contains(@class, "page-selection")]/button[@mat-icon-button]

nav_btn = driver.find_elements(By.XPATH, '//div[contains(@class, "page-selection")]/button[@mat-icon-button]')
nav_btn[1].click() # next btn 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


xnp = '//div[contains(@class, "page-selection")]/button[@mat-icon-button]'
count = 0
nextbtn = ''
while True:
     count += 1
     print(count)
     ## Get Data you want
     xp =  '//div[contains(@class,"tournament-container")]'
     try:
          elements = driver.find_elements(By.XPATH, xp) # if you cannot fetch elements then code under it will be discarded

          for i, el in enumerate(elements):
               item = el.get_attribute('outerHTML')
               item = str(item)
               with open(f'data/elem_{count}_{i}.html', 'w', encoding='utf-8') as f:
                    f.write(item)
     except:
          print("error in fetching elements")
     
     ## Get Button to Next Page
     try:
          nextbtn = WebDriverWait(driver, 10).until(
               EC.visibility_of_all_elements_located((By.XPATH, xnp))
          )
          nextbtn = nextbtn[1]
     except:
          print("next button not found!")
          break

     ## if next button is Hidden (last page)
     if nextbtn.get_attribute("diabled") is not None:
          print("No more pages")
          break
     else:
          nextbtn.click()
          WebDriverWait(driver, 10).until(
                EC.invisibility_of_element((By.XPATH, '//div[@class="loading-spinner"]'))
            )
          time.sleep(1)

driver.quit()


