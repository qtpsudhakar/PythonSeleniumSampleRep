from selenium.webdriver.common.by import By

from WdTests.DriverFactory import getDriver

class AddEmpPage():

    txtFirstName    = By.ID, "firstName"
    txtLastName     = By.ID, 'lastName'
    btnSave         = By.XPATH,'//input[@value="Save"]'

    def __init__(self,driver):
        self.driver = driver

    def enterFirstName(self,fname):
        self.driver.find_element(*self.txtFirstName).send_keys(fname)
        print(fname,"entered on first name text box")

    def enterLastName(self,lname):
        self.driver.find_element(*self.txtLastName).send_keys(lname)
        print(lname, "entered on last name text box")

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()
        print("clicked on save button")
