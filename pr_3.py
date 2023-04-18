from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


driver = webdriver.Chrome()


driver.get('https://www.nike.com/')
time.sleep(2)
##driver.implicitly_wait(10)

##pytlocator_0 = driver.find_element(By.XPATH, '//*[@id="hf_cookie_text_cookieAccept"]').click()


locator_1 = driver.find_element(By.ID, 'VisualSearchInput')
time.sleep(5)
##driver.implicitly_wait(10)


wait = WebDriverWait(driver, 10)
search = wait.until(EC.visibility_of_element_located((By.ID, 'VisualSearchInput')))
search.send_keys("Jordan", Keys.ENTER)


##locator_1.send_keys("sneakers", Keys.ENTER)
##locator_1.send_keys(Keys.ENTER)
##time.sleep(5)


##locator_2 = driver.find_element(By.XPATH, '//*[@id="skip-to-products"]/div[3]').click()
##time.sleep(5)
locator_2 = wait.until(EC.element_to_be_clickable(By.XPATH, '//*[@id="skip-to-products"]/div[1]/div/figure/a[2]/div/img')).click()


locator_3 = driver.find_element(By.XPATH, '//*[@id="buyTools"]/div[1]/fieldset/div/div[15]/label').click()
##time.sleep(5)
driver.implicitly_wait(10)

##locator_4 = driver.find_element(By.XPATH, '//*[@id="floating-atc-wrapper"]/div/button[1]').click()
##time.sleep(5)
locator_4 = wait.until(EC.element_to_be_clickable(By.XPATH, '//*[@id="floating-atc-wrapper"]/div/button[1]')).click()
