from selenium import webdriver #import selenium

# specify browser driver path and open chrome browser
driver = webdriver.Firefox(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\geckodriver.exe')

driver.set_page_load_timeout(10)

# navigate t0 url
driver.get('https://www.facebook.com/')
# get opened page title
print(driver.title)
# close the browser
driver.quit()


