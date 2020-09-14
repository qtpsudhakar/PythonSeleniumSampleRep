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

driver.get('https://jqueryui.com/droppable/')

act = ActionChains(driver)
act.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT,"view source")).perform()

frm = driver.find_element(By.CSS_SELECTOR,"iframe.demo-frame")

driver.switch_to.frame(frm)
src = driver.find_element(By.ID,"draggable")
dst = driver.find_element(By.ID,"droppable")

# loc = dst.location
# ActionChains(driver).drag_and_drop_by_offset(src,loc['x'],loc['y']).perform()
ActionChains(driver).drag_and_drop(src,dst).perform()

# driver.switch_to.parent_frame()
# driver.switch_to.default_content()


