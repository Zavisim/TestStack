import time


def test_correct_authorization(browser, login_page):
    login_page.open()
    login_page.login('DEMOWEB', 'awdrgy')
    time.sleep(2)
    assert "https://demo.app.stack-it.ru/fl/" in browser.current_url
