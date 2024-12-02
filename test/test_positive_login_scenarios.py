from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # navigation to the app
    login_page.open_home_page()

    # filling form
    login_page.type_user_name("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    # validation of redirection

    products_page = ProductsPage(browser=browser)
    products_page.validate_products_page_title()
