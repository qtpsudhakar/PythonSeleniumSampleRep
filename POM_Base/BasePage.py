from WdTests.DriverFactory import getDriver

class BasePage():
    driver = None
    @classmethod
    def OpenApplication(cls,brName):
        cls.driver = getDriver(brName)
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(20)
        cls.driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Application opened')

    @classmethod
    def CloseApplication(cls):
        cls.driver.quit()
        print('Application closed')

    @classmethod
    def getElement(cls,locator):
        return cls.driver.find_element(*locator)

    @classmethod
    def enterText(cls,locator,val):
        cls.getElement(locator).send_keys(val)
        print(val,"entered on ",locator)

    @classmethod
    def click(cls,locator):
        cls.getElement(locator).click()
        print("clicked on ",locator)

