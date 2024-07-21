from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")


# click on the button


blue_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")

for x in range(3):
    blue_button.click()
    sleep(2)
    driver.switch_to.alert.accept()


sleep(3)

driver.quit()