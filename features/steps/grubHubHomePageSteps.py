from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch safari browser')
def launchBrowser(context):
    # I moved chrome and edge drivers into Scripts file, so now I can skip passing the webdriver path below
    # self.driver = webdriver.Edge("C:\webdrivers\edgedriver_win64\msedgedriver.exe")
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


@when('open grubhub home page')
def openHomePage(context):
    context.driver.get("https://www.grubhub.com")


@then('verify that logo presence on the page')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//*[@id='Site']//*[@class='mainNavBrand-logo']").is_displayed()
    assert logo is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
