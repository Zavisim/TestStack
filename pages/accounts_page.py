import time

from selenium.webdriver.common.by import By

from elements.element import Element
from pages.base import BasePage


class AccountsPage(BasePage):
    URL = "https://demo.app.stack-it.ru/fl/accounts"

    @property
    def add_record(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-add"]')

    @property
    def add_name_of_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-test-id="Название района"]')

    @property
    def add_number_of_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-test-id="Номер в списке"]')

    @property
    def btn_cancel_add_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-cancel"]')

    @property
    def btn_exit_add_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-close"]')

    @property
    def save_btn_new_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-save"]')

    @property
    def editing_name_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-test-id="Название района"]')

    @property
    def editing_number_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-test-id="Номер в списке"]')

    @property
    def editing_btn_save(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-save"]')

    @property
    def btn_delete_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-delete"]')

    @property
    def btn_yes_delete_area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="btn-yes"]')

    @property
    def add_menu(self):
        return AddRecordMenu(self.driver)

    @property
    def table_rows(self):
        return Element(self.driver, By.CSS_SELECTOR, 'tbody tr')

    @property
    def area_name(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-field="название"]')

    def get_number_by_name(self, name):
        names = self.area_name.finds()
        index = 0
        for n in names:
            if n.text == name:
                return index
            index += 1

    def edit_table_element(self, number):
        elem = Element(self.driver, By.CSS_SELECTOR, f'tbody tr:nth-child({number}) [data-cy="btn-edit"]')
        elem.click()

    def select_table_element(self, number):
        elem = Element(self.driver, By.CSS_SELECTOR, f'tbody tr:nth-child({number}) [class="v-input__slot"]')
        elem.click()

    def cancel_dialog_b0x(self):
        self.add_record.click()
        self.add_menu.area.click()
        time.sleep(2)
        self.btn_cancel_add_area.click()

    def exit_dialog_box(self):
        self.add_record.click()
        self.add_menu.area.click()
        time.sleep(2)
        self.btn_exit_add_area.click()

    def add_area(self, name_of_area, number_of_record):
        self.add_record.click()
        self.add_menu.area.click()
        self.add_name_of_area.send_keys(name_of_area)
        self.add_number_of_area.send_keys(number_of_record)
        self.save_btn_new_area.click()
        time.sleep(2)

    def delete_record(self, number_of_record):
        self.select_table_element(number_of_record)
        self.btn_delete_area.click()
        self.btn_yes_delete_area.click()
        time.sleep(1)


class AddRecordMenu(Element):
    def __init__(self, driver):
        super().__init__(driver, By.CSS_SELECTOR, '.v-menu__content')

    @property
    def area(self):
        return Element(self.driver, By.CSS_SELECTOR, '[data-cy="stack-menu-list-item"]')
