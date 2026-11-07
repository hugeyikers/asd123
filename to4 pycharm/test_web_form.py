"""Selenium Web Form – form fields, their state and submission."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from config import SELENIUM_WEB_URL
from helpers import open_page, wait_for
from selenium.common.exceptions import ElementNotInteractableException


@pytest.fixture
def page(driver):
    """Opens the form and returns the driver."""
    url = f"{SELENIUM_WEB_URL}/web-form.html"
    open_page(driver, url, By.TAG_NAME, "form")
    return driver


def test_text_fields(page):
    text = page.find_element(By.ID, "my-text-id")
    password = page.find_element(By.NAME, "my-password")
    textarea = page.find_element(By.NAME, "my-textarea")
    text.send_keys("Selenium")
    password.send_keys("Secret123")
    textarea.send_keys("Line 1\nLine 2")


def test_attribute_vs_property(page):
    text = page.find_element(By.ID, "my-text-id")
    text.send_keys("abc")
    assert text.get_dom_attribute("value") is None  # not in the HTML
    assert text.get_property("value") == "abc"      # field state
    assert text.get_attribute("value") == "abc"     # "smart" read
    assert text.get_dom_attribute("myprop") == "myvalue"
    assert text.get_property("myprop") is None


def test_disabled_and_readonly(page):
    disabled = page.find_element(By.NAME, "my-disabled")
    readonly = page.find_element(By.NAME, "my-readonly")
    assert not disabled.is_enabled()
    assert readonly.is_enabled()             # readonly ≠ disabled
    assert readonly.get_property("readOnly") is True
    readonly.send_keys("XYZ")                # nothing changes
    assert readonly.get_property("value") == "Readonly input"


def test_select_and_datalist(page):
    dropdown = Select(page.find_element(By.NAME, "my-select"))
    dropdown.select_by_visible_text("Two")
    selected = dropdown.first_selected_option
    assert selected.get_attribute("value") == "2"
    css = "#my-options option"
    options = page.find_elements(By.CSS_SELECTOR, css)
    cities = [o.get_attribute("value") for o in options]
    assert len(cities) == 5 and "Seattle" in cities
    field = page.find_element(By.NAME, "my-datalist")
    field.send_keys("Seattle")
    assert field.get_property("value") == "Seattle"

def test_checkbox_and_radio(page):
    checked = page.find_element(By.ID, "my-check-1")
    unchecked = page.find_element(By.ID, "my-check-2")
    assert checked.is_selected()
    assert not unchecked.is_selected()
    radio1 = page.find_element(By.ID, "my-radio-1")
    radio2 = page.find_element(By.ID, "my-radio-2")
    radio2.click()
    assert radio2.is_selected()
    assert not radio1.is_selected()


def test_submit_form(page):
    page.find_element(By.ID, "my-text-id").send_keys("Selenium")
    button = page.find_element(By.TAG_NAME, "button")
    button.click()
    message = wait_for(page, By.ID, "message")
    assert message.text == "Received!"
    assert page.title == "Web form - target page"
    heading = page.find_element(By.TAG_NAME, "h1")
    assert heading.text == "Form submitted"
    assert "my-text=Selenium" in page.current_url


def test_range_slider(page):
    slider = page.find_element(By.NAME, "my-range")
    default_value = slider.get_property("value")
    assert default_value == "5"


def test_button_css_color(page):
    button = page.find_element(By.TAG_NAME, "button")
    color = button.value_of_css_property("color")
    assert color == "rgba(13, 110, 253, 1)"


def test_send_keys_disabled(page):
    disabled_input = page.find_element(By.NAME, "my-disabled")

    with pytest.raises(ElementNotInteractableException):
        disabled_input.send_keys("Test text")