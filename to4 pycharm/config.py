"""URLs of the pages used in the exercises.

By default the tests use public pages and a local XAMPP.
Each URL can be overridden with an environment variable (e.g. in PyCharm: Run > Edit Configurations > Environment variables).
"""
import os

INTERNET_URL = os.getenv("INTERNET_URL", "https://the-internet.herokuapp.com").rstrip("/")
SELENIUM_WEB_URL = os.getenv("SELENIUM_WEB_URL", "https://www.selenium.dev/selenium/web").rstrip("/")
SKLEPTO_URL = os.getenv("SKLEPTO_URL", "http://localhost/sklepto").rstrip("/")
