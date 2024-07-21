from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(16)

button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()

txt = driver.find_element(By.CSS_SELECTOR, ".bg-success").text
print(txt)

driver.quit