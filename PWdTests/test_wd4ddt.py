import pytest
from selenium.webdriver.common.by import By

from POMDoc.AddEmpPage import AddEmpPage
from POMDoc.WelcomePage import WelcomePage
from POMDoc.LoginPage import LoginPage
from WdTests.DriverFactory import getDriver
from config import logger as log
@pytest.mark.usefixtures("setupOhrmPOM","getTCData")
class Test_OhrmAddEmpPomDoc():

    def test_Login(self):
        loginpage = LoginPage()
        loginpage.enterText(loginpage.elements.txtUserName,self.data["username"])
        loginpage.enterText(loginpage.elements.txtPassword, self.data["password"])
        loginpage.click(loginpage.elements.btnLogin)
        print('Logged in to application')
        log.info("Logged in to application")

    def test_AddEmployee(self):
        welcomePage = WelcomePage()
        welcomePage.click(welcomePage.elements.lnkPIM)
        welcomePage.click(welcomePage.elements.btnAddEmp)
        print('Navigated to welcome page')
        addEmpPage = AddEmpPage()
        addEmpPage.enterText(addEmpPage.elements.txtFirstName,self.data["firstname"])
        addEmpPage.enterText(addEmpPage.elements.txtLastName, self.data["lastname"])
        addEmpPage.click(addEmpPage.elements.btnSave)
        print('employee added')

