from my_webdriver.browser_factory.browser import WebDriver
from selenium.common.exceptions import NoAlertPresentException


class Alert:

    @staticmethod
    def is_alert_invisible():
        try:
            WebDriver().switch_to().alert
        except NoAlertPresentException:
            return True
        else:
            return False
