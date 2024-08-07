from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def test_data(self, second):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(
            Keys.BACKSPACE, second)
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-warning").click()

    def wait(self, total):
        wait_txt = WebDriverWait(self.driver, 50)

        element = (By.CLASS_NAME, 'screen')
        condition = EC.text_to_be_present_in_element(element, total)
        assert wait_txt.until(condition)


        # ПОЧЕМУ НЕ РАБОТАЕТ С ЭТИМ СИНТАКСИСОМ, НО РАБОТАЕТ С ТЕМ, ЧТО ВЫШЕ?
        # assert wait_txt.until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "screen"), total)
        #     )
