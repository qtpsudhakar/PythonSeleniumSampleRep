from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from WdTests.DriverFactory import getDriver
import time
# specify browser driver path and open chrome browser

class Ohrm():
    def __init__(self):
        self.driver = getDriver('chrome')
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('https://qtpsudhakarblog-trials65141.orangehrmlive.com/')
    def login(self):
        self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('qtpsudhakar')
        self.driver.find_element(By.ID, 'txtPassword').submit()


driver = getDriver('chrome')
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)
driver.maximize_window()

driver.get('https://qtpsudhakarblog-trials65141.orangehrmlive.com/')

wd = WebDriverWait(driver,50)

driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
driver.find_element(By.ID,'txtPassword').send_keys('qtpsudhakar')
driver.find_element(By.ID,'txtPassword').submit()

driver.find_element(By.LINK_TEXT,"PIM").click()
driver.find_element(By.LINK_TEXT,"Add Employee").click()

driver.find_element(By.ID,"firstName").send_keys("sudhakar")
driver.find_element(By.ID,"lastName").send_keys("ka")

driver.find_element(By.CSS_SELECTOR,"#location_inputfileddiv input.select-dropdown").click()
driver.find_element(By.XPATH,"//div[@id='location_inputfileddiv']//span[contains(text(),'Canadian Regional HQ')]").click()

driver.find_element(By.LINK_TEXT,"NEXT").click()

driver.find_element(By.XPATH,"//input[@id='emp_birthday']/..//i").click()

driver.find_element(By.CSS_SELECTOR,"div.picker__select--year input").click()
driver.find_element(By.XPATH,"//li[normalize-space()='1983' and not(ancestor-or-self::*[contains(@aria-hidden,'true')])]").click()

driver.find_element(By.CSS_SELECTOR,"div.picker__select--month input").click()
driver.find_element(By.XPATH,"//li[normalize-space()='April' and not(ancestor-or-self::*[contains(@aria-hidden,'true')])]").click()

driver.find_element(By.XPATH,"//div[text()='20' and not(ancestor-or-self::*[contains(@aria-hidden,'true')])]").click()

# 90% of actions are click, enter text, select
