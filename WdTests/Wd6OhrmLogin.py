from selenium.webdriver.common.by import By
from WdTests.DriverFactory import getDriver

# specify browser driver path and open chrome browser
driver = getDriver('chrome')

# navigate t0 url
driver.get('https://opensource-demo.orangehrmlive.com/')

driver.find_element('id','txtUsername').send_keys('admin')
driver.find_element(By.ID,'txtPassword').send_keys('admin123')
driver.find_element(By.ID,'btnLogin').click()

# close the browser
driver.quit()