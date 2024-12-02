from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_locked_out_user_login(browser):
    login_page = LoginPage(browser)

    # navigation to the app
    login_page.open_home_page()

    # filling form
    login_page.type_user_name("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    # Error validation
    error_message_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    print(F"{error_message_text = }")
    assert error_message_text == 'Epic sadface: Sorry, this user has been locked out.'
