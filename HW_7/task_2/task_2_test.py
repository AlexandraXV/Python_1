from selenium import webdriver

from InfoPage import InfoPage


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
