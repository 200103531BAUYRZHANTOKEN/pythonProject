import time

from selenium import webdriver

driver = webdriver.Chrome()


driver.get('https://www.reddit.com/')

time.sleep(5)

driver.get('https://www.nike.com/')

time.sleep(5)

driver.get('https://www.youtube.com/')

time.sleep(5)
