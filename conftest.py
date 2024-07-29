import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage, AddRecordMenu


@pytest.fixture
def browser() -> WebDriver:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def accounts_page(browser, authorization) -> AccountsPage:
    page = AccountsPage(browser)
    page.open()
    return page


@pytest.fixture
def login_page(browser) -> LoginPage:
    return LoginPage(browser)


@pytest.fixture
def add_record_menu(browser) -> AddRecordMenu:
    return AddRecordMenu(browser)


@pytest.fixture
def authorization(login_page):
    login_page.open()
    login_page.login('DEMOWEB', 'awdrgy')
    time.sleep(2)
