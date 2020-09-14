from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome') #session
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://api.jquery.com/dblclick/')

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"div.demo.code-demo iframe"))

act = ActionChains(driver)

act.move_to_element(driver.find_element(By.TAG_NAME,"div")).perform()

driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.TAG_NAME,"div"))
# driver.execute_script("document.getElementById('id').scrollIntoView();")
# driver.execute_script("document.getElementById('id').click();")

#Using javascript we can work like a developer
