from selenium.webdriver.support.ui import WebDriverWait

from my_webdriver.browser_factory import BrowseFactory
from my_webdriver.singleton import Singleton
from my_webdriver.utils.config_manager import ConfigManager


class WebDriver(metaclass=Singleton):
    def __init__(self):
        self.__driver = BrowseFactory().get_driver()

    def get_driver(self):
        return self.__driver

    def find_element(self, locator: tuple):
        return self.__driver.find_element(*locator)

    def submit(self, locator: tuple):
        return self.find_element(locator).submit()

    def switch_to(self):
        return self.__driver.switch_to

    def stop_driver(self):
        self.__driver.quit()
        self._instances = {}

    def wait(self):
        return WebDriverWait(self.__driver, ConfigManager().get_driver_conf()["waiting_time"])

    def execute_script(self, script: str):
        return self.__driver.execute_script(script=script)
