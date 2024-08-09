from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def add_book(self):
        buy_book = self.driver.find_elements(
            By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
        print(buy_book)
        counter = 0
        for x in buy_book:
            x.click()
            counter += 1

        return counter
