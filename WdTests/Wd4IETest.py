from selenium import webdriver #import selenium

# specify browser driver path and open chrome browser
driver = webdriver.Ie(executable_path=r'C:\Users\envy\Desktop\PythonForTestersProject\BD\IEDriverServer.exe')

# navigate t0 url
driver.get('https://www.google.com/')

# get opened page title
print(driver.title)
# close the browser
driver.quit()