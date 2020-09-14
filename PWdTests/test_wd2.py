import pytest
from selenium.webdriver.common.by import By

from WdTests.DriverFactory import getDriver

@pytest.mark.usefixtures("setupOhrm")
class Test_OhrmAddEmp():

    def test_Login(self):
        self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('qtpsudhakar')
        self.driver.find_element(By.ID, 'txtPassword').submit()


    def test_AddEmployee(self):
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()

        self.driver.find_element(By.ID, "firstName").send_keys("sudhakar")
        self.driver.find_element(By.ID, "lastName").send_keys("ka")

        self.driver.find_element(By.CSS_SELECTOR, "#location_inputfileddiv input.select-dropdown").click()
        self.driver.find_element(By.XPATH,
                            "//div[@id='location_inputfileddiv']//span[contains(text(),'Canadian Regional HQ')]").click()
        self.driver.find_element(By.LINK_TEXT, "NEXT").click()
