from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_webdriver.browser_factory.browser import WebDriver
from my_webdriver.utils.config_manager import ConfigManager
from abc import ABC


class BaseForm(ABC):

    def __init__(self, uniq_element=None, form_name=None):
        self.uniq_element = uniq_element
        self.form_name = form_name

    def is_page_open(self):
        WebDriverWait(WebDriver().get_driver(), ConfigManager().get_driver_conf()["waiting_time"]) \
            .until(EC.visibility_of(self.uniq_element._find_element()))

        return True

