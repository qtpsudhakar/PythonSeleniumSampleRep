from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome')

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
driver.find_element(By.ID,'txtPassword').send_keys('admin123')
driver.find_element(By.ID,'txtPassword').submit()
# driver.find_element(By.ID,'btnLogin').click()

driver.find_element(By.LINK_TEXT,'PIM').click() # finds a single element
driver.find_element(By.ID,'btnAdd').click()
driver.find_element(By.ID,'firstName').send_keys('selenium')
driver.find_element(By.ID,'lastName').send_keys('webdriver')
driver.find_element(By.XPATH,'//input[@value="Save"]').click()

driver.find_element(By.XPATH,'//input[@value="Edit"]').click()

driver.find_element(By.XPATH,"//label[text()='License Expiry Date']/../img[@class='ui-datepicker-trigger']").click()

yearList = driver.find_element(By.CLASS_NAME,'ui-datepicker-year')
Select(yearList).select_by_visible_text("2022")

monthList = driver.find_element(By.CLASS_NAME,'ui-datepicker-month')
Select(monthList).select_by_visible_text("Dec")

driver.find_element(By.LINK_TEXT,"20").click()
