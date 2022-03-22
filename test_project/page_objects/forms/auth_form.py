from selenium.webdriver.support import expected_conditions as EC

from my_webdriver.page_objects.base_objects.base_form import BaseForm
from my_webdriver.page_objects.elements.form import Form
from my_webdriver.page_objects.elements.input import Input
from my_webdriver.page_objects.elements.button import Button
from my_webdriver.page_objects.elements.content import Content


class AuthForm(BaseForm):
    def __init__(self):
        super().__init__(
            form_name='AuthForm',
            uniq_element=Form(
                locator_type='css selector',
                locator='form.ant-form',
                element_name='FormAuth'
            )
        )
        self.login_input = Input(
            locator_type='id',
            locator='username',
            element_name='LoginInput'
        )
        self.pwd_input = Input(
            locator_type='id',
            locator='password',
            element_name='PwdInput'
        )
        self.mask_pwd_btn = Button(
            locator_type='css selector',
            locator='span.ant-input-suffix',
            element_name='PwdMaskBtn'
        )
        self.submit_btn = Button(
            locator_type='xpath',
            locator='//button[contains(@type,"submit")]',
            element_name='SubmitBtn'
        )
        self.alert_text = Content(
            locator_type='xpath',
            locator='//div[contains(@role, "alert")]',
            element_name='AlertText'
        )

    def wait_visibility_of_alert(self):
        return self.alert_text.wait().until(EC.visibility_of_element_located(self.alert_text.locator))

