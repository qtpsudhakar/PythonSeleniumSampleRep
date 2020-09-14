import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By

scenarios('../features/OhrmAddEmployee.feature')

@given('sudhakar launch Chrome Browser')
def browser():
    driver:webdriver = webdriver.Chrome()
    return driver

@given('sudhakar navigated orangehrm url')
def navigateToApp(browser):
    browser.get('https://opensource-demo.orangehrmlive.com/')

@when('sudhakar enter username and password')
def enterLoginDetails(browser):
    browser.find_element(By.ID, 'txtUsername').send_keys('admin')
    browser.find_element(By.ID, 'txtPassword').send_keys('admin123')

@when('sudhakar click on Login button')
def clickOnLogin(browser):
    browser.find_element(By.ID,'btnLogin').click()

@then('sudhakar should see welcome page')
def verifyWelcomePage(browser):
    print('welcome page displayed')

