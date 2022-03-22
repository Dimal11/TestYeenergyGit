from my_webdriver.page_objects.base_objects.base_element import BaseElement


class Link(BaseElement):
    def __init__(self, locator_type, locator, element_name):
        super().__init__(locator_type=locator_type, locator=locator, element_name=element_name)
