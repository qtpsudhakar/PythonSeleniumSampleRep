from WdTests.DriverFactory import getDriver

# specify browser driver path and open chrome browser
driver = getDriver('firefox')

# navigate t0 url
driver.get('https://www.google.com/')

# get opened page title
print(driver.title)
# close the browser
driver.quit()