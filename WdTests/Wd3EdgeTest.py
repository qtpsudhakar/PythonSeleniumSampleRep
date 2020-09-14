from selenium import webdriver #import selenium

# specify browser driver path and open chrome browser
driver = webdriver.Edge(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\msedgedriver.exe')

# navigate to url
driver.get('https://www.google.com/')

# get opened page title
print(driver.title)
# close the browser
driver.quit()