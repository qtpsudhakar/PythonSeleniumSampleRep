from enum import Enum

from selenium.webdriver.common.by import By

from POMDoc.BasePage import BasePage
from WdTests.DriverFactory import getDriver

class WelcomePage(BasePage):
    class elements(Enum):
        lnkPIM = By.LINK_TEXT, "PIM"
        btnAddEmp = By.ID, 'btnAdd'

    def navigateToAddEmp(self,uname,pwd):
        self.click(self.elements.lnkPIM)
        self.click(self.elements.btnAddEmp)
        print("Navigated to Add Employee Page")

if __name__=="__main__":
    pass