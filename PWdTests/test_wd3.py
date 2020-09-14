import pytest
from selenium.webdriver.common.by import By

from POMDoc.AddEmpPage import AddEmpPage
from POMDoc.WelcomePage import WelcomePage
from POMDoc.LoginPage import LoginPage
from WdTests.DriverFactory import getDriver


@pytest.mark.usefixtures("setupOhrmPOM")
class Test_OhrmAddEmpPomDoc():
    @pytest.mark.dependency()
    def test_Login(self):
        """
        this is login test
        """
        loginpage = LoginPage()
        loginpage.enterText(loginpage.elements.txtUserName,"admin")
        loginpage.enterText(loginpage.elements.txtPassword, "admin1234")
        loginpage.click(loginpage.elements.btnLogin)
        print('Logged in to application')

    @pytest.mark.dependency(depends=["Test_OhrmAddEmpPomDoc::test_Login"])
    def test_AddEmployee(self):
        """
        this is an add emp test
        """
        welcomePage = WelcomePage()
        welcomePage.click(welcomePage.elements.lnkPIM)
        welcomePage.click(welcomePage.elements.btnAddEmp)
        print('Navigated to welcome page')
        addEmpPage = AddEmpPage()
        addEmpPage.enterText(addEmpPage.elements.txtFirstName,"selenium")
        addEmpPage.enterText(addEmpPage.elements.txtLastName, "webdriver")
        addEmpPage.click(addEmpPage.elements.btnSave)
        print('employee added')

