from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome')

driver.maximize_window()
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get('https://www.redbus.in/')

driver.find_element(By.ID,'onward_cal').click()

while True:
    month = driver.find_element(By.CLASS_NAME, 'monthTitle').text
    if month=='Dec 2020':
        driver.find_element(By.XPATH,'//td[text()="20"]').click()
        break
    else:
        driver.find_element(By.CSS_SELECTOR,'td.next').click()
