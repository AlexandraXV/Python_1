from selenium import webdriver
from ShopPage import ShopPage

import allure


@allure.title("Проверка интернет-магазина")
@allure.description("Отправка вещей в корзину. Переход в корзину и заполнение формы. Отображение итоговой суммы.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("CREATE")
def test_shop():
    driver = webdriver.Chrome()

    shop_page = ShopPage(driver)
    shop_page.login("standard_user", "secret_sauce")
    shop_page.cart()
    shop_page.your_information("Alina", "Kulikova", "190000")
    shop_page.wait()

    driver.quit()
