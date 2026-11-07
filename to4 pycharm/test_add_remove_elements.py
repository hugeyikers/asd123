"""Adding and removing elements – find_elements() and count."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/add_remove_elements/"
ADD = (By.CSS_SELECTOR, "button[onclick='addElement()']")
DELETE = (By.CSS_SELECTOR, "#elements button")


def test_no_buttons_at_start(driver):
    open_page(driver, URL, *ADD)
    assert driver.find_elements(*DELETE) == []   # empty list


def test_add_three_delete_one(driver):
    add = open_page(driver, URL, *ADD)
    for _ in range(3):
        add.click()
    buttons = driver.find_elements(*DELETE)
    assert len(buttons) == 3
