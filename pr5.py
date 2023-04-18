from argparse import Action
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



driver = webdriver.Chrome()

driver.get('https://gate2home.com/English-Keyboard')
driver.implicitly_wait(10)

capslock = driver.find_element(By.XPATH, '//*[@id="kb_bcaps"]/div').click()
a = driver.find_element(By.XPATH, '//*[@id="kb_b26"]/div').click()
u = driver.find_element(By.XPATH, '//*[@id="kb_b20"]').click()
t = driver.find_element(By.XPATH, '//*[@id="kb_b18"]/div').click()
o = driver.find_element(By.XPATH, '//*[@id="kb_b22"]/div').click()
m = driver.find_element(By.XPATH, '//*[@id="kb_b43"]/div').click()
a1 = driver.find_element(By.XPATH, '//*[@id="kb_b26"]/div/span[5]').click()
t1 = driver.find_element(By.XPATH, '//*[@id="kb_b18"]/div').click()
i = driver.find_element(By.XPATH, '//*[@id="kb_b21"]/div').click()
o1 = driver.find_element(By.XPATH, '//*[@id="kb_b22"]/div').click()
n = driver.find_element(By.XPATH, '//*[@id="kb_b42"]/div').click()

space = driver.find_element(By.XPATH, '//*[@id="kb_bspace"]/div').click()
t2 = driver.find_element(By.XPATH, '//*[@id="kb_b18"]/div').click()
e = driver.find_element(By.XPATH, '//*[@id="kb_b16"]/div').click()
s = driver.find_element(By.XPATH, '//*[@id="kb_b27"]/div').click()
t3 = driver.find_element(By.XPATH, '//*[@id="kb_b18"]/div').click()
i1 = driver.find_element(By.XPATH, '//*[@id="kb_b21"]/div').click()
n1 = driver.find_element(By.XPATH, '//*[@id="kb_b42"]/div').click()
g = driver.find_element(By.XPATH, '//*[@id="kb_b30"]/div').click()



result = driver.find_element(By.XPATH,'//*[@id="textbox1_freetext"]')

actions = ActionChains(driver)
actions.click(capslock)
actions.click(a)
actions.click(u)
actions.click(t)
actions.click(o)
actions.click(m)
actions.click(a1)
actions.click(t1)
actions.click(i)
actions.click(o1)
actions.click(n)
actions.click(space)
actions.click(t2)
actions.click(e)
actions.click(s)
actions.click(t3)
actions.click(i1)
actions.click(n1)
actions.click(g)


result_txt = result.text
print(result_txt)




