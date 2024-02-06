import time

from behave import *
from selenium.webdriver.common.by import By


@when('Click profile button')
def profileClick(context):
    # //div [@class='mainNavCol mainNavProfile']
    context.driver.find_element(By.XPATH, "//div [@class='mainNavCol mainNavProfile']").click()
    time.sleep(2)


@when('Click on Payment button')
def paymentClick(context):
    context.driver.find_element(By.XPATH, "//div[@data-testid='mainNav-dropdown-innerMenu']//a[.='Payments']").click()


@then('Your Account page should be displayed')
def verify_account(context):
    text = context.driver.find_element(By.XPATH, "//span[@data-testid='account-nav']//*[contains(text(),'Your account')]").text
    assert text == "Your account"


@when('CLick on Help button')
def helpClick(context):
    context.driver.find_element(By.XPATH, "//span[@data-testid='main-nav-dropdown']//*[contains(text(),'Help')]").click()


@then('Help page should be displayed')
def verify_help(context):
    text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'How can we help?')]").text
    assert text == "How can we help?"
