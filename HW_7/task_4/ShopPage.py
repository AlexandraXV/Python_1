from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @allure.step ("Авторизация по {user_name} : {password}")
    def login(self, user_name, password):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step ("Добавление товара в корзин, нажатие на кнопку Checkout")
    def cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    @allure.step ("Заполнение формы пользователя, нажатие на кнопку Continue")
    def your_information(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)

        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step ("Отображение конечной суммы")
    def wait(self):
        wait_txt = WebDriverWait(self.driver, 10)
        assert wait_txt.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".summary_total_label"), "$58.29"))

        total = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        print(total)