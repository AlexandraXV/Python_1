from MainPage import MainPage
from ResultPage import ResultPage
from CartPage import CartPage

from selenium import webdriver


def test_cart_counter():
    driver = webdriver.Chrome()

    main_Page = MainPage(driver)
    main_Page.set_cookie_policy()
    main_Page.search('python')

    resultPage = ResultPage(driver)
    to_be = resultPage.add_book()

    cartPage = CartPage(driver)
    cartPage.get()
    as_is = cartPage.get_counter()

    assert to_be == as_is
    driver.quit()
