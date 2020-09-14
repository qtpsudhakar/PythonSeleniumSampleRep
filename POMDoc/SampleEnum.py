from enum import Enum
from selenium.webdriver.common.by import By

class Demo(Enum):
    txtUserName = By.XPATH, "//input[@id='txtUsername']"

print(Demo.txtUserName.name)
print(Demo.txtUserName.value)

# Demo.txtUserName = By.XPATH, "//input[@id='txtUsername1']"
# print(Demo.txtUserName.value)

st = Demo.txtUserName.name
print(st[3:])