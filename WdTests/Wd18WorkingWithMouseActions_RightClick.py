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

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

act = ActionChains(driver)
act.context_click(driver.find_element(By.XPATH,"//span[text()='right click me']")).\
    click(driver.find_element(By.XPATH,"//span[text()='Edit']")).perform()



