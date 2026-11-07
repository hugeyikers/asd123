"""DevTools exercise: CSS and XPath locators.

Fill in the table: for each element enter a CSS selector
and an XPath expression (checked in DevTools: $$() and $x()).
"""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL, SELENIUM_WEB_URL
from helpers import open_page

I, W = INTERNET_URL, SELENIUM_WEB_URL + "/web-form.html"
LOCATORS = [
    (I + "/login", "#username", "//input[@id='username']"),
    (I + "/login", "button[type='submit']", "//button[@type='submit']"),
    (I + "/login", "label[for='password']", "//label[@for='password']"),
    (I + "/checkboxes", "input[type='checkbox']:nth-of-type(2)", "(//input[@type='checkbox'])[2]"),
    (I + "/tables", "table#table2 tbody tr:nth-child(3) td.email", '''//table[@id='table2']//td[@class='email' and text()='jdoe@hotmail.com']'''),
    (I + "/tables", "table#table1 thead th:nth-child(4) span", '''//table[@id='table1']//span[text()='Due']'''),
    (I + "/add_remove_elements/", "button[onclick='addElement()']", '''//button[text()='Add Element']'''),
    (W, '#my-text-id', "//input[@id='my-text-id']"),
    (W, "input[name='my-disabled']", '''//input[@name='my-disabled']'''),
    (W, "option[value='2']", '''//option[@value='2']'''),
    (W, "button[type='submit']", '''//button[@type='submit']'''),
    (W, "a[href='./index.html']", '''//a[contains(text(), 'Return to index')]'''),
]


@pytest.mark.parametrize("url, css, xpath", LOCATORS)
def test_css_and_xpath(driver, url, css, xpath):
    if not css or not xpath:
        pytest.skip("TODO: fill in the locators")
    open_page(driver, url, By.CSS_SELECTOR, "#content, form")
    by_css = driver.find_elements(By.CSS_SELECTOR, css)
    by_xpath = driver.find_elements(By.XPATH, xpath)
    assert len(by_css) == 1, "CSS: expected exactly 1 element"
    assert len(by_xpath) == 1, "XPath: expected exactly 1 element"
    assert by_css[0] == by_xpath[0]           # the same element
