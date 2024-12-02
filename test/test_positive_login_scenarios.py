from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_standard_user_login(browser):
    login_page = LoginPage(browser)

    # navigation to the app
    login_page.open_home_page()

    # filling form
    login_page.type_user_name("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    # validation of redirection
    current_url = browser.current_url
    print(f"{current_url = }")
    assert current_url == "https://www.saucedemo.com/inventory.html"
    products_page_title = browser.find_element(By.XPATH, '//*[@data-test="title"]').text
    print(f"{products_page_title = }")
    assert products_page_title == "Products"
