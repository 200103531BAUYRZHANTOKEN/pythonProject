from argparse import Action
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://demo.automationtesting.in/Alerts.html')
time.sleep(2)


#alert3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
#time.sleep(2)
#alert4 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button').click()
#time.sleep(2)
#alert4 = driver.switch_to.alert
#time.sleep(2)
#alert4.accept()
#alert4 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button').click()
#alert4.dismiss()


alert5 =driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
time.sleep(2)
alert6 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button').click()
time.sleep(2)
alert6 = driver.switch_to.alert
alert6.send_keys('Test')
alert6.send_keys(Keys.ENTER)
alert6.accept()

