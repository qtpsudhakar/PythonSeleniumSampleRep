import config
from WdTests.DriverFactory import getDriver
from config import logger as log
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
        log.info(f"{val}, entering on {locator.name}:{locator.value}")
        cls.getElement(locator.value).send_keys(val)
        print(val,"entered on ",cls.getDoc(locator.name))
        log.info(f"{val}, entered on {locator.name}:{locator.value}")

    @classmethod
    def click(cls,locator):
        log.info(f"clicking on entered on {locator.name}:{locator.value}")
        cls.getElement(locator.value).click()
        print("clicked on ",cls.getDoc(locator.name))
        log.info(f"clicked on entered on {locator.name}:{locator.value}")

    @classmethod
    def getDoc(cls,elmname:str):
        if elmname.startswith('txt'):
            return f'{elmname[3:]} text box'
        elif elmname.startswith('btn'):
            return f'{elmname[3:]} button'
        elif elmname.startswith('lnk'):
            return f'{elmname[3:]} link'
        elif elmname.startswith('chk'):
            return f'{elmname[3:]} checkbox'
        elif elmname.startswith('rdb'):
            return f'{elmname[3:]} radio button'
        elif elmname.startswith('lst'):
            return f'{elmname[3:]} listbox'
    @classmethod
    def getScreenshot(cls,flname):
        flPath = config.GetDir().SCREENSHOTDIR+'/'+flname
        cls.driver.get_screenshot_as_file(flPath)
        return flPath

    @classmethod
    def getScreenshotBase(cls):
        return cls.driver.get_screenshot_as_base64()
