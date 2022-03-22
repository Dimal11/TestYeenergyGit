from selenium.webdriver import Keys


from my_webdriver.page_objects.base_objects.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, locator_type, locator, element_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=element_name)

    def send_keys(self, text):
        self.clear()
        self._find_element().send_keys(text)

    def clear(self):
        self._find_element().send_keys(Keys.CONTROL, 'a')
        self._find_element().send_keys(Keys.DELETE)
