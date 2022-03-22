from my_webdriver.browser_factory.browser import WebDriver
from abc import ABC


class BaseElement(ABC):

    def __init__(self, locator_type, locator, element_name):
        self.locator = (locator_type, locator)
        self.element_name = element_name

    def _find_element(self):
        element = WebDriver().find_element(self.locator)
        return element

    def _find_elements(self):
        elements = WebDriver().get_driver().find_elements(self.locator)
        return elements

    def get_text(self):
        return self._find_element().text

    def click(self):
        self._find_element().click()

    def is_displayed(self):
        return self._find_element().is_displayed()

    def get_attr(self, attr_name: str):
        return self._find_element().get_attribute(attr_name)

    def submit(self):
        self._find_element().submit()

    def wait(self):
        return WebDriver().wait()
