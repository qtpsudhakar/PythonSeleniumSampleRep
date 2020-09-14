from enum import Enum

from selenium.webdriver.common.by import By

from POMDoc.BasePage import BasePage
from WdTests.DriverFactory import getDriver

class LoginPage(BasePage):
    class elements(Enum):
        txtUserName = By.XPATH, "//input[@id='txtUsername']"
        txtPassword = By.ID, 'txtPassword'
        btnLogin    = By.ID,'btnLogin'

    def login(self,uname,pwd):
        self.enterText(self.elements.txtUserName,uname)
        self.enterText(self.elements.txtPassword,pwd)
        self.click(self.elements.btnLogin)
        print("Logged in to application")


if __name__=="__main__":
    pass