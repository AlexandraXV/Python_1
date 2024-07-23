from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.saucedemo.com/")


# def test_data_farm():
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
sleep(3)

driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Alina")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Kulikova")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("190000")
sleep(3)

driver.find_element(By.CSS_SELECTOR, "#continue").click()

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(total)

driver.quit()

sleep(6)