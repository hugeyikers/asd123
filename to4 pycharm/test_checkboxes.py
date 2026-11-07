"""Checkboxes – is_selected() state and clicks."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page

URL = f"{INTERNET_URL}/checkboxes"
CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")


def test_initial_state(driver):
    open_page(driver, URL, By.ID, "checkboxes")
    boxes = driver.find_elements(*CHECKBOXES)
    assert len(boxes) == 2
    assert [b.is_selected() for b in boxes] == [False, True]


def test_check_and_uncheck(driver):
    open_page(driver, URL, By.ID, "checkboxes")
    first, second = driver.find_elements(*CHECKBOXES)
    first.click()
    second.click()
    assert first.is_selected()
    assert not second.is_selected()


def test_check_only_unchecked(driver):
    open_page(driver, URL, By.ID, "checkboxes")
    boxes = driver.find_elements(*CHECKBOXES)
    for box in boxes:
        if not box.is_selected():
            box.click()
    assert all(b.is_selected() for b in boxes)