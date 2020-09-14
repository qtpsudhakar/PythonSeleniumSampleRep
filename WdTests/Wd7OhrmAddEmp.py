from selenium.webdriver.common.by import By
from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome')

driver.maximize_window()
# navigate t0 url
driver.get('https://qtpsudhakaranz-trials653.orangehrmlive.com/')

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('sudhakar')
driver.find_element(By.ID,'txtPassword').send_keys('qtpsudhakar')
driver.find_element(By.ID,'btnLogin').click()

driver.find_element(By.LINK_TEXT,'PIM').click() # finds a single element
time.sleep(1) #static
driver.find_elements(By.LINK_TEXT,'Add Employee')[0].click() # finds multiple elements by given locator

# close the browser
driver.quit()




sno = driver.find_elements(By.XPATH,'//div[@class="srvceNO"]')
for s in sno:
    if s.is_displayed():
        print(s.text)

