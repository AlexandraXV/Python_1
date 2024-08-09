from selenium import webdriver
from ShopPage import ShopPage


def test_shop():
    driver = webdriver.Chrome()

    shop_page = ShopPage(driver)
    shop_page.login("standard_user", "secret_sauce")
    shop_page.cart()
    shop_page.your_information("Alina", "Kulikova", "190000")
    shop_page.wait()

    driver.quit()