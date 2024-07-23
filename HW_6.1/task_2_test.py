from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

def test_data_farm():
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(Keys.BACKSPACE, "45")
    
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()

    wait = WebDriverWait(driver, 50)
    assert wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )