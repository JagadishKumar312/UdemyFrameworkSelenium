import time
import pytest
from selenium import webdriver


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("admin")
time.sleep(2)
driver.find_element(By.NAME,"pwd").send_keys("manager")
time.sleep(2)
driver.find_element(By.XPATH,"//div[normalize-space()='Login']")
time.sleep(3)