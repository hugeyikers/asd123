"""Helper functions used in the tests (exercises 4).

After navigation we wait for an element characteristic of the page
(a "marker") to be sure we are working on the NEW page.
Explicit waits (WebDriverWait) in detail – lecture 5.
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for(driver, *locator, timeout=10):
    """Waits (max `timeout` s) until the element is in the DOM."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator))


def open_page(driver, url, *marker):
    """Opens the URL and waits for the page marker; returns it."""
    driver.get(url)
    return wait_for(driver, *marker)


def wait_for_class(driver, locator, css_class, timeout=10):
    """Waits until the element's class attribute contains `css_class`."""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element_attribute(
            locator, "class", css_class))
