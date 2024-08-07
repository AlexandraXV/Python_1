from selenium import webdriver

from CalculatorPage import CalculatorPage


def test_info():
    driver = webdriver.Chrome()

    Calculator_Page = CalculatorPage(driver)
    Calculator_Page.test_data("45")
    Calculator_Page.wait("15")

    driver.quit()
