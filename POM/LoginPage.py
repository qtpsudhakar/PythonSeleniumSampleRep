from selenium.webdriver.common.by import By

from WdTests.DriverFactory import getDriver

class LoginPage():

    txtUserName = By.XPATH, "//input[@id='txtUsername']"
    txtPassword = By.ID, 'txtPassword'
    btnLogin    = By.ID,'btnLogin'

    def __init__(self,driver):
        self.driver = driver

    def enterUserName(self,uname):
        self.driver.find_element(*self.txtUserName).send_keys(uname)
        print(uname,"entered on User Name")

    def enterPassword(self,pwd):
        self.driver.find_element(*self.txtPassword).send_keys(pwd)
        print(pwd, "entered on Password")

    def clickOnLogin(self):
        self.driver.find_element(*self.btnLogin).click()
        print("clicked on login button")

if __name__=="__main__":
    pass