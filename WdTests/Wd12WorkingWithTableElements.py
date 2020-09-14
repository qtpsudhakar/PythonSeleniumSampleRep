from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome')
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

wd = WebDriverWait(driver,20)

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
driver.find_element(By.ID,'txtPassword').send_keys('admin123')
driver.find_element(By.ID,'txtPassword').submit()
# driver.find_element(By.ID,'btnLogin').click()

lnkPIM = wd.until(EC.presence_of_element_located((By.LINK_TEXT,'PIM')))
lnkPIM.click()
# driver.find_element(By.LINK_TEXT,'PIM').click() # finds a single element
driver.find_element(By.ID,'btnAdd').click()
driver.find_element(By.ID,'firstName').send_keys('selenium')
driver.find_element(By.ID,'lastName').send_keys('webdriver')
driver.find_element(By.XPATH,'//input[@value="Save"]').click()

empId = driver.find_element(By.ID,"personal_txtEmployeeId").get_attribute('value')
driver.find_element(By.LINK_TEXT,"Employee List").click()

# Explicit waiting
chk = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,f"//a[text()='{empId}']/../..//input")))
chk.click()
driver.find_element(By.ID,'btnDelete').click()
driver.find_element(By.ID,"dialogDeleteBtn").click()