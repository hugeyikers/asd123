"""First tests: open a page and check its title."""
from selenium.webdriver.common.by import By
from config import INTERNET_URL, SELENIUM_WEB_URL
from helpers import open_page


def test_title_the_internet(driver):
    open_page(driver, f"{INTERNET_URL}/login", By.ID, "login")
    assert driver.title == "The Internet"


def test_title_web_form(driver):
    open_page(driver, f"{SELENIUM_WEB_URL}/web-form.html",
              By.TAG_NAME, "form")
    assert driver.title == "Web form"
    assert driver.current_url.endswith("/web-form.html")