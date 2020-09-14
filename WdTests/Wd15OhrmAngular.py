from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome')
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)
driver.maximize_window()

driver.get('https://qtpsudhakarblog-trials65141.orangehrmlive.com/')

wd = WebDriverWait(driver,50)

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
driver.find_element(By.ID,'txtPassword').send_keys('qtpsudhakar')
driver.find_element(By.ID,'txtPassword').submit()
# driver.find_element(By.ID,'btnLogin').click()
driver.find_element(By.LINK_TEXT,"Admin").click()
driver.find_element(By.LINK_TEXT,"User Management").click()
driver.find_element(By.LINK_TEXT,"Users").click()

wd.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='systemUserDiv']//tbody//tr")))
# wd.until(lambda d:len(d.find_elements(By.XPATH, "//div[@id='systemUserDiv']//tbody//tr"))==50)

nUsers = driver.find_element(By.CSS_SELECTOR,"li.summary").text
userCount = nUsers.split(" ")[2]
if len(driver.find_elements(By.XPATH, "//div[@id='systemUserDiv']//tbody//tr"))==int(userCount):
    print(userCount," Elements are displayed")
else:
    print(userCount," Elements are not displayed")
