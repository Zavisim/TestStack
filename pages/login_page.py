import time
from idlelib import browser

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from elements.element import Element
from pages.base import BasePage


class LoginPage(BasePage):
    URL = "https://demo.app.stack-it.ru/fl/redirect?from=%2Faccounts%3FparentID%3D4867%26page%3D1"

    @property
    def login_input(self):
        return Element(self.driver, By.CSS_SELECTOR, '.v-text-field__slot [data-cy="login"]')

    @property
    def password_input(self):
        return Element(self.driver, By.CSS_SELECTOR, '.v-text-field__slot [data-cy="password"]')

    @property
    def authorization_button(self):
        return Element(self.driver, By.CSS_SELECTOR, '.pt-12 .v-btn__content')

    @property
    def continue_logging(self):
        return Element(self.driver, By.CSS_SELECTOR, '.v-card__actions [data-cy="btn-yes"]')

    def login(self, username: str, password: str):
        self.login_input.send_keys(username, with_clear=False)
        self.password_input.send_keys(password, with_clear=False)
        self.authorization_button.click()
        time.sleep(2)
        if self.continue_logging.is_located():
            self.continue_logging.click()
