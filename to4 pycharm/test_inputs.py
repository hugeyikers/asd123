"""The <input type=number> field – send_keys, clear, keys."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/inputs"
FIELD = (By.CSS_SELECTOR, "input[type='number']")


@pytest.mark.parametrize("typed, expected", [
    ("10", "10"),        # positive number
    ("-25", "-25"),      # negative number
    ("abc", ""),         # letters – the browser rejects them
])
def test_typing(driver, typed, expected):
    field = open_page(driver, URL, *FIELD)
    field.send_keys(typed)
    assert field.get_property("value") == expected


def test_arrows_and_clear(driver):
    field = open_page(driver, URL, *FIELD)
    field.send_keys("5", Keys.ARROW_UP, Keys.ARROW_UP)
    assert field.get_property("value") == "7"
