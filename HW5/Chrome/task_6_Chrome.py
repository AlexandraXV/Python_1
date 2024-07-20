from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

UserName = driver.find_element(By.CSS_SELECTOR, "#username")

UserName.send_keys("tomsmith")
sleep(2)


pas = driver.find_element(By.CSS_SELECTOR, "#password")

pas.send_keys("SuperSecretPassword!")
sleep(2)


driver.find_element(By.XPATH, '//*[@id="login"]/button').click()


sleep(5)