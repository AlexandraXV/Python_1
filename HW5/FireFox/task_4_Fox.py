from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep (2)

# click on the button "Close"

driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p').click()

sleep(2)
driver.quit()