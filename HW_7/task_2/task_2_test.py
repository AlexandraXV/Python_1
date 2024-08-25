from selenium import webdriver
from InfoPage import InfoPage

import allure


@allure.title("Заполнение формы")
@allure.description("Заполнение формы значениями. Проверка работоспособности кнопки, а также на не заполненные поля.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("CREATE")
def test_info():
    driver = webdriver.Chrome()

    info_Page = InfoPage(driver)
    info_Page.test_data_farm(
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "test@skypro.com",
        "+7985899998787",
        "Москва",
        "Россия",
        "QA",
        "SkyPro")

    driver.quit()
