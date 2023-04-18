from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


# set up the webdriver
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1409245047%3A1679890447701194&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ifkv=AQMjQ7T_lADnvOe0PYIGjUeenxyg7naEir3luNU-MvZMOIZ5Hn1KHQH2-HsXaqBgVo9YdYyn-AuNcw&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

email = driver.find_element(By.XPATH, "//input[@type='email']")
email.send_keys("200103531@stu.sdu.edu.kz")
time.sleep(2)
but1 = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
time.sleep(5)

password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("baukatoken02")
time.sleep(2)
but2 = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
time.sleep(5)

test2 = driver.find_element(By.XPATH, '//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[1]/div/div/div/div[2]/div/div')
test1 = driver.find_element(By.XPATH, '//*[@id=":5"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz[1]/c-wiz/div/c-wiz[2]/div/div/div/div[2]/div/div')

actions = ActionChains(driver)
actions.drag_and_drop(test1, test2).perform()
time.sleep(10)
actions.double_click(test2).perform()
time.sleep(10)

test1_1 = driver.find_element(By.CLASS_NAME, 'KL4NAf')
Driver = driver.find_element(By.XPATH, '//*[@id="nt:Dr:label"]/div/span')
action = ActionChains(driver)
action.drag_and_drop(test1_1, Driver).perform()
time.sleep(10)
action.double_click(Driver).perform()
time.sleep(10)
driver.quit()
