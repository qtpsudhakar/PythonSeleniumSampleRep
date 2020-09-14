from enum import Enum

from selenium.webdriver.common.by import By

from POMDoc.BasePage import BasePage
from WdTests.DriverFactory import getDriver

class AddEmpPage(BasePage):
    class elements(Enum):
        txtFirstName = By.ID, "firstName"
        txtLastName = By.ID, 'lastName'
        btnSave = By.XPATH, '//input[@value="Save"]'

    def AddEmployee(self, fname):
        self.enterText(self.elements.txtFirstName,"selenium")
        self.enterText(self.elements.txtLastName, "webdriver")
        self.click(self.elements.btnSave)
        print("Employee Added")

if __name__=="__main__":
    pass