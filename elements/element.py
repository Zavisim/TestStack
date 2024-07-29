from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Element:
    def __init__(self, driver, by, locator):
        self.driver = driver
        self.by = by
        self.locator = locator

    def find(self):
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((self.by, self.locator)))

    def finds(self):
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((self.by, self.locator)))

    def count(self):
        return len(self.finds())

    def click(self):
        self.find().click()

    def send_keys(self, text, with_clear=True):
        if with_clear:
            self.clear()
        self.find().send_keys(text)

    def clear(self):
        elem = self.find()
        elem.send_keys(Keys.CONTROL + 'a')
        elem.send_keys(Keys.BACKSPACE)

    def is_located(self):
        try:
            self.driver.find_element(self.by, self.locator)
            return True
        except NoSuchElementException:
            return False
