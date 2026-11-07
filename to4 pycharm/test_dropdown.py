"""Dropdown list – the Select class."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/dropdown"


def test_dropdown_options(driver):
    dropdown = Select(open_page(driver, URL, By.ID, "dropdown"))
    texts = [o.text for o in dropdown.options]
    assert texts == ["Please select an option", "Option 1",
                     "Option 2"]
    selected = dropdown.first_selected_option
    assert selected.text == "Please select an option"
    assert not dropdown.options[0].is_enabled()   # disabled option


def test_select_option(driver):
    dropdown = Select(open_page(driver, URL, By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1"
    dropdown.select_by_value("2")
    selected = dropdown.first_selected_option
    assert selected.get_attribute("value") == "2"
    dropdown.select_by_index(1)
    assert dropdown.first_selected_option.text == "Option 1"
