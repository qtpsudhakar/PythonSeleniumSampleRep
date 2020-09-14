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

# if id exist
driver.find_element(By.ID,'personal_optGender_1').click()

# if id doesn't exist
# driver.find_elements(By.NAME,'personal[optGender]')[1].click()

lstElm = driver.find_element(By.ID,'personal_cmbNation')
Select(lstElm).select_by_visible_text('Indian')
Select(lstElm).select_by_value('82')
Select(lstElm).select_by_index(4)
driver.find_element(By.XPATH,'//input[@value="Save"]').click()

driver.find_element(By.LINK_TEXT,'PIM').click()

chk = driver.find_element(By.ID,'ohrmList_chkSelectAll')
print(chk.is_selected())
if not chk.is_selected():
    chk.click()
time.sleep(5)
# close the browser
driver.quit()

# Select(lstElm).options
# lstElm.find_elements(By.TAG_NAME,"option")
# driver.find_elements(By.XPATH,"//select[@id='personal_cmbNation']/option")