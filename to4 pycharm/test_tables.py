"""Tables – reading a column and sorting by clicking the header."""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL
from helpers import open_page, wait_for_class

URL = f"{INTERNET_URL}/tables"


def column(driver, table_id, index):
    """Cell texts of column `index` (from 1) of the table with this id."""
    css = f"#{table_id} tbody td:nth-child({index})"
    cells = driver.find_elements(By.CSS_SELECTOR, css)
    return [td.text for td in cells]


def test_read_column(driver):
    open_page(driver, URL, By.ID, "table1")
    assert column(driver, "table1", 1) == [
        "Smith", "Bach", "Doe", "Conway"]


def test_sort_last_names(driver):
    open_page(driver, URL, By.ID, "table1")
    header = (By.XPATH, "//table[@id='table1']//th[1]")
    driver.find_element(*header).click()
    wait_for_class(driver, header, "headerSortDown")  # A→Z
    last_names = column(driver, "table1", 1)
    assert last_names == sorted(last_names)


def amounts(driver):
    """The Due column of table 2 as numbers, e.g. '$50.00' -> 50.0."""
    css = "#table2 td.dues"
    cells = driver.find_elements(By.CSS_SELECTOR, css)
    return [float(td.text.replace("$", "")) for td in cells]


def test_sort_amounts_descending(driver):
    open_page(driver, URL, By.ID, "table2")
    due = (By.CSS_SELECTOR, "#table2 th:nth-child(4)")
    driver.find_element(*due).click()
    wait_for_class(driver, due, "headerSortDown")   # ascending
    assert amounts(driver) == sorted(amounts(driver))
    driver.find_element(*due).click()
    wait_for_class(driver, due, "headerSortUp")     # descending
    assert amounts(driver) == sorted(amounts(driver), reverse=True)

def test_emails_contain_at_symbol(driver):
    open_page(driver, URL, By.ID, "table1")
    emails = column(driver, "table1", 3)
    assert all("@" in email for email in emails)
