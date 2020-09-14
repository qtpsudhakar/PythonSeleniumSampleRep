import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from WdTests.DriverFactory import getDriver
import time

from pywinauto.application import Application
from pywinauto.application import findwindows

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

driver.find_element(By.LINK_TEXT,"PIM").click()
driver.find_element(By.LINK_TEXT,"Add Employee").click()

driver.find_element(By.ID,"firstName").send_keys("sudhakar")
driver.find_element(By.ID,"lastName").send_keys("ka")

driver.find_element(By.CSS_SELECTOR,"#location_inputfileddiv input.select-dropdown").click()
driver.find_element(By.XPATH,"//div[@id='location_inputfileddiv']//span[contains(text(),'Canadian Regional HQ')]").click()

driver.find_element(By.CSS_SELECTOR,"label#photo-preview-lable").click()
# driver.find_element(By.CSS_SELECTOR,"label#photo-preview-lable").send_keys(r"C:\Users\envy\Desktop\PythonForTestersB2\selenium.png")

time.sleep(2)

app = Application()
hwnd = findwindows.find_windows(class_name='#32770',title='Open')
print(hwnd)
window = app.connect(handle=hwnd[0])
# app.top_window().PrintControlIdentifiers()
app.top_window().Edit.type_keys('{}'.format(r"C:\Users\envy\Desktop\PythonForTestersB2\selenium.png"))
app.top_window()['&OpenButton'].click()

