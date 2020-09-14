from POM_Base.BasePage import BasePage
from POM_Base.LoginPage import LoginPage

Ohrm = BasePage()
Ohrm.OpenApplication('chrome')
loginpage = LoginPage()
loginpage.enterUserName('admin')
loginpage.enterPassword('admin123')
loginpage.clickOnLogin()

Ohrm.CloseApplication()