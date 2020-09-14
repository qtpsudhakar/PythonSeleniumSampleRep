from selenium.webdriver.common.by import By

from POM_Base.BasePage import BasePage
from WdTests.DriverFactory import getDriver

class LoginPage(BasePage):

    txtUserName = By.XPATH, "//input[@id='txtUsername']"
    txtPassword = By.ID, 'txtPassword'
    btnLogin    = By.ID,'btnLogin'

    def enterUserName(self,uname):
        # self.getElement(*self.txtUserName).send_keys(uname)
        self.enterText(self.txtUserName,uname)
        print(uname,"entered on User Name")

    def enterPassword(self,pwd):
        self.enterText(self.txtPassword,pwd)
        print(pwd, "entered on Password")

    def clickOnLogin(self):
        self.click(self.btnLogin)
        print("clicked on Login Button")

    def login(self,uname,pwd):
        self.enterUserName(uname)
        self.enterPassword(pwd)
        self.clickOnLogin()
        print("Logged in to application")


if __name__=="__main__":
    pass