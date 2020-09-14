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

driver.find_element(By.ID,"photofile").send_keys(r"C:\Users\envy\Desktop\PythonForTestersB2\selenium.png")

driver.find_element(By.XPATH,'//input[@value="Save"]').click()
