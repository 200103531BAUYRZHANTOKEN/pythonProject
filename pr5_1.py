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

alert2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a').click()
time.sleep(1)
alert1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button').click()
time.sleep(2)
alert1 = driver.switch_to.alert
time.sleep(2)
alert1.accept()
time.sleep(2)


alert3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a').click()
time.sleep(2)
alert4 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button').click()
time.sleep(2)
alert4 = driver.switch_to.alert
time.sleep(2)
alert4.accept()
alert4 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button').click()
alert4.dismiss()
