import pytest

from my_webdriver.browser_factory.browser import WebDriver


@pytest.fixture()
def driver():
    yield WebDriver().get_driver()
    WebDriver().stop_driver()
