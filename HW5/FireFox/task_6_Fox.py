from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

# ввести юзернейм

UserName = driver.find_element(By.CSS_SELECTOR, "#username")

UserName.send_keys("tomsmith")
sleep(2)

# ввести пароль

pas = driver.find_element(By.CSS_SELECTOR, "#password")

pas.send_keys("SuperSecretPassword!")
sleep(2)

# нажать на кнопку "Логин"

driver.find_element(By.XPATH, '//*[@id="login"]/button').click()


sleep(2)
driver.quit()