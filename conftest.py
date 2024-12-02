from time import sleep
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # after test
    driver.quit()
    sleep(3)
