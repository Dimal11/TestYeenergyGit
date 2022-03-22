from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from my_webdriver.utils.config_manager import ConfigManager


class BrowseFactory:

    @staticmethod
    def get_driver():
        driver = None
        driver_conf = ConfigManager.get_driver_conf()
        if driver_conf["browser"] == "chrome":
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument(f'--window-size={driver_conf["size"]}')
            # options.add_argument('--headless')
            driver = webdriver.Chrome(service=service, options=options)
        elif driver_conf["browser"] == "firefox":
            service = Service(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            options.add_argument(f'--window-size={driver_conf["size"]}')
            # options.add_argument("--headless")
            driver = webdriver.Firefox(service=service)
        elif driver_conf["browser"] == "opera":
            driver_path = OperaDriverManager().install()
            options = webdriver.ChromeOptions()
            options.add_argument(f'--window-size={driver_conf["size"]}')
            options.add_argument('--remote-debugging-port=9222')
            # options.add_argument('--headless')
            driver = webdriver.Opera(executable_path=driver_path, options=options)

        return driver
