"""Shared fixtures for all tests (conftest.py)."""
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """A new Chrome browser for each test."""
    drv = webdriver.Chrome()  # Selenium Manager picks the driver
    drv.implicitly_wait(0)    # explicit waits only
    yield drv                 # the test runs here
    drv.quit()                # cleanup – also after a failure