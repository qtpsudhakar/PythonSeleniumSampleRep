from POM.AddEmpPage import AddEmpPage
from POM.LoginPage import LoginPage
from POM.WelcomePage import WelcomePage
from WdTests.DriverFactory import getDriver

driver = getDriver('chrome')
driver.get('https://opensource-demo.orangehrmlive.com/')
loginpage = LoginPage(driver)
loginpage.enterUserName('admin')
loginpage.enterPassword('admin123')
loginpage.clickOnLogin()

welcomepage = WelcomePage(driver)
welcomepage.clickOnPIMLink()
welcomepage.clickOnAddEmpLink()

addemppage = AddEmpPage(driver)
addemppage.enterFirstName('selenium')
addemppage.enterLastName('webdriver')
addemppage.clickOnSave()