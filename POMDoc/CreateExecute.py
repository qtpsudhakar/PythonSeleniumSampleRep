from POMDoc.BasePage import BasePage
from POMDoc.LoginPage import LoginPage

Ohrm = BasePage()
Ohrm.OpenApplication('chrome')
loginpage = LoginPage()
loginpage.login('admin','admin123')

Ohrm.CloseApplication()