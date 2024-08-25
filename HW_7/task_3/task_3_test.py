from selenium import webdriver
from CalculatorPage import CalculatorPage

import allure

@allure.title("Проверка калькулятора")
@allure.description("Заполнение время отправки запроса в калькуляторе. Использование селекторов для нажатия на клавиши.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("CREATE")
def test_info():
    driver = webdriver.Chrome()

    Calculator_Page = CalculatorPage(driver)
    Calculator_Page.test_data("45")
    Calculator_Page.wait("15")

    driver.quit()
