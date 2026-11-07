"""Login on the-internet – equivalence partitioning (EP)."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page, wait_for
from selenium.webdriver.support.relative_locator import locate_with

USERNAME, PASSWORD = "tomsmith", "SuperSecretPassword!"


def log_in(driver, username, password):
    """Fills in the form; returns the #flash message."""
    open_page(driver, f"{INTERNET_URL}/login", By.ID, "login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#login button").click()
    return wait_for(driver, By.ID, "flash")


@pytest.mark.parametrize("username, password, message, path", [
    (USERNAME, PASSWORD, "You logged into a secure area!", "/secure"),
    ("tomek", PASSWORD, "Your username is invalid!", "/login"),
    (USERNAME, "asdfhaslo", "Your password is invalid!", "/login"),
    ("", "", "Your username is invalid!", "/login"),
    ("zlylogin", "zlehaslo", "Your username is invalid!", "/login"),
], ids=["valid", "wrong-username", "wrong-password", "empty-fields", "wrong-both"])
def test_login_ep(driver, username, password, message, path):
    flash = log_in(driver, username, password)
    assert message in flash.text
    assert driver.current_url.endswith(path)


def test_message_css_class(driver):
    flash = log_in(driver, USERNAME, "wrongpassword")
    assert "error" in flash.get_attribute("class").split()

def test_locate_with(driver):
    open_page(driver, f"{INTERNET_URL}/login", By.ID, "login")
    password_field = driver.find_element(
        locate_with(By.TAG_NAME, "input").below({By.ID: "username"})
    )
    assert password_field.get_attribute("id") == "password"
