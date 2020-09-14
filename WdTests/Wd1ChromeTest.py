from selenium import webdriver #import selenium
from pathlib import Path
import os

# specify browser driver path and open chrome browser
driver = webdriver.Chrome(executable_path=os.path.abspath('./../BD/chromedriver.exe'))

# navigate t0 url
driver.get('https://www.google.com/')
# get opened page title
print(driver.title)
# close the browser
# print(os.path.abspath(r'.\..\BD\chromedriver.exe'))