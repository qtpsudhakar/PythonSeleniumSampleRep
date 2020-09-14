from behave import given, when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(U'sudhakar launch Chrome Browser')
def launchBrowser(context):
    context.driver:webdriver = webdriver.Chrome(executable_path='BD/chromedriver.exe')

@given(U'sudhakar navigated orangehrm url')
def navigateToApp(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@when(U'sudhakar enter username and password')
def enterLoginDetails(context):
    context.driver.find_element(By.ID, 'txtUsername').send_keys('admin')
    context.driver.find_element(By.ID, 'txtPassword').send_keys('admin123')

@when(U'sudhakar click on Login button')
def clickOnLogin(context):
    context.driver.find_element(By.ID,'btnLogin').click()

@then(U'sudhakar should see welcome page')
def verifyWelcomePage(context):
    print('welcome page displayed')

