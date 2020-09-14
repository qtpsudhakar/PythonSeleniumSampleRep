from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser
driver = getDriver('chrome') #session
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.naukri.com/')

# print(driver.current_window_handle)

# print(driver.window_handles)

driver.find_element(By.LINK_TEXT,"LOGIN").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,".social-media .fb-icon").click()

wndHandles = driver.window_handles

currentWindowHandle = driver.current_window_handle

for wnd in wndHandles:
    driver.switch_to.window(wnd)

    # if len(driver.find_elements(By.ID, "email"))>=1:
    #     break

    if "Facebook" in driver.title:
        break
    # driver.switch_to.window("Log in to Facebook | Facebook")

driver.find_element(By.ID,"email").send_keys('abc@gmail.com')

driver.switch_to.window(currentWindowHandle)

driver.close() # closes the active window
driver.quit() # closes the session
