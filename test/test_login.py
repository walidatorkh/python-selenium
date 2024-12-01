from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    #after test
    driver.quit()
    sleep(3)


def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # navigation to the app
    login_page.open_home_page()

    #filling form
    login_page.type_user_name("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    #validation of redirection
    current_url = browser.current_url
    print(f"{current_url = }")
    assert current_url == "https://www.saucedemo.com/inventory.html"
    products_page_title = browser.find_element(By.XPATH, '//*[@data-test="title"]').text
    print(f"{products_page_title = }")
    assert products_page_title == "Products"


def test_locked_out_user_login(browser):
    login_page = LoginPage(browser)

    # navigation to the app
    login_page.open_home_page()

    #filling form
    login_page.type_user_name("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    #Error validation
    error_message_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    print(F"{error_message_text = }")
    assert error_message_text == 'Epic sadface: Sorry, this user has been locked out.'
