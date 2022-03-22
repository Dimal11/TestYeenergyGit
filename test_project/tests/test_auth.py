import time

from my_webdriver.utils.config_manager import ConfigManager
from test_project.page_objects.forms.auth_form import AuthForm
from test_project.page_objects.forms.main_form import MainForm


class TestAuth:

    def test_auth(self, driver):
        ''' Тестування сторінки авторизації '''

        ''' 1. Перехід до сторінки авторизації. 
        Очікуваний результат: Сторінка авторизації відкрита'''

        driver.get(ConfigManager().get_url())
        assert AuthForm().is_page_open() is True, 'Помилка при відкритті сторінки авторизації'

        test_auth_data = ConfigManager().get_test_data('auth_data.json')
        login = test_auth_data['login']
        password = test_auth_data['password']
        wrong_login = test_auth_data['wrong_login']
        wrong_pwd = test_auth_data['wrong_password']

        ''' 2. Введення невірного логіну та паролю.
            Очікуваний результат: Відмова у авторизації та поява напису 
            "Відмовлено у доступі, зверніться до адміністратора мережі" '''

        AuthForm().login_input.send_keys(wrong_login)
        AuthForm().pwd_input.send_keys(wrong_pwd)
        AuthForm().submit_btn.click()
        AuthForm().wait_visibility_of_alert()
        assert AuthForm().alert_text.get_text() == 'Відмовлено у доступі, зверніться до адміністратора мережі', \
            'Попередження при введенні невірного логіну та паролю працює не корректно'

        ''' 3. Введення вірного логіну та невірного паролю.
            Очікуваний результат: Відмова у авторизації та поява напису 
            "Відмовлено у доступі, зверніться до адміністратора мережі" '''

        AuthForm().login_input.send_keys(login)
        AuthForm().pwd_input.send_keys(wrong_pwd)
        AuthForm().submit_btn.click()
        AuthForm().wait_visibility_of_alert()
        assert AuthForm().alert_text.get_text() == 'Відмовлено у доступі, зверніться до адміністратора мережі', \
            'Попередження при введенні невірного паролю працює не корректно'

        ''' 4. Введення невірного логіну та вірного паролю.
            Очікуваний результат: Відмова у авторизації та поява напису 
            "Відмовлено у доступі, зверніться до адміністратора мережі" '''

        AuthForm().login_input.clear()
        AuthForm().login_input.send_keys(wrong_login)
        AuthForm().pwd_input.send_keys(password)
        AuthForm().submit_btn.click()
        AuthForm().wait_visibility_of_alert()
        assert AuthForm().alert_text.get_text() == 'Відмовлено у доступі, зверніться до адміністратора мережі', \
            'Попередження при введенні невірного логіну працює не корректно'

        ''' 5. Введення вірного логіну та паролю. Перевірка маски паролю
            Очікуваний результат: Маска паролю активна. '''

        AuthForm().login_input.send_keys(login)
        assert AuthForm().pwd_input.get_attr('type') == 'password', 'Маска паролю не активована за замовченням'

        ''' 6. Введення вірного логіну та паролю. Зняття маски паролю
                    Очікуваний результат: Маска паролю деактивована. '''

        AuthForm().mask_pwd_btn.click()
        assert AuthForm().pwd_input.get_attr('type') == 'text', 'Маска паролю працює не коректно'

        '''7. Клік на кнопку "Увійти".
        Очікуваний результат: Перехід на головну сторінку сервісу.'''

        AuthForm().submit_btn.click()
        time.sleep(5)
        assert MainForm().is_page_open() is True, 'Не вдалося авторизуватися у сервісі'
