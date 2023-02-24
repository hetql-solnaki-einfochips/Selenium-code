import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.db4free.net/")
driver.find_element(By.XPATH,"//a[@href='/phpMyAdmin']").click()
print(driver.title)

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID,'input_username').send_keys("Heta")
driver.find_element(By.ID,'input_password').send_keys("hetal2325")
driver.find_element(By.ID, 'input_go').click()

time.sleep(5)
driver.quit()