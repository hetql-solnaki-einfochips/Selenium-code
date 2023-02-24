import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.implicitly_wait(5)
driver.find_element(By.NAME,"firstname").send_keys("John")
driver.find_element(By.NAME,"lastname").send_keys("Solanki")
driver.find_element(By.NAME,"reg_email__").send_keys("john@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys("Snow123@#")
driver.implicitly_wait(5)
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text('20')

select_month=Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text('Dec')

select_year=Select(driver.find_element(By.ID,"year"))
select_year.select_by_visible_text('2008')

driver.find_element(By.XPATH,"//label[text()='Custom']").click() #Xpath: //tagname[@attribute=''] or /tagname[text()='']
driver.find_element(By.NAME, "websubmit").click()
time.sleep(20)
driver.quit()