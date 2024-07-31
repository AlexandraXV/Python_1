from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")


def test_data_farm():
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Alina")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Kulikova")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("190000")
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    sleep(3)

    wait = WebDriverWait(driver, 10)
    assert wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary_total_label"), "$58.29")
    )
    driver.quit()