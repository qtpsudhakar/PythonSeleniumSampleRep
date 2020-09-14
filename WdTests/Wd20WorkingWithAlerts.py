from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome')

driver.maximize_window()
driver.set_page_load_timeout(50)
driver.implicitly_wait(10)

driver.get('https://www.apsrtconline.in/oprs-web/')

driver.find_element(By.ID,'searchBtn').click()

time.sleep(2)
al = driver.switch_to.alert

if al.text=="Please select start place.":
    print('From place validation is successful')
else:
    print('From place validation is failed')

al.accept()

driver.find_element(By.ID,'fromPlaceName').send_keys('VISAKHAPATNAM')
driver.find_element(By.LINK_TEXT,'VISAKHAPATNAM').click()

driver.find_element(By.ID,'searchBtn').click()
time.sleep(2)
print(al.text)
al.accept()

driver.find_element(By.ID,'toPlaceName').send_keys('TIRUPATHI')
driver.find_element(By.LINK_TEXT,'TIRUPATHI').click()

driver.find_element(By.ID,'txtJourneyDate').click()
driver.find_element(By.LINK_TEXT,"14").click()

driver.find_element(By.ID,'searchBtn').click()
