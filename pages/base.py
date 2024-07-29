import time


class BasePage:
    URL = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)
