from selenium.webdriver.common.by import By

from WdTests.DriverFactory import getDriver

class WelcomePage():

    lnkPIM      = By.LINK_TEXT, "PIM"
    btnAddEmp   = By.ID,'btnAdd'

    def __init__(self,driver):
        self.driver = driver

    def clickOnPIMLink(self):
        self.driver.find_element(*self.lnkPIM).click()
        print("clicked on PIM link")

    def clickOnAddEmpLink(self):
        self.driver.find_element(*self.btnAddEmp).click()
        print("clicked on Add Emp Button")

if __name__=="__main__":
    pass


