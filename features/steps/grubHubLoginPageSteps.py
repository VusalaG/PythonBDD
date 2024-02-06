import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch edge browser')
def launchBrowser(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


@when('I open grubhub home page')
def openHomePage(context):
    context.driver.get("https://www.grubhub.com/")


@when('Click on Sign In button')
def signIn(context):
    context.driver.find_element(By.XPATH, "//*[button='Sign in']").click()
    time.sleep(2)


@when('Enter username "{user}" and password "{pwd}"')
def enterParam(context, user, pwd):
    context.driver.find_element(By.XPATH, "//*[@id='email']").send_keys(user)
    context.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)


@when('Click on login button')
def login(context):
    context.driver.find_element(By.XPATH, "//*[button='Sign in']").click()


@then('User must successfully land on main page')
def verify(context):
    # if below try statement throwing an exception, except statement needs to recover it ,handle it.
    # In this case closing the browser and failing test
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id='delivery-button']").text
    except:
        context.driver.close()
        assert False, "Test failed"
    if text == "Delivery":
        context.driver.close()
        # assert False/ True forcefully fails/pass the test
        assert True, "Test passed"
