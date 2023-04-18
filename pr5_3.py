from argparse import Action
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://kolesa.kz/')
time.sleep(2)

img = driver.find_element(By.XPATH, '//*[@id="minPageHotBlock"]/div/div[2]/a/picture/img').click()
time.sleep(2)

print(driver.current_window_handle)
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Колёса — продажа авто в Казахстане. Весь авторынок Казахстана на одном сайте kolesa.kz":
        driver.close()


