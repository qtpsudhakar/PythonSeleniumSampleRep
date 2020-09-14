from selenium.webdriver.common.by import By

from WdTests.DriverFactory import getDriver


class Test_OhrmAddEmp():

    driver = getDriver('chrome')

    def test_openAppliaction(self):
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('https://qtpsudhakarblog-trials65141.orangehrmlive.com/')
        # assert self.driver.title=="OrangeHRM"

    def test_Login(self):
        self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('qtpsudhakar')
        self.driver.find_element(By.ID, 'txtPassword').submit()

    def test_closeApplication(self):
        self.driver.quit()
