from my_webdriver.page_objects.base_objects.base_form import BaseForm
from my_webdriver.page_objects.elements.content import Content


class MainForm(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='MainForm',
            uniq_element=Content(
                locator_type='css selector',
                locator='main.ant-layout-content',
                element_name='MainForm'
            )
        )
